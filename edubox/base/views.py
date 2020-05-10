from edubox.base.serializers import *
from edubox.base.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

class PostsListCreate(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class Test(APIView):
    def get(self, request,*args, **kwargs):
        return Response({'success':True})