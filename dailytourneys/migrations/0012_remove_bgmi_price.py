# Generated by Django 3.2.13 on 2022-07-30 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailytourneys', '0011_bgmi_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bgmi',
            name='price',
        ),
    ]
