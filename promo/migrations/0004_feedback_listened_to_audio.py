# Generated by Django 3.2.20 on 2023-08-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0003_auto_20230812_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='listened_to_audio',
            field=models.BooleanField(default=False),
        ),
    ]
