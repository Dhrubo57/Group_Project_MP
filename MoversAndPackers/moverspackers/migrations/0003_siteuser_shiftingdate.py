# Generated by Django 5.1 on 2024-10-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moverspackers', '0002_remove_siteuser_professional_remove_siteuser_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='shiftingdate',
            field=models.DateField(null=True),
        ),
    ]
