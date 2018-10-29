import django_filters

from django.db.models import Q

from cotidia.admin.views import (
    AdminListView,
    AdminDetailView,
    AdminCreateView,
    AdminUpdateView,
    AdminDeleteView,
)

from cotidia.actionable.models import Actionable
from cotidia.actionable.forms.admin.actionable import (
    ActionableAddForm,
    ActionableUpdateForm,
)


class ActionableFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label="Title",
        method="filter_title"
    )

    class Meta:
        model = Actionable
        fields = ['title', 'status']

    def filter_title(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
        )


class ActionableList(AdminListView):
    columns = (
        ('Message', 'message'),
        ('Link', 'link'),
        ('Status', 'status'),
    )
    model = Actionable
    filterset = ActionableFilter


class ActionableDetail(AdminDetailView):
    model = Actionable
    fieldsets = [
        {
            "legend": "Actionable details",
            "fields": [
                {
                    "label": "Message",
                    "field": "message",
                },
                {
                    "label": "Link",
                    "field": "link",
                },
                {
                    "label": "Debug data",
                    "field": "debug_data"
                },
                {
                    "label": "Status",
                    "field": "status",
                },
            ]
        },
    ]


class ActionableCreate(AdminCreateView):
    model = Actionable
    form_class = ActionableAddForm


class ActionableUpdate(AdminUpdateView):
    model = Actionable
    form_class = ActionableUpdateForm


class ActionableDelete(AdminDeleteView):
    model = Actionable
