# Generated by Django 3.0.5 on 2021-03-11 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JSONConfigurer', '0008_auto_20210311_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalmodel',
            name='ORBExtractor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JSONConfigurer.ORBExtractorModel'),
        ),
    ]
