# Generated by Django 4.2.3 on 2023-07-19 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Data',
            fields=[
                ('Accno', models.IntegerField(primary_key=True, serialize=False)),
                ('Balance', models.FloatField()),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Customer_Data',
            fields=[
                ('Cust_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Phone_no', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('Trans_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('Type', models.CharField(max_length=30)),
                ('Accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.account_data')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='Money_Transfers',
            fields=[
                ('Trans_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('From_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From_accno', to='profiles.account_data')),
                ('To_accno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To_accno', to='profiles.account_data')),
            ],
            options={
                'db_table': 'transfers',
            },
        ),
        migrations.CreateModel(
            name='ECS_Data',
            fields=[
                ('ECS_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Payer_Name', models.CharField(max_length=300)),
                ('Upper_Limit', models.FloatField()),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.account_data')),
            ],
            options={
                'db_table': 'ecs',
            },
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField()),
                ('Completed', models.BooleanField()),
                ('ECS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.ecs_data')),
            ],
            options={
                'db_table': 'bills',
            },
        ),
        migrations.AddField(
            model_name='account_data',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.customer_data'),
        ),
    ]