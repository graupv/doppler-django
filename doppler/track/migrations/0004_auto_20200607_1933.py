# Generated by Django 3.0.7 on 2020-06-08 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_auto_20200605_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_id',
            field=models.CharField(max_length=35, primary_key=True, serialize=False),
        ),
    ]
