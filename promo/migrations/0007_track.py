# Generated by Django 3.2.20 on 2023-08-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0006_auto_20230810_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tracks/images/')),
                ('title', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('info', models.TextField()),
                ('audio_file', models.FileField(upload_to='tracks/audio/')),
            ],
        ),
    ]
