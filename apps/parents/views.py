from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.parents.models import Parents
from apps.parents.serializers import ParentsRetrieveSerializer


class ParentsDetailView(RetrieveAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsRetrieveSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        children = instance.get_children()
        children_ids = children.values_list('id', flat=True)
        return Response({
            'parent': serializer.data,
            'children_ids': children_ids
        })
