# Generated by Django 2.2.2 on 2019-06-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('TAC_number', models.CharField(max_length=15)),
                ('Subject', models.CharField(max_length=23)),
                ('KRA_PIN', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('Registration_number', models.CharField(max_length=5)),
                ('Email', models.EmailField(max_length=70)),
                ('Phonenumber', models.CharField(max_length=12)),
                ('Profession', models.CharField(max_length=15)),
                ('Date_employed', models.DateField(max_length=10, null=True)),
            ],
        ),
    ]
