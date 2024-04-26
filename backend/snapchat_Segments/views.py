from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import CustomerList

def customer_list_list(request):
    customer_lists = CustomerList.objects.all()
    return render(request, 'customer_list_list.html', {'customer_lists': customer_lists})

def customer_list_detail(request, pk):
    customer_list = get_object_or_404(CustomerList, pk=pk)
    return render(request, 'customer_list_detail.html', {'customer_list': customer_list})