from django.urls import path
from .views import ChallengeListView, ChallengeCreateView

urlpatterns = [
    path("", ChallengeListView.as_view(), name="challenge-list"),
    path("create/", ChallengeCreateView.as_view(), name="challenge-create"),
]