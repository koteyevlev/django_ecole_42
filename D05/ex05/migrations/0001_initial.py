# Generated by Django 3.2.2 on 2021-05-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('title', models.CharField(max_length=64)),
                ('episode_nb', models.AutoField(primary_key=True, serialize=False)),
                ('opening_crawl', models.TextField()),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
