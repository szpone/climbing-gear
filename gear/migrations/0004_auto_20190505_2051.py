# Generated by Django 2.2.1 on 2019-05-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("gear", "0003_auto_20190505_2043")]

    operations = [
        migrations.AlterField(
            model_name="gear",
            name="image",
            field=models.ManyToManyField(blank=True, to="gear.Image"),
        )
    ]
