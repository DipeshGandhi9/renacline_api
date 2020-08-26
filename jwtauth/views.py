from django.contrib.auth import get_user_model
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer
from consultancy.serializers import ProfileSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
User = get_user_model()

# @swagger_auto_schema(methods=[ 'post'], request_body=ProfileSerializer)
# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])
# def registration(request):
#     # user_data = request.data['owner']
#     # serializer = UserCreateSerializer(data=user_data)
#     # if not serializer.is_valid():
#     #     return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#     # user = serializer.save()
#     # profile_data = request.data
#     # print(profile_data)
#     # profile_data['owner'] = UserCreateSerializer(user).data
#     profile_serializer = ProfileSerializer(data=request.data)
#     if not profile_serializer.is_valid():
#         return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#     profile = profile_serializer.save()
#     # profile.owner_set(user)
#     # profile.save()
#     refresh = RefreshToken.for_user(profile.owner)
#     res = {
#         "refresh": str(refresh),
#         "access": str(refresh.access_token),
#     }
#     return response.Response(res, status.HTTP_201_CREATED)

@swagger_auto_schema(methods=[ 'post'], request_body=ProfileSerializer)
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    user_data = request.data['owner']
    serializer = UserCreateSerializer(data=user_data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    profile_data = request.data
    profile_data.pop('owner')
    profile_data['owner'] = UserCreateSerializer(user).data
    profile_serializer = ProfileSerializer(data=profile_data, partial=True)
    if not profile_serializer.is_valid():
        return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
    profile = profile_serializer.save()
    refresh = RefreshToken.for_user(profile.owner)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)