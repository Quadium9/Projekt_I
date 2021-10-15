import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SearchStarComponent } from './search-star/search-star.component';
import { ConstellationListComponent } from './constellation-list/constellation-list.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { LoginSystemComponent } from './login-system/login-system.component';
import { RegisterComponent } from './register/register.component';
import { EmailComponent } from './email/email.component';

const routes: Routes = [
  { path: 'search-star', component: SearchStarComponent},
  { path: 'constellation-list', component: ConstellationListComponent},
  { path: 'login-system', component: LoginSystemComponent},
  { path: 'register', component: RegisterComponent},
  { path: 'email', component:EmailComponent},
  { path: '', component: WelcomeComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
