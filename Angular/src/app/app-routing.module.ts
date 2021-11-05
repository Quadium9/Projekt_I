import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SearchStarComponent } from './search-star/search-star.component';
import { ConstellationListComponent } from './constellation-list/constellation-list.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { LoginSystemComponent } from './login-system/login-system.component';
import { RegisterComponent } from './register/register.component';
import { EmailComponent } from './email/email.component';
import { ConstellationInfoComponent } from './constellation-info/constellation-info.component';
import { FactsComponent } from './facts/facts.component';
import { FormComponent } from './form/form.component';
import { FormListComponent } from './form-list/form-list.component';
import { ToolbarAdminComponent } from './toolbar-admin/toolbar-admin.component';
import { ToolbarUserComponent } from './toolbar-user/toolbar-user.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { ProfileComponent } from './profile/profile.component';
import { MoreInfoStarComponent } from './more-info-star/more-info-star.component';
import { EditFormComponent } from './edit-form/edit-form.component';

const routes: Routes = [
  { path: 'edit-form', component: EditFormComponent},
  { path: 'search-star', component: SearchStarComponent},
  { path: 'constellation-list', component: ConstellationListComponent},
  { path: 'login-system', component: LoginSystemComponent},
  { path: 'register', component: RegisterComponent},
  { path: 'email', component:EmailComponent},
  { path: 'constellation', component:ConstellationInfoComponent},
  { path: 'facts', component:FactsComponent},
  { path: 'form', component:FormComponent},
  { path: 'default-toolbar', component:ToolbarComponent},
  { path: 'user-toolbar', component:ToolbarUserComponent},
  { path: 'admin-toolbar', component:ToolbarAdminComponent},
  { path: 'form-list', component:FormListComponent},
  { path: 'profil', component:ProfileComponent},
  { path: 'star-more-info', component:MoreInfoStarComponent},
  { path: '', component: WelcomeComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
