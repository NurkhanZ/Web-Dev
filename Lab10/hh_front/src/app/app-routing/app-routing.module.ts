import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VacanciesComponent } from '../vacancies/vacancies.component';
import { CompaniesComponent } from '../companies/companies.component';
import { TestComponent } from '../test/test.component';
import { CommonModule } from '@angular/common';

export const routes: Routes = [
  { path: 'vacancies', component: VacanciesComponent },
  { path: 'test', component: TestComponent},
  { path: '', component: CompaniesComponent },
  { path: '**', redirectTo: '' },
]

@NgModule({
  imports: [CommonModule, RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
