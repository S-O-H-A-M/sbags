# Generated by Django 3.0.6 on 2020-05-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
