# Generated by Django 4.1.5 on 2023-01-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('desc', models.TextField()),
                ('img', models.ImageField()),
            ],
        ),
    ]
