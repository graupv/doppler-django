# Generated by Django 3.0.7 on 2020-06-08 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versions', '0003_auto_20200607_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versions',
            name='modify_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]