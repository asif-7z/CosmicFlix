# Generated by Django 4.2.4 on 2023-09-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
