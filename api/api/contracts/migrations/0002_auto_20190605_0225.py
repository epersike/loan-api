# Generated by Django 2.2.1 on 2019-06-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
