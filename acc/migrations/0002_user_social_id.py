# Generated by Django 4.1.2 on 2023-02-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='social_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
