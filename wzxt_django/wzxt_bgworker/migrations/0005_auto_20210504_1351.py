# Generated by Django 3.2 on 2021-05-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wzxt_bgworker', '0004_alter_transaction_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='currency',
            field=models.CharField(default='BTC', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='rate',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=7),
        ),
    ]