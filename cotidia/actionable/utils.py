from cotidia.actionable.models import Actionable

def count_uncomplete_actions(statuses=["NEW"]):
    return Actionable.objects.filter(status__in=statuses).count()