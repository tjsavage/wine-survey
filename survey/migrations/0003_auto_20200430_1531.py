# Generated by Django 3.0.5 on 2020-04-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200430_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wineitem',
            name='country',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='wineitem',
            name='item_key',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wineitem',
            name='name',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='wineitem',
            name='origin',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='wineitem',
            name='region',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='wineitem',
            name='varietal',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='wineitem',
            name='winc_product_code',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='wineitem',
            name='winc_product_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
