from rest_framework import generics
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

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