# Generated by Django 3.0.5 on 2020-05-06 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20200506_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyabtestinstance',
            old_name='timestamp',
            new_name='created',
        ),
    ]
