# Generated by Django 4.2.5 on 2023-10-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_video', '0015_alter_series_name_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(),
        ),
    ]