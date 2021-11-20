import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { ApiService } from '../shared/api.service';

@Component({
  selector: 'app-constellation-list',
  templateUrl: './constellation-list.component.html',
  styleUrls: ['./constellation-list.component.scss']
})
export class ConstellationListComponent implements OnInit {

  constellationdata !: any;

  constructor(private api: ApiService, private router: Router, private cookieService:CookieService) {}

  ngOnInit(): void {
    this.getConst()
  }

  getConst(){
    this.api.allconstellations().subscribe(res=>{
      this.constellationdata = res;
    })
  }
  moreInfo(row:any) {
    this.cookieService.set("CONSTELLATION-id",row.id)
    this.cookieService.set("CONSTELLATION-name",row.name)
    this.cookieService.set("CONSTELLATION-area",row.area)
    this.cookieService.set("CONSTELLATION-declination",row.declination)
    this.cookieService.set("CONSTELLATION-rectascension",row.rectascension)
    this.cookieService.set("CONSTELLATION-sky_side",row.sky_side)
    this.cookieService.set("CONSTELLATION-symbolism",row.symbolism)
    this.router.navigate(['/constellation-more-info']);
  }
}
