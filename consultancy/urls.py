from django.urls import path
from .views import ListProfileView


urlpatterns = [
    path('profiles/', ListProfileView.as_view(), name="profile-all"),
]
