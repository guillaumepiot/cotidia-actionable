# Generated by Django 2.0.2 on 2018-10-26 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actionable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actionable',
            old_name='data',
            new_name='debug_data',
        ),
        migrations.RenameField(
            model_name='actionable',
            old_name='title',
            new_name='message',
        ),
    ]
