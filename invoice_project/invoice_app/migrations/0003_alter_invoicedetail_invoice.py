# Generated by Django 4.2.3 on 2023-07-31 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0002_alter_invoicedetail_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='invoice_app.invoice'),
        ),
    ]
