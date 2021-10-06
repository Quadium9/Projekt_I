import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SearchStarComponent } from './search-star/search-star.component';
import { ConstellationListComponent } from './constellation-list/constellation-list.component';
import { WelcomeComponent } from './welcome/welcome.component';

const routes: Routes = [
  { path: 'search-star', component: SearchStarComponent},
  { path: 'constellation-list', component: ConstellationListComponent},
  { path: '', component: WelcomeComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
