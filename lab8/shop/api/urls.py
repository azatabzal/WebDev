from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('products', views.products, name='products'),
	path('categories', views.categories, name='categories'),
	path('products/<int:id>', views.oneproduct, name='oneproduct'),
	path('categories/<int:id>', views.onecategory, name='onecategory')
]
