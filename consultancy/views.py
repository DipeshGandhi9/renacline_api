from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.exceptions import PermissionDenied

from .models import Profile
from .serializers import ProfileSerializer

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_superuser


class ListProfileView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwner,)

    # Ensure a user sees only own Profile objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Profile.objects.all()
            return Profile.objects.filter(owner=user)
        raise PermissionDenied()

    # Set user as owner of a Profile object.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class LoginView(generics.CreateAPIView):
#     """
#     POST auth/login/
#     """
#     # This permission class will overide the global permission
#     # class setting
#     permission_classes = (permissions.AllowAny,)
#
#     queryset = User.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         username = request.data.get("username", "")
#         password = request.data.get("password", "")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             # login saves the user’s ID in the session,
#             # using Django’s session framework.
#             login(request, user)
#             serializer = TokenSerializer(data={
#                 # using drf jwt utility functions to generate a token
#                 "token": jwt_encode_handler(
#                     jwt_payload_handler(user)
#                 )})
#             serializer.is_valid()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
