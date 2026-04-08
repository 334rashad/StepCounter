from rest_framework import generics, permissions
from .models import Challenge
from .serializers import ChallengeSerializer


class ChallengeListView(generics.ListAPIView):
    queryset = Challenge.objects.all().order_by("-created_at")
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChallengeCreateView(generics.CreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAdminUser]