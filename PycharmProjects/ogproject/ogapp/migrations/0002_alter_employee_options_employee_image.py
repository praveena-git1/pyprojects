# Generated by Django 5.1 on 2024-09-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='profile.jpg', upload_to='images/'),
        ),
    ]
