from django.db import models
import uuid


class Invoice(models.Model):
    date = models.DateField(auto_now_add=True)
    invoice_no = models.CharField(
        max_length=100, unique=True, default=uuid.uuid4, editable=False
    )
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Invoice {self.invoice_no} - {self.customer_name}"


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="details", blank=True
    )
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.invoice.invoice_no} - {self.description}"
