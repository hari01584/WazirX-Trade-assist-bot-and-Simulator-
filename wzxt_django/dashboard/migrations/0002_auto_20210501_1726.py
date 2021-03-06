# Generated by Django 3.2 on 2021-05-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.IntegerField(default=0)),
                ('currencyBase', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=7)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='instance_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transationType',
            field=models.CharField(default='buy', max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency',
            field=models.CharField(default='INR', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='money',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=7),
        ),
    ]
