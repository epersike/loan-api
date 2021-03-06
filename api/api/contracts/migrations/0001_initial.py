# Generated by Django 2.2.1 on 2019-06-04 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty_payment', models.IntegerField()),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ip_address', models.CharField(max_length=32)),
                ('ts_subscription', models.DateField(auto_now_add=True)),
                ('bank_name', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('payment_original_date', models.DateField()),
                ('payment_date', models.DateField(blank=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.Contract')),
            ],
        ),
    ]
