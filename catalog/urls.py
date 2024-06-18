from django.conf import settings
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, contacts, CategoryListView
from django.conf.urls.static import static
from django.urls import path


app_name = CatalogConfig.name

urlpatterns = [path("", cache_page(60)(ProductListView.as_view()), name='product_list'),
               path("<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
               path('contacts/', contacts, name='contacts'),
               path('catalog/create', ProductCreateView.as_view(), name='product_create'),
               path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
               path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
               path('categories/', cache_page(60)(CategoryListView.as_view()), name="categories_list"),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
