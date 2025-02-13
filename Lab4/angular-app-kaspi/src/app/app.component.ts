import { Component } from '@angular/core';
import { StoreComponent } from './store/store.component';

@Component({
  selector: 'app-root',
  imports: [StoreComponent],
  template: `
    <main>
      <header>
      </header>
      <section>
        <app-store></app-store>
      </section>
    </main>
  `,

  styleUrl: './app.component.css',
  
})
export class AppComponent {
  title = 'angular-app-kaspi';
}
