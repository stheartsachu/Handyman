# Generated by Django 3.0.8 on 2020-07-26 18:17

import buisnessuser.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buisnessuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional_user',
            name='account_creation',
            field=buisnessuser.models.CustomDateTimeField(auto_now_add=True),
        ),
    ]
