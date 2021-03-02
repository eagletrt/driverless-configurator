# Generated by Django 3.1.4 on 2021-03-01 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CameraModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fx', models.FloatField()),
                ('fy', models.FloatField()),
                ('cx', models.FloatField()),
                ('cy', models.FloatField()),
                ('k1', models.FloatField()),
                ('k2', models.FloatField()),
                ('p1', models.FloatField()),
                ('p2', models.FloatField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('fps', models.IntegerField()),
                ('bf', models.FloatField()),
                ('BGR_RGB', models.BooleanField(default=True)),
                ('THDepth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=500)),
                ('mission', models.CharField(choices=[('Acceleration', 'Acceleration'), ('Trackdrive', 'Trackdrive'), ('Skidpad', 'Skidpad'), ('none', 'none')], default=('Acceleration', 'Acceleration'), max_length=100)),
                ('mapping', models.BooleanField(default=True)),
                ('rectsBeforeTracking', models.BooleanField(default=True)),
                ('NNThreaded', models.BooleanField(default=True)),
                ('PCLThreaded', models.BooleanField(default=True)),
                ('datasetPath', models.CharField(default='/', max_length=300)),
                ('camera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JSONConfigurer.cameramodel')),
            ],
        ),
    ]