# Generated by Django 2.2.5 on 2019-11-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradesApp', '0008_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='dld',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='dm',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='ds',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='la',
            field=models.IntegerField(blank=True),
        ),
    ]
