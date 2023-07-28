# Generated by Django 4.2.2 on 2023-07-28 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('text', models.CharField(max_length=300)),
                ('parent_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks_list.list')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]