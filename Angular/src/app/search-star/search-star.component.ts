import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { ApiService } from '../shared/api.service';

const STAR = "";

@Component({
  selector: 'app-search-star',
  templateUrl: './search-star.component.html',
  styleUrls: ['./search-star.component.scss']
})
export class SearchStarComponent implements OnInit {

  errorMessage = "";
  noStar = false;
  starData !: any;
  constructor(private api: ApiService, private router: Router, private cookieService: CookieService) {
  }
  ngOnInit(): void {
  }

  getStar(name: string) {
    this.api.getStarByName(name).subscribe(res => {
      if (res == null) {
        this.errorMessage = "Bląd wyszukania gwiazdy"
      } else {
        this.starData = res;
      }
    })
  }
  moreInfo(row:any) {
    this.cookieService.set("STAR-id", row.id);
    this.cookieService.set("STAR-name", row.name);
    this.cookieService.set("STAR-confirmed", row.confirmed);
    this.cookieService.set("STAR-rectascensionh", row.rectascensionh);
    this.cookieService.set("STAR-rectascensionm", row.rectascensionm);
    this.cookieService.set("STAR-rectascensions", row.rectascensions);
    this.cookieService.set("STAR-declinationh", row.declinationh);
    this.cookieService.set("STAR-declinationm", row.declinationm);
    this.cookieService.set("STAR-declinations", row.declinations);
    this.cookieService.set("STAR-radial_speed", row.radial_speed);
    this.cookieService.set("STAR-distance", row.distance);
    this.cookieService.set("STAR-brightness", row.brightness);
    this.cookieService.set("STAR-star_type", row.star_type);
    this.cookieService.set("STAR-mass", row.mass);
    this.cookieService.set("STAR-greek_symbol", row.greek_symbol);
    this.cookieService.set("STAR-discaverer_name", row.discaverer_name);
    this.cookieService.set("STAR-discaverer_lastname", row.discaverer_lastname);
    this.cookieService.set("STAR-constellation_name", row.constellation_name);
    this.router.navigate(['/star-more-info']);
  }
}