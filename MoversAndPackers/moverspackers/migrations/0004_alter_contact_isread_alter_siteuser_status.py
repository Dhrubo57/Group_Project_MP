# Generated by Django 5.1 on 2024-10-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moverspackers', '0003_siteuser_shiftingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='isread',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='status',
            field=models.CharField(max_length=300, null=True),
        ),
    ]