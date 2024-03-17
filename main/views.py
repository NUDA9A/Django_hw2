from django.shortcuts import render

from main.models import Product


def catalog(request):
    products = Product.objects.all()
    context = {
        'objects_list': products,
        'title': 'Каталог'
    }
    return render(request, 'main/catalog.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'object': product,
        'title': product.name
    }

    return render(request, 'main/product.html', context)

