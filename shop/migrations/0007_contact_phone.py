# Generated by Django 2.1.7 on 2019-09-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
