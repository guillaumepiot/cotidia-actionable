import json
import logging

class ActionableHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def emit(self, record):
        # Has to be imported here as it is instantiated before apps are registered
        from cotidia.actionable.models import Actionable
        message = self.format(record)
        actionable = Actionable(message=message)
        if hasattr(record, "additional_data"):
            actionable.debug_data = json.dumps(record.additional_data)
        if hasattr(record, "link"):
            actionable.link = record.link

        actionable.save()
