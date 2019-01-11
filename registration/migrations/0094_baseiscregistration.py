# Generated by Django 2.1.4 on 2019-01-11 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0093_auto_20190112_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseISCRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('school_name', models.CharField(max_length=127)),
                ('school_address', models.TextField(max_length=2000)),
                ('city', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('school_contact', models.CharField(max_length=20)),
                ('teacher_contact', models.CharField(blank=True, max_length=20)),
                ('student1a', models.CharField(blank=True, max_length=127)),
                ('class1a', models.CharField(blank=True, max_length=127)),
                ('student1b', models.CharField(blank=True, max_length=127)),
                ('class1b', models.CharField(blank=True, max_length=127)),
                ('student1c', models.CharField(blank=True, max_length=127)),
                ('class1c', models.CharField(blank=True, max_length=127)),
                ('student2a', models.CharField(blank=True, max_length=127)),
                ('class2a', models.CharField(blank=True, max_length=127)),
                ('student2b', models.CharField(blank=True, max_length=127)),
                ('class2b', models.CharField(blank=True, max_length=127)),
                ('student2c', models.CharField(blank=True, max_length=127)),
                ('class2c', models.CharField(blank=True, max_length=127)),
                ('student3a', models.CharField(blank=True, max_length=127)),
                ('class3a', models.CharField(blank=True, max_length=127)),
                ('student3b', models.CharField(blank=True, max_length=127)),
                ('class3b', models.CharField(blank=True, max_length=127)),
                ('student3c', models.CharField(blank=True, max_length=127)),
                ('class3c', models.CharField(blank=True, max_length=127)),
                ('howyouknow', models.CharField(blank=True, max_length=200)),
                ('confirmation_email_sent', models.BooleanField(default=False)),
                ('isSubmit', models.BooleanField(default=False)),
                ('last_modify_date', models.DateTimeField(blank=True, null=True)),
                ('submit_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
