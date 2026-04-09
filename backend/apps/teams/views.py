from rest_framework import generics, permissions
from .models import Team
from .serializers import TeamSerializer


class TeamListView(generics.ListAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        challenge_id = self.kwargs.get("challenge_id")
        return Team.objects.filter(challenge_id=challenge_id).order_by("-created_at")


class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminUser]