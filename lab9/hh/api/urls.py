from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('companies', views.companies, name='companies'),
	path('vacancies', views.vacancies, name='vacancies'),
	path('companies/<int:id>', views.onecompanies, name='onecompanies'),
	path('vacancies/<int:id>', views.onevacancies, name='onevacancies'),
	path('companies/<int:id>/vacancies', views.listvacancies, name='onecompanies'),
	path('vacancies/top_ten', views.top_ten, name='top_ten'),
]
