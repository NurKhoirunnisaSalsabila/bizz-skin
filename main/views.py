from django.shortcuts import render, redirect  
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Test

def show_main(request):
    products = Product.objects.all()

    context = {
        'app name': 'Happy Skin',
        'name': 'Nur Khoirunnisa Salsabila',
        'npm' : '2306165534',
        'class': 'PBP A',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    else:
        print(form.errors)

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")