# Generated by Django 2.2.1 on 2019-06-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_auto_20190605_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_original_date',
            field=models.DateField(),
        ),
    ]