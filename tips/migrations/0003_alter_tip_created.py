# Generated by Django 4.2.7 on 2023-11-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0002_tip_active_tip_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
