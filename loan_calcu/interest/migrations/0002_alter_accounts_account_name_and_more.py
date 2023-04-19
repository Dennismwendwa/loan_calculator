# Generated by Django 4.2 on 2023-04-19 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='account_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='account_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='accounty_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='month_saving',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savings',
            name='month',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='interest.month_saving'),
        ),
    ]
