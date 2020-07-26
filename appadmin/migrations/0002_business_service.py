# Generated by Django 3.0.8 on 2020-07-26 06:08

import appadmin.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business_Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('service_level', models.CharField(choices=[('SIMPLE', 'Simple'), ('PREMIUM', 'Premium\n(Extra Care)')], default='SIMPLE', max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('people_involve_in_service', models.IntegerField(default=0)),
                ('service_creation', appadmin.models.CustomDateTimeField(auto_now_add=True)),
                ('Business_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appadmin.Business_category')),
            ],
        ),
    ]