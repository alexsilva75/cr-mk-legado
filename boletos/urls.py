from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='boletos'),
    path('bol_search', views.search, name='bol_search'),
    # path('<int:listing_id>', views.listing, name='listing'),
    # path('search', views.search, name='search'),
]