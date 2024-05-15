from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.viewed += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'photo', 'price', 'category']
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'photo', 'price', 'category']
    # success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')




def base(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/product_list.html", context)


def contacts(request):
    """Принимает контактные данные от пользователя с сайта"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Ваше сообщение: {name}, {phone}, {message}')
        with open('write.txt', 'wt', encoding='UTF-8') as file:
            file.write(f'Ваше сообщение: {name}, {phone}, {message}')

    return render(request, 'catalog/contacts.html')






# def product_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'catalog/base.html', context)
#
#
# def product_detail(request, pk):
#     product_pk = get_object_or_404(Product, pk=pk)
#     context = {"product": product_pk}
#     return render(request, 'catalog/product_detail.html', context)


# def index(request):
#     return render(request, "catalog/home.html")
#
#
# def contacts(request):
#     return render(request, "catalog/contacts.html")
