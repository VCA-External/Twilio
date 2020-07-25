from rest_framework import generics, authentication, permissions, status
from core.serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.views import APIView
import requests as req
from requests.auth import HTTPBasicAuth



class CreateUserView(generics.CreateAPIView):

    # Create a new user in the system
    serializer_class = UserSerializer

    # Create a new auth token for user

class CreateTokenView(ObtainAuthToken):
    serializer_class = UserLoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



user = 'SK9055c301c395a98a68a8622eb2a5304d'
pwd = '4O0rYpjWcd2IKkVncSS7yBaYxutQAnmh'


class CreateRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        if (request.data.get('roomUniqueName')):
            unique = request.data.get('roomUniqueName')
            if(request.data.get('maxParticipants')):
                maxPart = request.data.get('maxParticipants')
                if maxPart > 4:
                    call = req.post("https://video.twilio.com/v1/Rooms/", auth=HTTPBasicAuth(
                        user, pwd), data={'UniqueName': unique, "Type": 'group', 'MaxParticipants': maxPart}, headers=head)
                    
                    print(call)
                    return Response(call)

                call = req.post("https://video.twilio.com/v1/Rooms/", auth=HTTPBasicAuth(
                    user, pwd), data={'UniqueName': unique, "Type": 'peer-to-peer', 'MaxParticipants': maxPart}, headers=head)
                print(call)
                return Response(call)

            call = req.post("https://video.twilio.com/v1/Rooms/", auth=HTTPBasicAuth(
                user, pwd), data={'UniqueName': unique, "Type": 'peer-to-peer', 'MaxParticipants': 4}, headers=head)
            print(call)
            return Response(call)

        
