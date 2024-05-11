from django.conf import settings
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, product_detail
from django.conf.urls.static import static


app_name = CatalogConfig.name

urlpatterns = [path("", base, name='product_list'),
               path("<int:pk>/", product_detail, name='product_detail')
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

