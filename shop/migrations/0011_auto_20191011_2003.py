# Generated by Django 2.1.7 on 2019-10-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20191011_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(default='', max_length=6),
        ),
    ]
