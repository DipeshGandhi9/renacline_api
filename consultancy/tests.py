# import json
# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.views import status
# from .models import Profile
# from .serializers import ProfileSerializer
# from django.contrib.auth.models import User
#
# # Create your tests here.
# # tests for views
#
#
# class BaseViewTest(APITestCase):
#     client = APIClient()
#
#     @staticmethod
#     def create_profile(name="", father_name="", birth_date="", birth_place="", district=""):
#         if name != "" and father_name != "":
#             Profile.objects.create(name=name, father_name=father_name, birth_date=birth_date, birth_place=birth_place,
#                                    district=district)
#
#     def login_a_user(self, username="", password=""):
#         url = reverse(
#             "auth-login",
#             kwargs={
#                 "version": "v1"
#             }
#         )
#         return self.client.post(
#             url,
#             data=json.dumps({
#                 "username": username,
#                 "password": password
#             }),
#             content_type="application/json"
#         )
#
#     def login_client(self, username="", password=""):
#         # get a token from DRF
#         response = self.client.post(
#             reverse('create-token'),
#             data=json.dumps(
#                 {
#                     'username': username,
#                     'password': password
#                 }
#             ),
#             content_type='application/json'
#         )
#         self.token = response.data['token']
#         # set the token in the header
#         self.client.credentials(
#             HTTP_AUTHORIZATION='Bearer ' + self.token
#         )
#         self.client.login(username=username, password=password)
#         return self.token
#
#
#     def setUp(self):
#         # create a admin user
#         self.user = User.objects.create_superuser(
#             username="test_user",
#             email="test@mail.com",
#             password="testing",
#             first_name="test",
#             last_name="user",
#         )
#         # add test data
#         self.create_profile("Dipesh ", "Kanchanlal", '', 'surat', 'surat')
#         self.create_profile("Kanchanlal", "Chandulal", '', 'surat', 'surat')
#
#
# class GetAllProfilesTest(BaseViewTest):
#
#     def test_get_all_profiles(self):
#         # this is the update you need to add to the test, login
#         self.login_client('test_user', 'testing')
#         # hit the API endpoint
#         response = self.client.get(
#             reverse("profile-all", kwargs={"version": "v1"})
#         )
#         # fetch the data from db
#         expected = Profile.objects.all()
#         serialized = ProfileSerializer(expected, many=True)
#         self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
# class AuthLoginUserTest(BaseViewTest):
#     """
#     Tests for the auth/login/ endpoint
#     """
#
#     def test_login_user_with_valid_credentials(self):
#         # test login with valid credentials
#         response = self.login_a_user("test_user", "testing")
#         # assert token key exists
#         self.assertIn("token", response.data)
#         # assert status code is 200 OK
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # test login with invalid credentials
#         response = self.login_a_user("anonymous", "pass")
#         # assert status code is 401 UNAUTHORIZED
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)