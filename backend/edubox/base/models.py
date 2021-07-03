from django.db import models
from edubox.users.models import User


class Assignment(models.Model):
    deadline = models.DateTimeField(blank=True, null=True)


class Submission(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('base.Post', on_delete=models.CASCADE, null=True)
    file_path = models.FileField(
        upload_to='submissionFile/', blank=True, null=True)
    grade = models.FloatField()

    class Meta:
        unique_together = ('user', 'post')


'''
class GradedAssignment(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    assignment = models.ForeignKey(
        'base.Assignment', on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()

    def __str__(self):
        return self.student.username
'''


class Choice(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField('base.Choice')
    answer = models.ForeignKey(
        'base.Choice', on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey(
        'base.Assignment', on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    timeopen = models.IntegerField(default=0)
    timeclose = models.IntegerField(default=0)
    timelimit = models.IntegerField(default=0)
    attempts = models.IntegerField(default=1)


class Course(models.Model):
    owner = models.ForeignKey(
        'users.User', related_name='owner', on_delete=models.CASCADE)
    code = models.CharField(max_length=8, unique=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.title


class Membership(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    course = models.ForeignKey('base.Course', on_delete=models.CASCADE)
    role = models.IntegerField()
    favorite = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'course')


class PostFile(models.Model):
    post = models.ForeignKey('base.Post', on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='uploads/')


class Post(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(
        'base.Course', on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=10000, blank=True, null=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    assignment = models.ForeignKey('base.Assignment',
                                   blank=True,
                                   null=True,
                                   on_delete=models.DO_NOTHING)
