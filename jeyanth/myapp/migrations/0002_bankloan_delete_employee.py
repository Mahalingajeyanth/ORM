# Generated by Django 5.1.3 on 2024-11-16 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankLoan',
            fields=[
                ('acc', models.IntegerField(primary_key='accno', serialize=False)),
                ('ph', models.IntegerField()),
                ('ifsc', models.CharField(max_length=100)),
                ('loanno', models.IntegerField()),
                ('adress', models.CharField(max_length=100)),
                ('pan', models.IntegerField()),
                ('adhar', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
