# Generated by Django 4.2.19 on 2025-03-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_remove_alumni_email_remove_alumni_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='password',
            field=models.CharField(default='defaultpassword', max_length=255),
        ),
    ]
