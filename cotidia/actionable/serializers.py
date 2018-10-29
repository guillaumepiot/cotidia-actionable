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
            'message',
            'level',
            'link',
            'status',
        ]
        model = Actionable

    class SearchProvider:
        filters = ['level', 'status']
        field_representation = {
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
        sidebar_filters = [
            'status',
            'level'
        ]
        default_columns = ['level', 'message', 'link', 'status']