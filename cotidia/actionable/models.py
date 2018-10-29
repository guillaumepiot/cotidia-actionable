from django.db import models

from cotidia.core.models import BaseModel
from cotidia.admin.models import AbstractOrderable

status_choices = (
    ('NEW','NEW'),
    ('SOLVED','SOLVED'),
    ('IGNORED','IGNORED'),
)
log_level_choices = (
    ('INFO', 'INFO'),
    ('WARNING', 'WARNING'),
    ('ERROR', 'ERROR'),
)

class Actionable(BaseModel):
    message = models.CharField(max_length=250, blank=True)
    link = models.URLField("Link", max_length=200, blank=True)
    debug_data = models.TextField(blank=True)
    status = models.CharField(max_length=20, default="NEW", choices=status_choices)
    level = models.CharField(max_length=20, default="WARNING", choices=log_level_choices)

    class Meta:
        verbose_name = 'Actionable'
        verbose_name_plural = 'Actionables'

    def __str__(self):
        return self.message
