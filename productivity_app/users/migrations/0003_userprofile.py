# Generated by Django 4.2.2 on 2023-07-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('face_book_profile', models.CharField(max_length=150)),
                ('twitter_profile', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='profile_images')),
            ],
        ),
    ]
