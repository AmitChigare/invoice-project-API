from django.shortcuts import render

# Create your views here.
# invoice_app/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Process the nested invoice details manually
        details_data = request.data.get("details", [])
        for detail_data in details_data:
            detail_data["invoice"] = serializer.instance.id

        invoice_detail_serializer = serializer.fields["details"].child
        detail_serializer = invoice_detail_serializer(data=details_data, many=True)
        detail_serializer.is_valid(raise_exception=True)
        detail_serializer.save()

        return Response(serializer.data, status=201, headers=headers)
