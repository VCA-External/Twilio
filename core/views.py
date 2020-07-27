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


user = 'SK7bd24ca754fb718aa9ded7f12a991253'
pwd = 'C4eIpMfgmlhtXUT87JvFP0BhaZ3WcgnM'


class CreateRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "MaxParticipants": 4,
            "Type": "group-small"
        }
        if (request.data):
            payload["UniqueName"] = request.data.get('roomUniqueName')
            if(request.data.get('maxParticipants') or 0 != 4):
                if(request.data.get('maxParticipants') or 0 > 4):
                    payload["Type"] = "group"
                payload["MaxParticipants"] = request.data.get(
                    'maxParticipants')
            if(request.data.get("RecordParticipantConnect")):
                payload["RecordParticipantsOnConnect"] = request.data.get(
                    "RecordParticipantConnect")

        call = req.post('https://video.twilio.com/v1/Rooms/', auth=HTTPBasicAuth(
            user, pwd), headers=head, data=payload)

        return Response(call.json())
