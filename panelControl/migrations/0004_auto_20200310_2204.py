# Generated by Django 3.0.3 on 2020-03-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panelControl', '0003_auto_20200310_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='telefono',
            field=models.IntegerField(verbose_name=10),
        ),
    ]
