from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('user/registration/', views.registration_view.as_view()),
    path('user/login/', views.Login.as_view()),
]
