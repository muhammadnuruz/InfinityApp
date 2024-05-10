from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.groups.serializers import GroupsSerializer, GroupsRetrieveSerializer
from apps.groups.models import Groups


class GroupsListView(ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [AllowAny]


class GroupsDetailView(RetrieveAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsRetrieveSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        students = instance.get_students()
        students_ids = students.values_list('id', flat=True)
        return Response({
            'group': serializer.data,
            'students_id': students_ids
        })
