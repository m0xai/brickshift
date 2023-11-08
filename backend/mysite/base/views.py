from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(username=request.data['username'])
            return Response({'token': response.data['token'], 'user_id': user.id})
        return Response(response.data, status=response.status_code)