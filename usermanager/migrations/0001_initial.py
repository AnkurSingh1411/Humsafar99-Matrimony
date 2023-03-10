# Generated by Django 2.2.3 on 2020-12-11 16:28

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
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=10)),
                ('dob', models.DateField()),
            ],
        ),
    ]
