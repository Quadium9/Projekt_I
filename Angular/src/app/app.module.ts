import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule} from '@angular/material/toolbar'
import { MatIconModule } from '@angular/material/icon'
import { SearchStarComponent } from './search-star/search-star.component';
import { DrawConstComponent } from './draw-const/draw-const.component';
import { StarsComponent } from './stars/stars.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { ConstellationListComponent } from './constellation-list/constellation-list.component';
import { LoginSystemComponent } from './login-system/login-system.component';
import { RegisterComponent } from './register/register.component';
import { UnderLineComponent } from './under-line/under-line.component';
import { EmailComponent } from './email/email.component';
import { ConstellationInfoComponent } from './constellation-info/constellation-info.component';
import { FactsComponent } from './facts/facts.component';
import { ToolbarAdminComponent } from './toolbar-admin/toolbar-admin.component';
import { ToolbarUserComponent } from './toolbar-user/toolbar-user.component';
import { FormComponent } from './form/form.component';
import { FormListComponent } from './form-list/form-list.component';
import { authInterceptorProviders } from './_helpers/auth.interceptor';
import { ProfileComponent } from './profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    ToolbarComponent,
    SearchStarComponent,
    DrawConstComponent,
    StarsComponent,
    WelcomeComponent,
    ConstellationListComponent,
    LoginSystemComponent,
    RegisterComponent,
    UnderLineComponent,
    EmailComponent,
    ConstellationInfoComponent,
    FactsComponent,
    ToolbarAdminComponent,
    ToolbarUserComponent,
    FormComponent,
    FormListComponent,
    ProfileComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    FormsModule,
  ],
  providers: [ authInterceptorProviders],
  bootstrap: [AppComponent]
})
export class AppModule { }
