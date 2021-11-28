import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule} from '@angular/material/toolbar'
import { MatIconModule } from '@angular/material/icon'
import { SearchStarComponent } from './search-star/search-star.component';
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
import { MoreInfoStarComponent } from './more-info-star/more-info-star.component';
import { ConfirmedstarComponent } from './confirmedstar/confirmedstar.component';
import { NonconfirmedstarComponent } from './nonconfirmedstar/nonconfirmedstar.component';
import { UserComponent } from './user/user.component';
import { EditFormComponent } from './edit-form/edit-form.component';
import { ConstellationMoreInfoComponent } from './constellation-more-info/constellation-more-info.component';
import { CookieService } from 'ngx-cookie-service';
import { StarListComponent } from './star-list/star-list.component';

@NgModule({
  declarations: [
    AppComponent,
    ToolbarComponent,
    SearchStarComponent,
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
    MoreInfoStarComponent,
    ConfirmedstarComponent,
    NonconfirmedstarComponent,
    UserComponent,
    EditFormComponent,
    ConstellationMoreInfoComponent,
    StarListComponent,
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
    ReactiveFormsModule,
  ],
  providers: [ authInterceptorProviders, CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
