from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('user/registration/', views.registration_view.as_view()),
    path('nursery/registration/', views.Nurseryregistration_view.as_view()),
    path('user/login/', views.Login.as_view()),
    path('user/plantlist/', views.PlantList.as_view()),
    path('nursery/addplant/', views.AddPlant.as_view()),
    path('nursery/getplant/', views.NurseryPlantList.as_view()),
]
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA5NTczMDkyLCJqdGkiOiIzNjMwMDgyY2ZlM2Q0MjQ2YTU5NzA3ZGQ1NzMyNGZjOSIsInVzZXJfaWQiOjV9.A5wzABHC_1UZuL7IW5RAzx4bQSQOBp3BwpUaKZS72Lk
