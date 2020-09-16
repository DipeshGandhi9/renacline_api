from django.contrib.auth import get_user_model
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer
from consultancy.serializers import ProfileSerializer
from drf_yasg.utils import swagger_auto_schema
# from.utils import Encryption

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

# @swagger_auto_schema(methods=[ 'post'], request_body=ProfileSerializer)
# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])
# def registration(request):
#     user_data = request.data['owner']
#     serializer = UserCreateSerializer(data=user_data)
#     if not serializer.is_valid():
#         return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#     user = serializer.save()
#     profile_data = request.data
#     profile_data.pop('owner')
#     profile_data['owner'] = UserCreateSerializer(user).data
#     profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#     if not profile_serializer.is_valid():
#         return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#     profile = profile_serializer.save()
#     refresh = RefreshToken.for_user(profile.owner)
#     res = {
#         "refresh": str(refresh),
#         "access": str(refresh.access_token),
#     }
#     return response.Response(res, status.HTTP_201_CREATED)

# @swagger_auto_schema(methods=['post'], request_body=UserCreateSerializer)
# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.IsAuthenticated])
# def getlogin(request):
#     if not request.data:
#         return response.Response({'error': "Please provide username/password"}, status="400")
#     # user_data = request.data
#     username = request.data['username']
#     password = request.data['password']
#     print('username ', username)
#     print('password ', password)
#     u = User.set_password()
#     try:
#         user = User.objects.get(username=username, password=password)
#
#     except User.DoesNotExist:
#         return response.Response({'error': "Invalid username/password"}, status="400")
#     if user:
#         password_str = user.password
#         print('db username ', user.username)
#         print('db password ', password_str)
#         # encryption = Encryption()
#         # encrypted_pass = encryption.do_encrypted_str(password_str)
#         # print(encrypted_pass)
#         if not password == password_str:
#             return response.Response({'error': "Invalid username/password"}, status="400")
#     else:
#         return response.Response({'error': "Invalid username/password"}, status="400")
#
#     user_data = UserCreateSerializer(user).data
#     refresh = RefreshToken.for_user(user)
#     res = {
#         "refresh": str(refresh),
#         "access": str(refresh.access_token),
#     }
#     user_data['token'] = res
#     return response.Response(user_data, status.HTTP_200_OK)
#


@swagger_auto_schema(methods=['post'], request_body=UserCreateSerializer)
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    print("registration")
    user_data = request.data
    # Create User
    serializer = UserCreateSerializer(data=user_data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()

    # Create Profile
    profile_data = request.data
    if not profile_data['name']:
        profile_data['name'] = user_data['first_name'] + ' ' + user_data['last_name']

    # profile_data.pop('owner')
    profile_data['owner'] = UserCreateSerializer(user).data
    profile_data['main'] = True
    profile_serializer = ProfileSerializer(data=profile_data, partial=True)
    if not profile_serializer.is_valid():
        return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
    profile = profile_serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)
