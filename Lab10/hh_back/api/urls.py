from django.urls import path
from api.views import CompanyListView, CompanyDetailView, CompanyVacanciesView, VacancyListView, VacancyDetailView, VacancyTop10View
from django.http import HttpResponseRedirect
from api.views import companies_list, company_detail, vacancy_list, vacancy_detail, company_vacancies, top_vacancies
# urlpatterns = [
#     path('companies/',companies_list, name='company_list'),
#     path('companies/<int:company_id>/', company_detail, name='company_detail'),
#     path('companies/<int:company_id>/vacancies/', company_vacancies, name='companies_vacancies'),
#     path('vacancies/', vacancy_list, name='vacancy_list'),
#     path('vacancies/<int:vacancy_id>/', vacancy_detail, name='vacancy_detail'),
#     path('vacancies/top_ten/',top_vacancies, name='vacancies_top' ),
#     path('', lambda request: HttpResponseRedirect('/api/companies/')),
# ]

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:company_id>/', CompanyDetailView.as_view(), name='company_detail'),
    # path('companies/<int:company_id>/vacancies/', CompanyVacanciesView.as_view(), name='companies_vacancies'),
    path('companies/<int:id>/vacancies/', company_vacancies),
    
    path('vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:vacancy_id>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/top_ten/', VacancyTop10View.as_view(), name='vacancies_top'),
    path('', lambda request: HttpResponseRedirect('/api/companies/')),
]