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

from .models import Profile, Question, Answer
from .serializers import ProfileSerializer, QuestionSerializer, AnswerSerializer

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
                gender = profile_data['gender']
                try:
                    queryset = Profile.objects.get(owner=user, name__iexact=name)
                    profile_obj = ProfileSerializer(queryset, many=False)
                    prof_data = profile_obj.data
                    if profile_obj.data['middle_name'] == "" or profile_obj.data['birth_date'] is None or profile_obj.data['birth_place'] == "":
                        prof_data['middle_name'] = profile_data['middle_name']
                        birth_date = profile_data['birth_date']
                        date_time_obj = datetime.strptime(birth_date, "%d/%m/%Y %I:%M %p")
                        prof_data['birth_date'] = date_time_obj
                        prof_data['birth_place'] = profile_data['birth_place']
                        prof_data['district'] = profile_data['district']
                        prof_data['gender'] = gender
                        serializer = ProfileSerializer(data=prof_data, partial=True)
                        if serializer.is_valid():
                            profile_obj = serializer.update( profile_obj.instance, serializer.validated_data)
                            profile_serializer = ProfileSerializer(profile_obj)
                            prof_data = profile_serializer.data

                    date_time_obj = datetime.strptime(prof_data['birth_date'], "%d/%m/%Y %I:%M %p")
                    prof_data['birth_date'] = date_time_obj
                    question_data['profile'] = prof_data
                except Profile.DoesNotExist:
                    profile_data['owner'] = UserCreateSerializer(user).data
                    profile_data['middle_name'] = profile_data['middle_name']
                    birth_date = profile_data['birth_date']
                    date_time_obj = datetime.strptime(birth_date, "%d/%m/%Y %I:%M %p")
                    profile_data['birth_date'] = date_time_obj
                    profile_data['birth_place'] = profile_data['birth_place']
                    profile_data['district'] = profile_data['district']
                    profile_data['gender'] = gender
                    profile_serializer = ProfileSerializer(data=profile_data, partial=True)
                    if not profile_serializer.is_valid():
                        return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
                    profile_obj = profile_serializer.save()
                    profile_data = profile_serializer.data

                    date_time_obj = datetime.strptime(profile_data['birth_date'], "%d/%m/%Y %I:%M %p")
                    profile_data['birth_date'] = date_time_obj
                    question_data['profile'] = profile_data

        else:
            print("no value")

        profile2_data = question_data.pop('profile2')
        if profile2_data is not None:

            if user.is_authenticated:
                name = profile2_data['name']
                gender = profile2_data['gender']
                try:
                    queryset2 = Profile.objects.get(owner=user, name__iexact=name)
                    profile2_obj = ProfileSerializer(queryset2, many=False)
                    prof2_data = profile2_obj.data
                    if profile2_obj.data['middle_name'] == "" and profile2_obj.data['birth_date'] is None and profile2_obj.data['birth_place'] == "":
                        prof2_data['middle_name'] = profile2_data['middle_name']
                        birth_date2 = profile2_data['birth_date']
                        date_time_obj2 = datetime.strptime(birth_date2, "%d/%m/%Y %I:%M %p")
                        prof2_data['birth_date'] = date_time_obj2
                        prof2_data['birth_place'] = profile2_data['birth_place']
                        prof2_data['district'] = profile2_data['district']
                        prof2_data['gender'] = gender
                        serializer2 = ProfileSerializer(data=prof2_data, partial=True)
                        if serializer2.is_valid():
                            profile2_obj = serializer2.update(profile2_obj.instance, serializer2.validated_data)
                            profile2_serializer = ProfileSerializer(profile2_obj)
                            prof2_data = profile2_serializer.data

                    date_time_obj2 = datetime.strptime(prof2_data['birth_date'], "%d/%m/%Y %I:%M %p")
                    prof2_data['birth_date'] = date_time_obj2
                    question_data['profile2'] = prof2_data
                except Profile.DoesNotExist:
                    profile2_data['owner'] = UserCreateSerializer(user).data
                    profile2_data['middle_name'] = profile2_data['middle_name']
                    birth_date2 = profile2_data['birth_date']
                    date_time_obj2 = datetime.strptime(birth_date2, "%d/%m/%Y %I:%M %p")
                    profile2_data['birth_date'] = date_time_obj2
                    profile2_data['birth_place'] = profile2_data['birth_place']
                    profile2_data['district'] = profile2_data['district']
                    profile2_data['gender'] = gender
                    profile_serializer = ProfileSerializer(data=profile2_data, partial=True)
                    if not profile_serializer.is_valid():
                        return response.Response(profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
                    profile_obj = profile_serializer.save()
                    profile2_data = profile_serializer.data

                    date_time_obj2 = datetime.strptime(profile2_data['birth_date'], "%d/%m/%Y %I:%M %p")
                    profile2_data['birth_date'] = date_time_obj2
                    question_data['profile2'] = profile2_data

        else:
            print("profile2_data no value")

        # if profile_data is not None:
        #     profile = question_data['profile']
        #     # date_time_obj = datetime.strptime(profile['birth_date'], "%d/%m/%Y %I:%M %p")
        #     # profile['birth_date'] = date_time_obj
        #     question_data['profile'] = profile

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


class AnswerViewSet(viewsets.ViewSet):

    def list(self, request, qid):
        print("qid")
        print(qid)
        user = request.user
        queryset = None
        ans_queryset = None
        if user.is_authenticated:
            queryset = Question.objects.get(id=qid)
            if queryset is not None:
                # serializer = QuestionSerializer(queryset)
                question_owner = queryset.owner
                if user.is_superuser or user.pk == question_owner.pk:
                    try:
                        ans_queryset = Answer.objects.get(question=queryset)
                    except Answer.DoesNotExist:
                        return Response({}, status.HTTP_200_OK)

        ans_serializer = AnswerSerializer(ans_queryset, many=False)
        return Response(ans_serializer.data, status.HTTP_200_OK)

    # @swagger_auto_schema(request_body=QuestionSerializer)
    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass