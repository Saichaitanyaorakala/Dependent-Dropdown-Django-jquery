# Generated by Django 3.0.7 on 2020-06-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.PositiveIntegerField(null=True)),
                ('executive_authority', models.CharField(blank=True, max_length=15, null=True, verbose_name='Is This Person also has Signing Authority')),
                ('exec_first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Executive First Name')),
                ('exec_last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Executive Last Name')),
                ('exec_title', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Executive Title/Position')),
                ('exec_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Executive - Email')),
                ('exec_phone_number', models.CharField(blank=True, max_length=17, null=True, verbose_name='Executive Phone Number')),
                ('payment_type', models.CharField(max_length=30)),
                ('institution_code', models.CharField(max_length=30)),
                ('branch_number', models.CharField(max_length=30)),
                ('account_number', models.CharField(max_length=30)),
            ],
        ),
    ]