from rest_framework import viewsets, permissions
from .models import UserData
from .serializers import UserSerializer

# register our view to add logic

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # to enable no serious authentication
