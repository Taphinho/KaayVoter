# Generated by Django 5.0.6 on 2024-06-30 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_candidat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
