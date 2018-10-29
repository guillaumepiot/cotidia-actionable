from django.urls import path

from cotidia.admin.views.api import DynamicListAPIView

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
    )
]