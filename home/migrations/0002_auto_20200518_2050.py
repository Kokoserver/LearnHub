# Generated by Django 3.0.5 on 2020-05-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.CharField(blank=True, default='2020-05-18', max_length=10),
        ),
        migrations.AlterField(
            model_name='enrolcourse',
            name='date',
            field=models.CharField(blank=True, default='2020-05-18', max_length=10),
        ),
    ]
