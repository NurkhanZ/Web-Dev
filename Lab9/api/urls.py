from django.urls import path
from . import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name='company-list'),
    path('companies/<int:company_id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('companies/<int:company_id>/vacancies/', views.CompanyVacanciesView.as_view(), name='companies_vacancies'),
    path('vacancies/', views.VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:vacancy_id>/', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/top_ten/', views.VacancyTop10View.as_view(), name='vacancies_top'),
    path('', lambda request: HttpResponseRedirect('/api/companies/')),
]