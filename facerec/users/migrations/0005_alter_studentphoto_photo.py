# Generated by Django 4.0.2 on 2022-03-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_attendance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentphoto',
            name='photo',
            field=models.ImageField(upload_to='D:\\Python\\Projects\\Face-Recognition-System\\data\\database'),
        ),
    ]
