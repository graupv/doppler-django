# Generated by Django 3.0.7 on 2020-06-08 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_auto_20200607_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
