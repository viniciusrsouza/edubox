from rest_framework import serializers
from edubox.users.models import User


class CreateAuthUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200)
    confirm_password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = (['id',
                   'email',
                   'name',
                   'password',
                   'confirm_password'])


class UserSerializer(serializers.ModelSerializer):

    courses = serializers.SerializerMethodField()

    def get_courses(self, instance):
        courses_list = []
        a = instance.course_set.all()
        for i in a:
            courses_list.append(i.id)
        return courses_list

    class Meta:
        model = User
        fields = (['id',
                   'email',
                   'name',
                   'courses', ])

    def create(self, validated_data):
        return User.objects.create(**validated_data)
