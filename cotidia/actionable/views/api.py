from uuid import UUID

from rest_framework.views import APIView
from rest_framework.response import Response

from cotidia.actionable.models import Actionable

class UpdateActionableStatusView(APIView):
    def post(self, request, *args, **kwargs):
        uuids = self.request.data.getlist('uuids')
        valid_uuids = []
        for uuid in uuids:
            try:
                valid_uuids.append(UUID(uuid))
            except ValueError:
                pass

        Actionable.objects.filter(uuid__in=valid_uuids).update(
            status=self.kwargs.get('status')
        )
        return Response()