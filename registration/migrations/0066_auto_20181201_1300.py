# Generated by Django 2.1.3 on 2018-12-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0065_auto_20181201_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='ibmhackathonregistration',
            name='question1',
            field=models.TextField(default='Write your response here'),
        ),
        migrations.AddField(
            model_name='ibmhackathonregistration',
            name='question2',
            field=models.TextField(default='Write your response here'),
        ),
        migrations.AddField(
            model_name='ibmhackathonregistration',
            name='question3',
            field=models.TextField(default='Write your response here'),
        ),
        migrations.AddField(
            model_name='ibmhackathonregistration',
            name='question4',
            field=models.TextField(blank=True, default='Write your response here'),
        ),
    ]
