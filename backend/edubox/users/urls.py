from django.urls import path

from edubox.users.views import *

app_name = "users"
urlpatterns = [

    path("create/", view=CreateAuthUserView.as_view()),
]
