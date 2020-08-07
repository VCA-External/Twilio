from django.urls import path, include
from core import views
from rest_framework_simplejwt import views as jwt_views

app_name = 'core'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('rooms/CreateRoom/', views.CreateRoomView.as_view(), name='room'),
    path('rooms/deleteRoom/<uniquename>/',
         views.DeleteRoom.as_view(), name="deleteRoom"),
    path('rooms/CompleteRoom/<roomUniqueName>/',
         views.CompleteRoom.as_view(), name="CompleteRoom"),
    # path('room/beta/', views.RoomSerializer.as_view(), name='beta')
]
