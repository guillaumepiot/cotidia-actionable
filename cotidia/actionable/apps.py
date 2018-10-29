import logging

from django.apps import AppConfig

from cotidia.actionable.log import ActionableHandler

class ActionableConfig(AppConfig):
    name = "cotidia.actionable"
    label = "actionable"

    def ready(self):
        actionable_logger = logging.getLogger('actionable')
        handler = ActionableHandler()
        actionable_logger.addHandler(handler)
