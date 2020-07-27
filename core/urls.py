from django.urls import path, include
from core import views
from rest_framework_simplejwt import views as jwt_views

app_name ='core'

urlpatterns =[
    path('create/',views.CreateUserView.as_view(), name='create'),
    path('rooms/CreateRoom/', views.CreateRoomView.as_view(),name='room'), 
]

