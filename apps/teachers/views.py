from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.teachers.models import Teachers
from apps.teachers.serializers import TeachersRetrieveSerializer


class TeachersDetailView(RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersRetrieveSerializer
    permission_classes = [AllowAny]
