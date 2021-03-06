from edubox.base.serializers import *
from edubox.base.models import *
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from edubox.base.serializers import *
from django.shortcuts import get_object_or_404, get_list_or_404


class PostsListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(course=self.kwargs['course'])
        if 'assignment' in self.request.query_params:
            return queryset.exclude(assignment__isnull=True)
        return queryset

    def get(self, request, *args, **kwargs):
        self.serializer_class = PostListSerializer
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'assignment' in request.data:
            assignment = request.data['assignment']
            assignment_serializer = AssignmentSerializer(data=assignment)
            if assignment_serializer.is_valid():
                assignment = assignment_serializer.save()
                request.data.update({'assignment': assignment.id})
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        course = get_object_or_404(Course,
                                   members=self.request.user,
                                   id=self.kwargs['course'])
        serializer.save(author=self.request.user, course=course)


class PostsRetrieve(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def retrieve(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #    return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = get_list_or_404(Post, course=kwargs['course'])
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CourseListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(members=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        headers = self.get_success_headers(serializer.data)
        m = Membership.objects.create(
            user=request.user, course=serializer.instance, role=1)
        m.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MembershipCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, token):
        related_course = get_object_or_404(Course, code=token)
        m = Membership.objects.create(
            user=request.user, course=related_course, role=3)
        m.save()
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request, user, course, role):
        member = get_object_or_404(Membership, user=user, course=course)
        member.role = role
        member.save()
        return Response(status=status.HTTP_200_OK)
    '''
    def put(self, request, user, course):
        member = get_object_or_404(Membership, user=user, course=course)
        serializer = Membership(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''


class CourseDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Course, id=kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(Course, id=kwargs['pk'])
        instance.delete()
        return Response(status=status.HTTP_200_OK)


class AssignmentListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        print(self.kwargs)
        course = self.kwargs['course_pk']
        return Assignment.objects.filter(course=course)

    def get(self, request, *args, **kwargs):
        print(request)
        return super().get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        obj = get_object_or_404(Course, id=self.kwargs['course_pk'])
        serializer.save(course=obj)


class AssignmentDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

# list all members of a course


class MemberList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MembershipSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['role']

    def get_queryset(self):
        return Membership.objects.filter(course=self.kwargs['pk'])
