from django.urls import reverse
from django.utils.safestring import mark_safe

from cotidia.actionable.utils import count_uncomplete_actions

def admin_menu(context):
    count = count_uncomplete_actions()

    if count > 99:
        count = "99+"

    if count:
        label = 'Actionable Items <span class="label label--primary">{}</span>'.format(count)
    else:
        label = 'Actionable Items'
    return [
        {
            "text": mark_safe(label),
            "icon": "tasks",
            "url": reverse("actionable-admin:actionable-list"),
            "permissions": ["actionable.add_actionable", "actionable.change_actionable"],
        }
    ]
