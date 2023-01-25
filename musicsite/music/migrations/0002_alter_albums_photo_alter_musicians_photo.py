# Generated by Django 4.1.5 on 2023-01-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/albums/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='musicians',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/musicians/%Y/%m/%d/'),
        ),
    ]