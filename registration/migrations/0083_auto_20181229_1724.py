# Generated by Django 2.1.3 on 2018-12-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0082_pisround2registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pisregistration',
            name='member1email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pisregistration',
            name='member2email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pisregistration',
            name='member3email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
