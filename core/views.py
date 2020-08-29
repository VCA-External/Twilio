from rest_framework import generics, authentication, permissions, status
from core.serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.views import APIView
import requests as req
from requests.auth import HTTPBasicAuth
import json
def change_format_resp(b):
        d=json.loads(b)
        a={}
        a["id"]=d["sid"]
        a["roomUniqueName"]=d["unique_name"]
        a["rooomstatus"]=d["status"]
        a["maxparticipants"]=d["max_participants"]
        a["type"]=d["type"]
        a["startDt"]=None
        a["endDt"]=None
        a["duration"]=0
        a["createdDt"]=d["date_created"]
        a["modifiedDt"]=d["date_updated"]
        a["participants"]=[]
        return json.dumps(a)


class CreateUserView(generics.CreateAPIView):

    # Create a new user in the system
    serializer_class = UserSerializer

    # Create a new auth token for user

#
# class RoomView(viewsets.GenericViewSet):
#     serializer_class = RoomSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = UserLoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


user = 'SK20841af8008834611f84e7590630f467'
pwd = 'oRob0tiWhYPm9gLQChE9FxX1vViOsI2U'


class CreateRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,uniquename):
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "MaxParticipants": 4,
            "Type": "group-small"
        }  # dict type
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
    
    def get(self,request,uniquename):
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        call = req.get('https://video.twilio.com/v1/Rooms/'+uniquename, auth=HTTPBasicAuth(
            user, pwd),)
        return Response(call.json())


class DeleteRoom(APIView):
    def delete(self, request, uniquename):
        call = req.delete('https://video.twilio.com/v1/Rooms/'+uniquename)
        return Response(call.json())


class CompleteRoom(APIView):
    permission_classes = (IsAuthenticated,)
    

    def get(self, request, roomUniqueName):
          # only one field what is it?
        

        head = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "Status": "completed"
        }
        call = req.post("https://video.twilio.com/v1/Rooms/"
                        + roomUniqueName, data=payload, auth=HTTPBasicAuth(
                            user, pwd))
        return Response(change_format_resp(call.json()))
