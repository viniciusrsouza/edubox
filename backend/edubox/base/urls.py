from django.urls import path

from edubox.base import views

urlpatterns = [

    path("courses/", view=views.CourseListCreate.as_view()),

    path("courses/<int:pk>/", view=views.CourseDetail.as_view()),

    path("courses/<int:course>/posts/$", view=views.PostsListCreate.as_view()),

    path("courses/<int:course>/posts/<int:pk>",
         view=views.PostsRetrieve.as_view()),

    path("courses/<int:course_pk>/assignments/",
         view=views.AssignmentListCreate.as_view()),

    path("courses/<int:course_pk>/assignments/<int:pk>/",
         view=views.AssignmentDetail.as_view()),

    path("membership/<str:token>", view=views.MembershipCreate.as_view()),

    path("membership/<int:user>/<int:course>/<int:role>",
         view=views.MembershipCreate.as_view()),

    path("memberlist/<int:pk>", view=views.MemberList.as_view()),
]
