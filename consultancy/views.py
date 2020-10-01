from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import response, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from .serializers import UserCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from datetime import datetime

from .models import Profile, Question
from .serializers import ProfileSerializer, QuestionSerializer

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_superuser


# class ListProfileView(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsOwner,)
#
#     # Ensure a user sees only own Profile objects.
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_authenticated:
#             if user.is_superuser:
#                 return Profile.objects.all()
#             return Profile.objects.filter(owner=user)
#         raise PermissionDenied()
#
#     # Set user as owner of a Profile object.
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# @swagger_auto_schema(methods=['post'], request_body=ProfileSerializer)
# @api_view(["POST"])
# @permission_classes([permissions.IsAuthenticated])
# def add_profile(request):
#     # payload = json.loads(request.body)
#     # user = request.user
#     # try:
#     #     author = Author.objects.get(id=payload["author"])
#     #     book = Book.objects.create(
#     #         title=payload["title"],
#     #         description=payload["description"],
#     #         added_by=user,
#     #         author=author
#     #     )
#     #     serializer = BookSerializer(book)
#     #     return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
#     # except ObjectDoesNotExist as e:
#     #     return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#     # except Exception:
#     #     return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     profile_data = request.data
#     profile_data['owner'] = UserCreateSerializer(request.user).data
#     profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#     if not profile_serializer.is_valid():
#         return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#     profile = profile_serializer.save()
#     response.Response(profile_serializer.data, status.HTTP_201_CREATED)
#
# @swagger_auto_schema(methods=['put'], request_body=ProfileSerializer)
# @api_view(["PUT"])
# @permission_classes([permissions.IsAuthenticated])
# def update_profile(request, profile_id):
#     profile_data = request.data
#     profile_data['owner'] = UserCreateSerializer(request.user).data
#     profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#     if not profile_serializer.is_valid():
#         return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#     profile = profile_serializer.save()
#     response.Response(profile_serializer.data, status.HTTP_201_CREATED)


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

# @swagger_auto_schema(['get','post'])
# class ProfileListView(APIView):
#
#     # @swagger_auto_schema(method='get')
#     @api_view(["GET"])
#     @permission_classes([IsOwner])
#     def get(self, request):
#         user = request.user
#         if user.is_authenticated:
#             if user.is_superuser:
#                 return Profile.objects.all()
#             return Profile.objects.filter(owner=user)
#         raise PermissionDenied()
#         # queryset = Profile.objects.all()
#         # serializer_class = ProfileSerializer
#         # permission_classes = (IsOwner,)
#         # payload = json.loads(request.body)
#         # user = request.user
#         # try:
#         #     author = Author.objects.get(id=payload["author"])
#         #     book = Book.objects.create(
#         #         title=payload["title"],
#         #         description=payload["description"],
#         #         added_by=user,
#         #         author=author
#         #     )
#         #     serializer = BookSerializer(book)
#         #     return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
#         # except ObjectDoesNotExist as e:
#         #     return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#         # except Exception:
#         #     return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         # profile_data = request.data
#         # profile_data['owner'] = UserCreateSerializer(request.user).data
#         # profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#         # if not profile_serializer.is_valid():
#         #     return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#         # profile = profile_serializer.save()
#         # response.Response(profile_serializer.data, status.HTTP_201_CREATED)
#
#     # @swagger_auto_schema(method='post')
#     @api_view(["POST"])
#     @permission_classes([permissions.IsAuthenticated])
#     def post(self, request):
#         profile_data = self.request.data
#         profile_data['owner'] = UserCreateSerializer(request.user).data
#         profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#         if not profile_serializer.is_valid():
#             return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#         profile = profile_serializer.save()
#         response.Response(profile_serializer.data, status.HTTP_201_CREATED)
#
#
# class ProfileDetailsView(APIView):
#
#     # @swagger_auto_schema(method='get')
#     @api_view(["GET"])
#     @permission_classes([IsOwner])
#     def get(self, request, id):
#         user = request._request.user
#         if user.is_authenticated:
#             if user.is_superuser:
#                 return Profile.objects.all()
#             return Profile.objects.filter(owner=user)
#         raise PermissionDenied()
#         # queryset = Profile.objects.all()
#         # serializer_class = ProfileSerializer
#         # permission_classes = (IsOwner,)
#         # payload = json.loads(request.body)
#         # user = request.user
#         # try:
#         #     author = Author.objects.get(id=payload["author"])
#         #     book = Book.objects.create(
#         #         title=payload["title"],
#         #         description=payload["description"],
#         #         added_by=user,
#         #         author=author
#         #     )
#         #     serializer = BookSerializer(book)
#         #     return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
#         # except ObjectDoesNotExist as e:
#         #     return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#         # except Exception:
#         #     return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         # profile_data = request.data
#         # profile_data['owner'] = UserCreateSerializer(request.user).data
#         # profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#         # if not profile_serializer.is_valid():
#         #     return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#         # profile = profile_serializer.save()
#         # response.Response(profile_serializer.data, status.HTTP_201_CREATED)
#
#     @swagger_auto_schema(method='put', request_body=ProfileSerializer)
#     @api_view(["PUT"])
#     @permission_classes([permissions.IsAuthenticated])
#     def put(self, request, id):
#         # payload = json.loads(request.body)
#         # user = request.user
#         # try:
#         #     author = Author.objects.get(id=payload["author"])
#         #     book = Book.objects.create(
#         #         title=payload["title"],
#         #         description=payload["description"],
#         #         added_by=user,
#         #         author=author
#         #     )
#         #     serializer = BookSerializer(book)
#         #     return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
#         # except ObjectDoesNotExist as e:
#         #     return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#         # except Exception:
#         #     return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         profile_data = self.request.data
#         profile_data['owner'] = UserCreateSerializer(request.user).data
#         profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#         if not profile_serializer.is_valid():
#             return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#         profile = profile_serializer.save()
#         response.Response(profile_serializer.data, status.HTTP_201_CREATED)
#
#     # @swagger_auto_schema(method='delete')
#     @api_view(["delete"])
#     @permission_classes([permissions.IsAuthenticated])
#     def delete(self, request, id):
#         profile_data = self.request.data
#         profile_data['owner'] = UserCreateSerializer(self.request.user).data
#         profile_serializer = ProfileSerializer(data=profile_data, partial=True)
#         if not profile_serializer.is_valid():
#             return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
#         profile = profile_serializer.save()
#         response.Response(profile_serializer.data, status.HTTP_201_CREATED)

class ProfileViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        user = request.user
        if user.is_authenticated:
            queryset = Profile.objects.filter(owner=user)
            if user.is_superuser:
                queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProfileSerializer)
    def create(self, request):
        user = request.user
        # user_data = request.data
        # serializer = UserCreateSerializer(data=user_data)
        # if not serializer.is_valid():
        #     return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # user = serializer.save()
        profile_data = request.data
        profile_data.pop('owner')
        profile_data['owner'] = UserCreateSerializer(user).data
        birth_date = profile_data['birth_date']
        date_time_obj = datetime.strptime(birth_date, "%d/%m/%Y %I:%M %p")
        profile_data['birth_date'] = date_time_obj
        profile_serializer = ProfileSerializer(data=profile_data, partial=True)
        if not profile_serializer.is_valid():
            return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
        profile = profile_serializer.save()
        return response.Response(profile_serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = request.user
        queryset = None
        if user.is_authenticated:
            if user.is_superuser:
                queryset = Profile.objects.get(id=pk)
            else:
                queryset = Profile.objects.get(owner=user, id=pk)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class QuestionViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        user = request.user
        if user.is_authenticated:
            queryset = Question.objects.filter(owner=user)
            if user.is_superuser:
                queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=QuestionSerializer)
    def create(self, request):
        user = request.user
        question_data = request.data
        question_data['owner'] = UserCreateSerializer(user).data
        profile_data = question_data.pop('profile')
        if profile_data is not None:
            print("for profile 1", profile_data)

            if user.is_authenticated:
                name = profile_data['name']
                mid_name = profile_data['middle_name']
                try:
                    queryset = Profile.objects.get(owner=user, name=name, middle_name=mid_name)
                    profile_obj = ProfileSerializer(queryset, many=False)
                    date_time_obj = datetime.strptime(profile_obj.data['birth_date'], "%d/%m/%Y %I:%M %p")
                    profile_obj.data['birth_date'] = date_time_obj
                    question_data['profile'] = profile_obj.data
                except Profile.DoesNotExist:
                    profile_data['owner'] = UserCreateSerializer(user).data
                    birth_date = profile_data['birth_date']
                    date_time_obj = datetime.strptime(birth_date, "%d/%m/%Y %I:%M %p")
                    profile_data['birth_date'] = date_time_obj
                    profile_serializer = ProfileSerializer(data=profile_data, partial=True)
                    if not profile_serializer.is_valid():
                        return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
                    profile_obj = profile_serializer.save()
                    question_data['profile'] = profile_serializer.data


        else:
            print("no value")

        profile2_data = question_data.pop('profile2')
        if profile2_data is not None:
            print("profile2_data has value")
        else:
            print("profile2_data no value")

        if profile_data is not None:
            profile = question_data['profile']
            date_time_obj = datetime.strptime(profile['birth_date'], "%d/%m/%Y %I:%M %p")
            profile['birth_date'] = date_time_obj
            question_data['profile'] = profile

        question_serializer = QuestionSerializer(data=question_data, partial=True)
        if not question_serializer.is_valid():
            return response.Response(question_serializer.errors, status.HTTP_400_BAD_REQUEST)
        question = question_serializer.save()

        # user_data = request.data
        # serializer = UserCreateSerializer(data=user_data)
        # if not serializer.is_valid():
        #     return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # user = serializer.save()
        # profile_data = request.data
        # profile_data.pop('owner')
        # profile_data['owner'] = UserCreateSerializer(user).data
        # birth_date = profile_data['birth_date']
        # date_time_obj = datetime.strptime(birth_date, "%d/%m/%Y %I:%M %p")
        # profile_data['birth_date'] = date_time_obj
        # profile_serializer = ProfileSerializer(data=profile_data, partial=True)
        # if not profile_serializer.is_valid():
        #     return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
        # profile = profile_serializer.save()
        return response.Response(question_serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = request.user
        queryset = None
        if user.is_authenticated:
            if user.is_superuser:
                queryset = Question.objects.get(id=pk)
            else:
                queryset = Question.objects.get(owner=user, id=pk)
        serializer = QuestionSerializer(queryset)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
