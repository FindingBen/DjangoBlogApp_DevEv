# Generated by Django 3.1 on 2020-10-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='journey_pics'),
        ),
    ]
