from django.http import Http404
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from dandiapi.api.girder import GirderClient
from dandiapi.api.models import Dandiset
from dandiapi.api.views.common import DandiPagination


class DandisetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dandiset
        fields = [
            'identifier',
            'uuid',
            'metadata',
            'created',
            'modified',
        ]
        read_only_fields = ['created']


class DandisetViewSet(ModelViewSet):
    queryset = Dandiset.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DandisetSerializer
    pagination_class = DandiPagination

    lookup_value_regex = Dandiset.IDENTIFIER_REGEX
    # This is to maintain consistency with the auto-generated names shown in swagger.
    lookup_url_kwarg = 'identifier'

    @action(detail=False, methods=['POST'], serializer_class=None)
    def sync(self, request):
        if 'folder-id' not in request.query_params:
            raise ValidationError('Missing query parameter "folder-id"')
        draft_folder_id = request.query_params['folder-id']

        with GirderClient() as client:
            Dandiset.from_girder(draft_folder_id, client)
        return Response('', status=status.HTTP_202_ACCEPTED)
