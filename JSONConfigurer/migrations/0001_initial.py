# Generated by Django 3.1.4 on 2021-03-10 21:26

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
            name='ORBextractorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nFeautures', models.IntegerField()),
                ('scaleFactor', models.FloatField()),
                ('nLevels', models.IntegerField()),
                ('iniThFAST', models.IntegerField()),
                ('minThFAST', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SlamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RGB', models.BooleanField(default=True)),
                ('ThDepth', models.IntegerField()),
                ('DepthMapFactor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ViewerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KeyFrameSize', models.FloatField()),
                ('KeyFrameLineWidth', models.FloatField()),
                ('ReferenceSystemSize', models.FloatField()),
                ('ReferenceSystemLineWidth', models.FloatField()),
                ('GraphLineWidth', models.FloatField()),
                ('PointSize', models.FloatField()),
                ('CameraSize', models.FloatField()),
                ('CameraLineWidth', models.FloatField()),
                ('ViewpointX', models.FloatField()),
                ('ViewpointY', models.FloatField()),
                ('ViewpointZ', models.FloatField()),
                ('ViewpointF', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.CharField(blank=True, max_length=500)),
                ('Mission', models.CharField(choices=[('Acceleration', 'Acceleration'), ('Trackdrive', 'Trackdrive'), ('Skidpad', 'Skidpad'), ('none', 'none')], default=('Acceleration', 'Acceleration'), max_length=100)),
                ('Mapping', models.BooleanField(default=True)),
                ('RectsBeforeTracking', models.BooleanField(default=True)),
                ('NNThreaded', models.BooleanField(default=True)),
                ('PCLThreaded', models.BooleanField(default=True)),
                ('DatasetPath', models.CharField(default='/', max_length=300)),
                ('Camera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JSONConfigurer.cameramodel')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=500)),
                ('Camera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JSONConfigurer.cameramodel')),
                ('ORBExtractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JSONConfigurer.orbextractormodel')),
                ('SLAM', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JSONConfigurer.slammodel')),
                ('Viewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JSONConfigurer.viewermodel')),
            ],
        ),
    ]
