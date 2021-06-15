from edubox.base.serializers import *
from edubox.base.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from edubox.base.serializers import *


class PostsListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CourseListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = request.user
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
        #course.save()

        #deletar
        #course = Course.objects.get(id=1)
        #course.delete()

        # filter
        #courses = Course.objects.filter(id__in=[2,3])
        #for course in courses:
        #    course.title = course.title + ' alo'
        #    course.save()
        # courses = Course.objects.filter(author__org__name)
        # autor = Author.objects.filter(nome='caio')

        return Response({"Ola":"Ok", "data":CourseSerializer(courses, many=True).data})

    def post(self, request, *args, **kwargs):
        # CRIANDO NA MÃO
        #print(request.data)
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
    def get(self, request,*args, **kwargs):
        return Response({'success':True})