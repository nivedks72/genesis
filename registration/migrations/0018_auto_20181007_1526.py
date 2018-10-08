# Generated by Django 2.1.1 on 2018-10-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_decoherenceregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decoherenceregistration',
            name='contact2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='decoherenceregistration',
            name='email2',
            field=models.EmailField(blank=True, max_length=144),
        ),
        migrations.AlterField(
            model_name='decoherenceregistration',
            name='participant2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='decoherenceregistration',
            name='qualification2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]