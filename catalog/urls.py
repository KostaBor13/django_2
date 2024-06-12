from django.conf import settings
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, contacts
from django.conf.urls.static import static
from django.urls import path

# from myapp.views import HomePageView

app_name = CatalogConfig.name

urlpatterns = [path("", ProductListView.as_view(), name='product_list'),
               path("<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
               path('contacts/', contacts, name='contacts'),
               path('catalog/create', ProductCreateView.as_view(), name='product_create'),
               path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
               path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
