# Generated by Django 3.0.7 on 2020-07-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defaultimage.jpg', upload_to='profile_pics'),
        ),
    ]
