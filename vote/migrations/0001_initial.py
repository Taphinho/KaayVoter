# Generated by Django 5.0.6 on 2024-06-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nbrvote', models.IntegerField(default=0)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
            ],
        ),
    ]
