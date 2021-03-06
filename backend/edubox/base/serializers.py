from rest_framework import serializers
from edubox.users.serializers import UserSerializer
from edubox.users.models import *
from edubox.base.models import *
from django.utils import crypto


class PostFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostFile
        fields = ['id',
                  'post',
                  'file_path', ]

    def create(self, validated_data):
        post = validated_data.pop('post')
        instance = Post.objects.get(id=post)
        return PostFile.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.file_path = validated_data.get(
            'file_path', instance.file_path)
        instance.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id',
                  'title',
                  'description',
                  'created_at',
                  'owner',
                  'code',
                  'role']
        read_only_fields = ['owner', 'code', 'role']

    def get_role(self, obj):
        current_user = self.context['request'].user
        if current_user == obj.owner:
            return 'owner'
        return 'student'

    def create(self, validated_data):
        validated_data['code'] = crypto.get_random_string(length=8)
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance


class CourseSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ['id',
                  'deadline']

    def create(self, validated_data):
        return Assignment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance


class MembershipSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField('get_name')
    email = serializers.SerializerMethodField('get_email')
    photo = serializers.SerializerMethodField('get_photo')

    def get_name(self, instance):
        return instance.user.name

    def get_email(self, instance):
        return instance.user.email

    def get_photo(self, instance):
        try:
            photo = instance.user.photo_url
            return photo
        except ValueError as x:
            return "null"

    class Meta:
        model = Membership
        fields = ['name',
                  'email',
                  'photo',
                  'role']

    def create(self, validated_data):
        return Membership.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
                  'author',
                  'course',
                  'title',
                  'text',
                  'assignment',
                  'created_at']
        read_only_fields = ['author', 'id', 'created_at', 'course']


class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    assignment = AssignmentSerializer()

    class Meta:
        model = Post
        fields = ['id',
                  'author',
                  'course',
                  'title',
                  'text',
                  'assignment',
                  'created_at']
        read_only_fields = ['author', 'id',
                            'created_at', 'course', 'assignment']
