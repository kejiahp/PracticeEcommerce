# Generated by Django 3.2.7 on 2021-12-02 11:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('order_used', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_details', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('receiverName', models.CharField(max_length=200)),
                ('phone1', models.CharField(max_length=50)),
                ('phone2', models.CharField(max_length=50, null=True)),
                ('ship_to_order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.ordered')),
            ],
        ),
    ]
