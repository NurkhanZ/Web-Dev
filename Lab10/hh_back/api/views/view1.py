from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from django.http import JsonResponse

# List all companies and create a new company
@api_view(['GET', 'POST'])
def companies_list(req):
    if req.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        data = req.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Retrieve, update, or delete a company
@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(req, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return Response({"message": "Company not found"}, status=404)
    
    if req.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    elif req.method == 'PUT':
        data = req.data
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif req.method == 'DELETE':
        company.delete()
        return Response({"message": "Company deleted successfully"}, status=204)

# List vacancies for a specific company and create a new vacancy
@api_view(['GET', 'POST'])
def company_vacancies(req, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return Response({"message": "Company not found"}, status=404)
    
    if req.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    
    elif req.method == 'POST':
        data = req.data
        data['company'] = company.id  # Associate vacancy with company
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# List all vacancies
@api_view(['GET'])
def vacancy_list(req):
    if req.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

# Retrieve, update, or delete a specific vacancy
@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(req, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return Response({"message": "Vacancy not found"}, status=404)
    
    if req.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    
    elif req.method == 'PUT':
        data = req.data
        serializer = VacancySerializer(instance=vacancy, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif req.method == 'DELETE':
        vacancy.delete()
        return Response({"message": "Vacancy deleted successfully"}, status=204)

# Top 10 vacancies based on salary
@api_view(['GET'])
def top_vacancies(req):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
