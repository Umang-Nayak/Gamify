# Generated by Django 5.0 on 2023-12-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gamify_Admin', '0003_company_type_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamifyuser',
            name='user_otp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gamifyuser',
            name='user_otp_used',
            field=models.IntegerField(null=True),
        ),
    ]
