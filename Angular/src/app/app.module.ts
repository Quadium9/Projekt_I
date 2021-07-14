import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule} from '@angular/material/toolbar'
import { MatIconModule } from '@angular/material/icon'
import { SlonceComponent } from './slonce/slonce.component';
import { CaruselComponent } from './carusel/carusel.component';
import { SearchStarComponent } from './search-star/search-star.component';
import { DrawConstComponent } from './draw-const/draw-const.component';

@NgModule({
  declarations: [
    AppComponent,
    ToolbarComponent,
    SlonceComponent,
    CaruselComponent,
    SearchStarComponent,
    DrawConstComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
