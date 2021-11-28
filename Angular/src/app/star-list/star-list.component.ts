import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { ApiService } from '../shared/api.service';

@Component({
  selector: 'app-star-list',
  templateUrl: './star-list.component.html',
  styleUrls: ['./star-list.component.scss']
})
export class StarListComponent implements OnInit {

  starData !: any;

  constructor(private api: ApiService, private cookieService: CookieService, private router: Router) { }

  ngOnInit(): void {
    let const_name = this.cookieService.get("CONSTELLATION-name")
    this.api.getstarbyconstellation(const_name).subscribe( res =>{
      this.starData = res;
    })
  }

  moreInfo(row: any) {
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

  searchStar() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("inputName");
    filter = input.value.toUpperCase();
    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
}
