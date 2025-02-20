# Generated by Django 5.0.6 on 2024-07-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='image',
            field=models.ImageField(default='profilepic.jpg', upload_to='cv'),
        ),
        migrations.AddField(
            model_name='cv',
            name='language',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='cv',
            name='project',
            field=models.TextField(default='', max_length=500),
        ),
    ]
