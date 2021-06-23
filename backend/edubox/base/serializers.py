from rest_framework import serializers
from edubox.users.serializers import UserSerializer
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


class PostSerializer(serializers.ModelSerializer):
    files = PostFileSerializer(
        many=True, required=False, allow_null=True, default=[])

    class Meta:
        model = Post
        fields = ['id',
                  'files',
                  'author',
                  'course',
                  'text',
                  'is_pinned',
                  'created_at']

    def create(self, validated_data):
        files_data = validated_data.pop('files', None)

        post = Post.objects.create(**validated_data)
        if files_data:
            for file_data in files_data:
                PostFile.objects.create(post=post, **file_data)
        return post

    def update(self, instance, validated_data):

        instance.text = validated_data.get('text', instance.text)
        instance.text = validated_data.get('email', instance.email)
        instance.text = validated_data.get('email', instance.email)
        instance.text = validated_data.get('email', instance.email)
        instance.text = validated_data.get('email', instance.email)

        files = validated_data.pop('files')
        files_serializer = self.fields['files']
        for file in files:
            file_id = file.get('id', None)
            if file_id:
                file_obj = PostFile.objects.get(id=file_id)
                file['post'] = instance.id
                files_serializer.update(file_obj, **file)
                file_obj.save()
            else:
                PostFile.objects.create(post=instance, **file)

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
                  'title',
                  'course',
                  'description',
                  'deadline',
                  'grade' ]

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance
