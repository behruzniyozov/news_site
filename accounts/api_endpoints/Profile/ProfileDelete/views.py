from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import User

class ProfileDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'email'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()