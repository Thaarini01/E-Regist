# Generated by Django 3.0 on 2021-11-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rural', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
