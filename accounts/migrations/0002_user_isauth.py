# Generated by Django 5.0.6 on 2024-06-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isauth',
            field=models.BooleanField(default=False),
        ),
    ]