from rest_framework.generics import RetrieveAPIView, get_object_or_404, UpdateAPIView
from rest_framework.permissions import AllowAny

from apps.students.models import Students
from apps.students.serializers import StudentsRetrieveSerializer, StudentsUpdateSerializer


class StudentsDetailView(RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsRetrieveSerializer
    permission_classes = [AllowAny]


class StudentsChatIdDetailView(RetrieveAPIView):
    serializer_class = StudentsRetrieveSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        chat_id = self.kwargs.get('chat_id')
        return get_object_or_404(Students, chat_id=chat_id)


class StudentsPhoneNumberDetailView(RetrieveAPIView):
    serializer_class = StudentsRetrieveSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        phone_number = self.kwargs.get('phone_number')
        return get_object_or_404(Students, phone_number=phone_number)


class StudentsUpdateView(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsUpdateSerializer
    permission_classes = [AllowAny]
