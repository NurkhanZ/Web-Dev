import { Routes } from '@angular/router';
import { VacanciesComponent } from './vacancies/vacancies.component';

export const routes: Routes = [
    { path : 'vacancies/:id', component: VacanciesComponent}
];
