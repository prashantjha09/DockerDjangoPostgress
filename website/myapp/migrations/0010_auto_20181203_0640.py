# Generated by Django 2.1.3 on 2018-12-03 06:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20181203_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 3, 6, 40, 48, 690402, tzinfo=utc)),
        ),
    ]
