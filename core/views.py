from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader  # type: ignore


def home(request):
    produtos = Product.objects.all()
    context = {
        'curso': 'Primeiro Projeto Django',
        'produtos': produtos
    }
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    # prod = Product.objects.get(id=pk)

    prod = get_object_or_404(Product, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'product.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
