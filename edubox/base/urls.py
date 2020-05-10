from django.urls import path

from edubox.base import views

urlpatterns = [

    
    path("test/", view=views.Test.as_view()),

    path("posts/", view=views.PostsListCreate.as_view()),

    path("posts/<int:pk>", view=views.PostDetail.as_view()),

    path("courses/", view=views.CourseListCreate.as_view()),

    path("courses/<int:pk>", view=views.CourseDetail.as_view()),

]
