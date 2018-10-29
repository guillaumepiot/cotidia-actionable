from django.urls import path

from cotidia.admin.views.api import DynamicListAPIView
from cotidia.actionable.views.api import UpdateActionableStatusView

from cotidia.actionable.serializers import ActionableDynamicListSerializer

app_name = 'actionable'
urlpatterns = [
    path(
        'list',
        DynamicListAPIView.as_view(),
        {
            'model': "actionable",
            'app_label': "actionable",
            'serializer_class': ActionableDynamicListSerializer,
        },
        name='actionable-list'
    ),
    path(
        'mark-new',
        UpdateActionableStatusView.as_view(),
        {
            'status': 'NEW'
        },
        name='actionable-mark-new'
    ),
    path(
        'mark-solved',
        UpdateActionableStatusView.as_view(),
        {
            'status': 'SOLVED'
        },
        name='actionable-mark-solved'
    ),
    path(
        'mark-ignored',
        UpdateActionableStatusView.as_view(),
        {
            'status': 'IGNORED'
        },
        name='actionable-mark-ignored'
    ),
]