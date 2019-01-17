# Generated by Django 2.1.4 on 2019-01-17 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0095_openmicregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOtherWordsSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('level', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')])),
                ('imageFile', models.ImageField(blank=True, upload_to=registration.models.InOtherWordsSubmission.filePathGenerate)),
                ('answer', models.TextField(max_length=2000)),
                ('comments', models.TextField(max_length=2000)),
                ('isSubmit', models.BooleanField(default=True)),
                ('submit_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
