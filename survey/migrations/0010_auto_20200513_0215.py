# Generated by Django 3.0.5 on 2020-05-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_wineitem_wine_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wineitem',
            name='label_type',
            field=models.CharField(blank=True, choices=[('TR', 'Traditional'), ('WH', 'Whimsical'), ('MO', 'Modern'), ('MI', 'Minimalist')], max_length=2, null=True),
        ),
    ]
