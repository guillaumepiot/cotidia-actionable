from django.urls import reverse_lazy

from rest_framework import serializers

from cotidia.admin.serializers import BaseDynamicListSerializer
from cotidia.admin import filters as admin_filters
from cotidia.actionable.models import (
    Actionable, status_choices, log_level_choices
)

class ActionableDynamicListSerializer(BaseDynamicListSerializer):
    status = serializers.ChoiceField(choices=status_choices)
    level = serializers.ChoiceField(choices=log_level_choices)
    class Meta:
        fields = [
            'uuid',
            'id',
            'created_at',
            'message',
            'level',
            'link',
            'status',
        ]
        model = Actionable

    class SearchProvider:
        filters = ['created_at', 'level', 'status']
        field_representation = {
            "created_at": {
                "label": "Date"
            },
            "link": {
                "display": "link"
            },
            "level": {
                "display": "function",
                "function_template": "admin/actionable/actionable/js/log_level.js"
            },
            "status": {
                "display": "function",
                "function_template": "admin/actionable/actionable/js/status.js"
            }

        }
        override_filters = {
            'status': admin_filters.ChoiceFilter(
                field_name='status',
                label='Status',
                options=[{"value":c[1],"label":c[0]} for c in status_choices],
            ),
            'level': admin_filters.ChoiceFilter(
                field_name='level',
                label='Log level',
                options=[{"value":c[1],"label":c[0]} for c in log_level_choices],
            ),
        }
        batch_actions = [
            {
                'action': 'mark-resolved',
                'label': 'Mark solved',
                'endpoint': reverse_lazy('actionable-api:actionable-mark-solved')
            },
            {
                'action': 'mark-ignored',
                'label': 'Ignore',
                'endpoint': reverse_lazy('actionable-api:actionable-mark-ignored')
            },
            {
                'action': 'mark-new',
                'label': 'Mark New',
                'endpoint': reverse_lazy('actionable-api:actionable-mark-new')
            },
        ]
        enable_detail_url = False
        sidebar_filters = [
            'status',
            'level'
        ]
        default_columns = ['created_at','level', 'message', 'link', 'status']