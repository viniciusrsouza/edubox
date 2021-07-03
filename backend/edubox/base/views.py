from edubox.base.serializers import *
from edubox.base.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from edubox.base.serializers import *
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, get_list_or_404
import time


class PostsListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostsList(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        #if not request.user.is_authenticated:
        #    return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = get_list_or_404(Post, course=kwargs['pk'])
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

class PostDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CourseListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]

    def post(self, request, token):
        related_course = get_object_or_404(Course, code=token)
        m = Membership.objects.create(
            user=request.user, course=related_course, role=3)
        m.save()
        return Response(status=status.HTTP_201_CREATED)
    
    def  put(self, request, user, course, role):
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
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = get_object_or_404(Course, id=kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AssignmentListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

#list all members of a course
class MemberList(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = MembershipSerializer

    def retrieve(self, request, *args, **kwargs):
        #if not request.user.is_authenticated:
        #    return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = get_list_or_404(Membership, course=kwargs['pk'])
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

class Test2(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()

        # Criar objeto
        #course_created = Course.objects.create(title="Sd", description="sistemas distribuidos")
        #print(course_created.title, course_created.description)

        # alterar objeto
        #course = Course.objects.get(id=2)
        #course.title = "Compiladores 2"
        #course.description = "Continua chata pra caralho"
        # course.save()

        # deletar
        #course = Course.objects.get(id=1)
        # course.delete()

        # filter
        #courses = Course.objects.filter(id__in=[2,3])
        # for course in courses:
        #    course.title = course.title + ' alo'
        #    course.save()
        # courses = Course.objects.filter(author__org__name)
        # autor = Author.objects.filter(nome='caio')

        return Response({"Ola": "Ok", "data": CourseSerializer(courses, many=True).data})

    def post(self, request, *args, **kwargs):
        # CRIANDO NA MÃO
        # print(request.data)
        #course_created = Course.objects.create(**request.data)
        # ou Course.objects.create(title=request.data.get('title), description=request.data.get('description'))

        # CRIANDO COM SERIALIZER
        course_serializer = CourseSerializer(data=request.data)
        course_serializer.is_valid(raise_exception=True)
        course_serializer.save()
        return Response({})


class Test3(APIView):
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs['pk'])
        course.title = request.data.get('title')
        course.description = request.data.get('description')
        course.save()
        return Response(course)


class Test(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'success': True})
