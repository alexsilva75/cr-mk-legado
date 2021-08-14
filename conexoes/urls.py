from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='conexoes'),
    path('con_search', views.search, name='con_search'),
    # path('<int:listing_id>', views.listing, name='listing'),
    # path('search', views.search, name='search'),
]