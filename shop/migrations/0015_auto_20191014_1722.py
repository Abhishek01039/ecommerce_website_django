# Generated by Django 2.1.7 on 2019-10-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
