from rest_framework import serializers
from edubox.base.models import *

class PostFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostFile
        fields = [  'id',
                    'post',
                    'file_path',]

    def create(self, validated_data):
        post = validated_data.pop('post')
        instance = Post.objects.get(id=post)
        return PostFile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.file_path  = validated_data.get('file_path', instance.file_path)
        instance.save()
        return instance

    

class PostSerializer(serializers.ModelSerializer):
    files = PostFileSerializer(many=True)

    class Meta:
        model = Post
        fields = [  'id',
                    'files',
                    'author',
                    'course',
                    'text',
                    'assignment',
                    'is_pinned'
                    'date']

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        post = Post.objects.create(**validated_data)
        for file_data in files_data:
            PostFile.objects.create(post=post, **file_data)
        return post

    def update(self, instance, validated_data):

        instance.text  = validated_data.get('text', instance.text)
        instance.text  = validated_data.get('email', instance.email)
        instance.text  = validated_data.get('email', instance.email)
        instance.text  = validated_data.get('email', instance.email)
        instance.text  = validated_data.get('email', instance.email)

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
