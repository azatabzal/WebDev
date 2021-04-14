from django.shortcuts import render
from .models import company
from .models import vacancy
  
def index(request):
	return render(request, 'api/index.html')

def companies(request):
	companies = company.objects.all()
	return render(request, 'api/companies.html', {'companies': companies})

def vacancies(request):
	vacancies = vacancy.objects.all()
	return render(request, 'api/vacancies.html', {'vacancies': vacancies})

def onecompanies(request, id):
    companies = company.objects.order_by('id')[id-1:id]
    return render(request, 'api/companies.html', {'companies': companies})

def onevacancies(request, id):
    vacancies = vacancy.objects.order_by('id')[id-1:id]
    return render(request, 'api/vacancies.html', {'vacancies': vacancies})

def listvacancies(request, id):
    vacancies = vacancy.objects.filter(company=id)
    return render(request, 'api/vacancies.html', {'vacancies': vacancies})

def top_ten(request):
    vacancies = vacancy.objects.order_by('salary').reverse()[:10]
    return render(request, 'api/vacancies.html', {'vacancies': vacancies})