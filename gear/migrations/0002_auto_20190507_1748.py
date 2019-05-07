# Generated by Django 2.2.1 on 2019-05-07 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gear', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='climber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gear',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gear.Brand'),
        ),
        migrations.AddField(
            model_name='gear',
            name='gear_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gear.GearType'),
        ),
        migrations.AddField(
            model_name='gear',
            name='model_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gear.Make'),
        ),
    ]
