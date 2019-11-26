from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from authapp.models import ShopUser
from adminapp.forms import ShopUserAdminRegisterForm, ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# @user_passes_test(lambda x: x.is_superuser)
# def index(request, page=1):
#     users = ShopUser.objects.all()
#
#     paginator = Paginator(users, 2)
#     try:
#         paginator_page = paginator.page(page)
#     except PageNotAnInteger:
#         paginator_page = paginator.page(1)
#     except EmptyPage:
#         paginator_page = paginator.page(paginator.num_pages)
#
#     context = {
#         # 'objects': users,
#         'objects': paginator_page,
#     }
#
#     return render(request, 'adminapp/index.html', context)

class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/index.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def user_create(request):
    title = 'Новый пользователь'

    if request.method == 'POST':
        form = ShopUserAdminRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:index'))
    else:
        form = ShopUserAdminRegisterForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_update.html', context)


def user_update(request, pk):
    title = 'Редактирование пользователя'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        form = ShopUserAdminEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:index'))
    else:
        form = ShopUserAdminEditForm(instance=user)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    title = 'Удаление пользователя'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:index'))

    context = {
        'title': title,
        'object': user,
    }

    return render(request, 'adminapp/user_delete.html', context)

def user_recover(request, pk):
    title = 'Востановление пользователя'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('admin:index'))

    context = {
        'title': title,
        'object': user,
    }

    return render(request, 'adminapp/user_recover.html', context)

def categories(request):
    title = 'Админка/Категории'
    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', context)


def products(request, category_pk):
    title = 'Админка/Продукт'

    category = get_object_or_404(ProductCategory, pk=category_pk)
    # products_list = Product.objects.filter(category__pk=pk).order_by('name')
    products_list = category.product_set.all().order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)

def product_create(request, category_pk):
    title = 'Новый продукт'
    category = get_object_or_404(ProductCategory, pk=category_pk)

    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'form': form,
        'category': category
    }

    return render(request, 'adminapp/product_update.html', context)


# def product_read(request, pk):
#     title = 'Продукт/Подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'title': title,
#         'object': product
#     }
#     return render(request, 'adminapp/product_read.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

def product_update(request, pk):
    title = 'Редактирование продукта'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:product_update',
                                                kwargs={'pk': product.pk}))
    else:
        form = ProductEditForm(instance=product)

    context = {
        'title': title,
        'form': form,
        'category': product.category
    }

    return render(request, 'adminapp/product_update.html', context)


def product_delete(request, pk):
    title = 'Удаление продукта'
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.is_active = False
        item.save()
        return HttpResponseRedirect(reverse('admin:products',
                                            kwargs={'category_pk': item.category.pk}))

    context = {
        'title': title,
        'object': item,
    }

    return render(request, 'adminapp/product_delete.html', context)

def product_recover(request, pk):
    title = 'Востановление продукта'
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.is_active = True
        item.save()
        return HttpResponseRedirect(reverse('admin:products',
                                            kwargs={'category_pk': item.category.pk}))

    context = {
        'title': title,
        'object': item,
    }

    return render(request, 'adminapp/product_recover.html', context)

# def category_create(request):
#     title = 'Новая категория'
#
#     if request.method == 'POST':
#         form = ProductCategoryEditForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'form': form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = ('__all__')
    # form_class = ProductCategoryEditForm

# def category_update(request, pk):
#     title = 'Редактирование категории'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         form = ProductCategoryEditForm(instance=category)
#
#     context = {
#         'title': title,
#         'form': form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)

class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = ('__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории/Редактирование'
        return context

# def category_delete(request, pk):
#     title = 'Удаление категории'
#     item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         # item.delete()
#         item.is_active = False
#         item.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#
#     context = {
#         'title': title,
#         'object': item,
#     }
#
#     return render(request, 'adminapp/category_delete.html', context)

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admin:categories')
    template_name = 'adminapp/category_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

def category_recover(request, pk):
    title = 'Восстановление категории'
    item = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        # item.delete()
        item.is_active = True
        item.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    context = {
        'title': title,
        'object': item,
    }

    return render(request, 'adminapp/category_recover.html', context)