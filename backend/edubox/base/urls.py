from django.urls import path

from edubox.base import views

urlpatterns = [


    path("test/", view=views.Test.as_view()),

    path("test2/", view=views.Test2.as_view()),

    path("test3/<int:pk>/", view=views.Test3.as_view()),

    path("posts/", view=views.PostsListCreate.as_view()),

    path("posts/<int:course>/", view=views.PostsList.as_view()),

    path("courses/", view=views.CourseListCreate.as_view()),

    path("courses/<int:pk>/", view=views.CourseDetail.as_view()),

    path("courses/<int:course_pk>/assignments/",
         view=views.AssignmentListCreate.as_view()),

    path("courses/<int:course_pk>/assignments/<int:pk>/",
         view=views.AssignmentDetail.as_view()),

    path("membership/<str:token>", view=views.MembershipCreate.as_view()),

    path("membership/<int:user>/<int:course>/<int:role>", view=views.MembershipCreate.as_view()),

    path("memberlist/<int:pk>", view=views.MemberList.as_view()),
]
