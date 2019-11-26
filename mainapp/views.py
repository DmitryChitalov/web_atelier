from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    context = {
        'title': 'Магазин',
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request, category_pk=None, page=1):
    products = Product.objects.filter(category__is_active=True, is_active=True)
    categories = ProductCategory.objects.filter(is_active=True)

    if category_pk:
        if not category_pk == '0':
            current_category = get_object_or_404(ProductCategory, pk=category_pk)
            products = Product.objects.filter(category=current_category, is_active=True)

    paginator = Paginator(products, 2)
    try:
        paginator_page = paginator.page(page)
    except PageNotAnInteger:
        paginator_page = paginator.page(1)
    except EmptyPage:
        paginator_page = paginator.page(paginator.num_pages)

    context = {
        'title': 'Каталог',
        # 'products': products,
        'products': paginator_page,
        'categories': categories,
    }

    return render(request, 'mainapp/catalog.html', context)

def product(request, product_pk):
    categories = ProductCategory.objects.filter(is_active=True)
    product = get_object_or_404(Product, pk=product_pk)

    context = {
        'title': 'Продукт',
        'product': product,
        'categories': categories,
    }

    return render(request, 'mainapp/product.html', context)

def contact(request):

    context = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context)

