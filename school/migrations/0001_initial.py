# Generated by Django 3.2.5 on 2022-02-04 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True)),
                ('name', models.CharField(default='0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=20)),
                ('gender', models.CharField(default='0', max_length=10)),
                ('email', models.CharField(default='0', max_length=30)),
                ('education', models.CharField(default='0', max_length=30)),
                ('DOB', models.DateField(default=datetime.date(1111, 11, 11))),
                ('contact', models.CharField(default='0', max_length=13)),
                ('age', models.IntegerField(default='0')),
                ('address', models.CharField(default='0', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=30)),
                ('desc', models.CharField(default='0', max_length=200)),
                ('s_date', models.DateField(default=datetime.date(1111, 11, 11))),
                ('associate_links', models.URLField(blank=True)),
                ('imp', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='to_do',
            fields=[
                ('id', models.IntegerField(default='0', primary_key=True, serialize=False)),
                ('work_due', models.CharField(default='0', max_length=200)),
                ('due_date', models.DateField(default=datetime.date(1111, 11, 11))),
            ],
        ),
        migrations.CreateModel(
            name='upcomingevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(default='0', upload_to='upcoming_events')),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
