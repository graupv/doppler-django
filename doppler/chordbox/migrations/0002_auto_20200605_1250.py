# Generated by Django 3.0.4 on 2020-06-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chordbox', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chordbox',
            name='owner',
        ),
        migrations.AddField(
            model_name='chordbox',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
