# Generated by Django 4.2.19 on 2025-03-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0011_remove_alumni_is_approved_alter_alumni_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
