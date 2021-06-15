from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from edubox.users.serializers import CreateAuthUserSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group
from rest_framework.response import Response
from edubox.users.services import services
from rest_framework import status

User = get_user_model()


class CreateAndRetrieveAuthUserView(generics.CreateAPIView, generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    model = User
    raise_exception = True
    serializer_class = CreateAuthUserSerializer

    def post(self, request):    
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        self.serializer_class = UserSerializer
        return super().get(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name','photo','is_superuser']
        extra_kwargs = {'password': {'write_only': True}, 'is_superuser':{'read_only': True},} 


class GetUserView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
