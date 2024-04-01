from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns=[
    path('register',views.SignupView.as_view()),
    path('token',ObtainAuthToken.as_view()),
]