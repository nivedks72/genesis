# Generated by Django 2.1.3 on 2018-12-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0085_pisround2registration_selectionstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pisround2registration',
            name='selectionStatus',
        ),
        migrations.AddField(
            model_name='pisregistration',
            name='selectionStatus',
            field=models.CharField(choices=[('notselected', 'Not Selected'), ('selected', 'Selected')], default='notselected', max_length=200),
        ),
    ]