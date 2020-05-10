from django.urls import path

from edubox.base import views

urlpatterns = [

    
    path("test/", view=views.Test.as_view()),

    path("posts/", view=views.PostsListCreate.as_view()),

    path("posts/<int:id>", view=views.PostDetail.as_view()),

]
