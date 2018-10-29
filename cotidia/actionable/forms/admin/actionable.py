from django import forms
from betterforms.forms import BetterModelForm

from cotidia.admin.widgets import TrixEditor
from cotidia.actionable.models import Actionable


class ActionableAddForm(BetterModelForm):
    class Meta:
        model = Actionable
        exclude = ['level','message','link','debug_data','created_at', 'updated_at', 'order_id']
        fieldsets = (
            ('info', {
                'fields': (
                    'status',
                ),
                'legend': 'Actionable details'
            }),
        )


class ActionableUpdateForm(ActionableAddForm):
    class Meta:
        model = Actionable
        exclude = ['level','message','link','debug_data','created_at', 'updated_at', 'order_id']
        fieldsets = (
            ('info', {
                'fields': (
                    'status',
                ),
                'legend': 'Actionable details'
            }),
        )
