import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import {CompanyService} from '../company.service';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css'],
  imports: [CommonModule, RouterLink],
})
export class CompaniesComponent implements OnInit {

  companies: Company[] = [];

  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.getCompanies()
  }
  getCompanies(){
    this.companyService.getCompanies().subscribe((data)=>{
      this.companies = data;
    });
  }
  getVacancies(id:any){
    this.companyService.getVacancies(id).subscribe((data)=>{
      this.companyService.setData(data);
    });
  }

}