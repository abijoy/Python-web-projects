# Generated by Django 2.0.5 on 2018-11-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_auto_20181004_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
