from rest_framework import generics
from ..models import Company, Vacancy
from ..serializers import CompanySerializer, VacancySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class CompanyVacanciesView(generics.CreateAPIView):
    serializer_class = VacancySerializer
    def get_queryset(self):
        company_id = self.kwargs['id']
        return Vacancy.objects.filter(company_id=company_id)
    def perform_create(self, serializer):
        company_id = self.kwargs['id']
        serializer.save(company_id=company_id)
    
class VacancyListView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyTop10View(generics.CreateAPIView):
    serializer_class = VacancySerializer
    
    def get_queryset(self):
        return Vacancy.objects.order_by('-salary')[:10]
    
@api_view(['GET', 'POST'])
def company_vacancies(req, id):
    print(f"Received request method: {req.method}")
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
