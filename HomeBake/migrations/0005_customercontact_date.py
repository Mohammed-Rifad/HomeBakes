# Generated by Django 4.2 on 2023-04-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeBake', '0004_customercontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercontact',
            name='date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]