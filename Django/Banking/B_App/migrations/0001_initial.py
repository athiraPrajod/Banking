# Generated by Django 2.2.1 on 2019-07-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=20)),
                ('Acc_No', models.IntegerField()),
                ('Cust_Name', models.CharField(max_length=50)),
                ('Curr_Balance', models.IntegerField()),
            ],
        ),
    ]