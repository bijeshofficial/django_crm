# Generated by Django 3.0.8 on 2020-07-15 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200715_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Product'),
        ),
    ]
