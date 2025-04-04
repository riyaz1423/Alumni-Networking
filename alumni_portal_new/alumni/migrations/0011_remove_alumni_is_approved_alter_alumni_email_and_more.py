# Generated by Django 4.2.19 on 2025-03-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0010_vacancy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='is_approved',
        ),
        migrations.AlterField(
            model_name='alumni',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
