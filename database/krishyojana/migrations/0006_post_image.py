# Generated by Django 3.1.1 on 2020-09-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishyojana', '0005_auto_20200926_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='emarket'),
        ),
    ]
