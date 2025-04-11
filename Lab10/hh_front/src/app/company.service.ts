import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Company,Vacancy} from './models'
import {Observable} from 'rxjs';
import {BehaviorSubject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  BASE_URL = 'http://localhost:8000';
  constructor(private http: HttpClient) { }

  private apiData = new BehaviorSubject<Vacancy[]>([]);
  public apiData$ = this.apiData.asObservable();

  setData(data:any) { 
    this.apiData.next(data)
  }

  getCompanies():Observable<Company[]>{
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  }
  getVacancies(id:any):Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`);
  }
}