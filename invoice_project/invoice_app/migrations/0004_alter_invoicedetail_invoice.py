# Generated by Django 4.1.2 on 2023-08-02 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0003_alter_invoicedetail_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='invoice_app.invoice'),
        ),
    ]
