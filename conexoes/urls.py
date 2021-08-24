from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='conexoes'),
    path('con_search', views.search, name='con_search'),
    path('details', views.details, name='details'),
    path('<int:cidade_id>', views.bairros_filter, name='bairros_filter'),
    # path('<int:conexao_id>', views.details, name='details'),
    # path('search', views.search, name='search'),
]