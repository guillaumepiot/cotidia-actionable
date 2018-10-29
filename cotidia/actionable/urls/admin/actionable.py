from django.conf.urls import url, include
from django.urls import reverse_lazy

from cotidia.admin.views.generic import DynamicListView
from cotidia.actionable.views.admin.actionable import (
    ActionableList,
    ActionableCreate,
    ActionableDetail,
    ActionableUpdate,
    ActionableDelete,
)
from cotidia.actionable.serializers import ActionableDynamicListSerializer

urlpatterns = [
    url(
        r'^$',
        DynamicListView.as_view(),
        {
            'model': "actionable",
            'app_label': "actionable",
            'serializer_class': ActionableDynamicListSerializer,
            'endpoint': reverse_lazy('actionable-api:actionable-list')
        },
        name='actionable-list'
    ),
    url(
        r'^add$',
        ActionableCreate.as_view(),
        name='actionable-add'
    ),
    url(
        r'^(?P<pk>[\d]+)$',
        ActionableDetail.as_view(),
        name='actionable-detail'
    ),
    url(
        r'^(?P<pk>[\d]+)/update$',
        ActionableUpdate.as_view(),
        name='actionable-update'
    ),
    url(
        r'^(?P<pk>[\d]+)/delete$',
        ActionableDelete.as_view(),
        name='actionable-delete'
    ),
]
