from django.contrib.auth.models import Group, Permission, User
from rest_framework import permissions, viewsets

from core.models import Psycologist
from core.serializers import GroupSerializer, PsycologistSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PsycologistViewSet(viewsets.ModelViewSet):
    queryset = Psycologist.objects.all()
    serializer_class = PsycologistSerializer
