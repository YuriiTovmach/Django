# Generated by Django 2.2 on 2019-05-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('tegline', models.CharField(max_length=500, verbose_name='tegline')),
                ('icon', models.CharField(max_length=255, verbose_name='icon')),
            ],
        ),
    ]
