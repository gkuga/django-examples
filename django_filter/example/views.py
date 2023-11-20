from django.http import HttpResponse
from django.shortcuts import render
from . import filters, models


def index(request):
    return HttpResponse("Hello, world.")


def product_list(request):
    f = filters.ProductFilter(request.GET, queryset=models.Product.objects.all())
    return render(request, 'example/template.html', {'filter': f})
