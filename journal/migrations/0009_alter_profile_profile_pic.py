# Generated by Django 4.0.6 on 2022-07-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]