# Generated by Django 2.1.3 on 2018-11-15 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0034_impromptooregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ETCRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('institution', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('subjects', models.CharField(choices=[('Physics', 'Physics'), ('Mathematics', 'Mathematics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Psychology', 'Psychology'), ('Economics', 'Economics')], default='English', max_length=200)),
                ('topic', models.CharField(max_length=800)),
                ('confirmation_email_sent', models.BooleanField(default=False)),
                ('isSubmit', models.BooleanField(default=False)),
                ('last_modify_date', models.DateTimeField(blank=True, null=True)),
                ('submit_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
