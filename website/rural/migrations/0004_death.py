# Generated by Django 3.0 on 2021-11-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rural', '0003_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('DateOfBirth', models.DateField(max_length=50)),
                ('Age', models.CharField(max_length=3)),
                ('Blood_Group', models.CharField(max_length=30)),
                ('Religion', models.CharField(max_length=30)),
                ('Caste', models.CharField(max_length=30)),
                ('Community', models.CharField(max_length=30)),
                ('Name_Of_Father', models.CharField(max_length=50)),
                ('Name_Of_Mother', models.CharField(max_length=50)),
                ('Name_Of_Spouse', models.CharField(max_length=50)),
                ('Occupation', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=100)),
                ('MobileNumber', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=50)),
                ('PlaceOfDeath', models.CharField(max_length=50)),
                ('DateOfDeath', models.DateField(max_length=30)),
                ('TimeOfDeath', models.CharField(max_length=50)),
                ('HospitalName', models.CharField(max_length=30)),
                ('DeathAddress', models.TextField(max_length=50)),
                ('Pincode', models.CharField(max_length=6)),
                ('Problems_Of_Deceased', models.TextField(max_length=100)),
                ('Actual_Reason', models.TextField(max_length=100)),
                ('Cause_Of_Death', models.TextField(max_length=100)),
                ('Female_Death', models.TextField(max_length=100)),
                ('Habitual_Smoker', models.TextField(max_length=100)),
                ('Tobacco_User', models.TextField(max_length=100)),
                ('Forms_Of_Tobacco', models.TextField(max_length=100)),
                ('Alcoholic_Person', models.TextField(max_length=100)),
                ('Remarks', models.TextField(max_length=100)),
            ],
        ),
    ]