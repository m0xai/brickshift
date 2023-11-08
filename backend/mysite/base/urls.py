from django.urls import path
from .views import UserRegistrationView, CustomObtainAuthToken

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register_user'),
    path('api/login/', CustomObtainAuthToken.as_view(), name='login'),
    # TODO: Use just a function for deleting the token
    path('api/logout/', CustomObtainAuthToken.as_view(), name='login'),
]
