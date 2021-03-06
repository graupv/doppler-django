# Generated by Django 3.0.4 on 2020-06-05 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Versions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField()),
                ('key', models.CharField(max_length=2, null=True, verbose_name='track_key')),
                ('name', models.CharField(max_length=200, verbose_name='track_name')),
                ('lyrics', models.CharField(max_length=6000, null=True, verbose_name='track_lyrics')),
                ('modify_date', models.DateTimeField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('track_id', models.ForeignKey(max_length=32, null=True, on_delete=django.db.models.deletion.SET_NULL, to='track.Track')),
            ],
        ),
        migrations.AddConstraint(
            model_name='versions',
            constraint=models.UniqueConstraint(fields=('track_id', 'version'), name='unique_track_id_version'),
        ),
    ]
