import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'https://loaclhost:8000';
  constructor() { }
}
