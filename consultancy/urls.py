from django.urls import path, re_path
# from .views import ListProfileView, add_profile, update_profile, ProfileListView, ProfileDetailsView
# from .views import ProfileListView, ProfileDetailsView
from .views import ProfileViewSet, QuestionViewSet, AnswerViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'answer/(?P<qid>\d+)', AnswerViewSet, basename='answer')
# router.register(r'accounts', AccountViewSet)

urlpatterns = [
    # path('profiles/', add_profile, name="profile-add"),
    # re_path(r'^profile/$', ProfileView.as_view(), name='profile'),
    # re_path(r'^profile/$', ProfileListView.as_view(), name='profile'),
    # re_path(r'^profile/<int:pk>/$', ProfileDetailsView.as_view(), name='profile-details'),
    # path('profile/', ProfileViewSet, name='profile'),
    # re_path(r'^profile/<int:id>/$', ProfileDetailsView.as_view(), name='profile-details'),
    # path('profiles/', ListProfileView.as_view(), name="profile-all"),
    # path('profiles/<int:profile_id>', update_profile, name="profile-update"),
]

urlpatterns = router.urls
