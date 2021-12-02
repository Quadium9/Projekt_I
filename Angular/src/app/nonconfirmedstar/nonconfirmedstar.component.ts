import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';

let x = 1

@Component({
  selector: 'app-nonconfirmedstar',
  templateUrl: './nonconfirmedstar.component.html',
  styleUrls: ['./nonconfirmedstar.component.scss']
})
export class NonconfirmedstarComponent implements OnInit {

  errorMessage: string = "";
  noStar = false;
  starData !: any;
  endData: boolean = false;
  message: string = null;

  constructor(private api: ApiService, private router: Router, private tokenStorage: TokenStorageService, private cookieService: CookieService) { }

  ngOnInit(): void {
    x = 1
    if (this.tokenStorage.getToken() == null) {
      window.location.replace("/login-system")
    } else {
      this.getStar()
    }
  }
  getStar() {
    this.endData = false;
    this.api.getFormListNO(this.tokenStorage.getUser()[0].username, 1).subscribe(res => {
      if (res == null) {
        this.errorMessage = "Bląd wyszukiwania"
      } else {
        if (res[0] == null) {
          this.message = "Koniec danych"
          this.endData = true;
      }
        this.starData = res;
      }
    })
  }

  nextpage() {
    this.endData = false;
    let page = x + 1
    x = x + 1
    this.api.getFormListNO(this.tokenStorage.getUser()[0].username, page).subscribe(res => {
      if (res.result == false) {
        alert(res.message);
        x = 1
      } else {
        if (res[0] == null) {
            this.message = "Koniec danych"
            this.endData = true;
        }
        this.starData = res;
      }
    })
  }
  previouspage() {
    this.message = null;
    this.endData = false;
    let page = x - 1
    x = x - 1
    this.api.getFormListNO(this.tokenStorage.getUser()[0].username, page).subscribe(res => {
      if (res.result == false) {
        this.message = "Koniec danych"
        this.endData = true;
        alert(res.message);
        x = 1
      } else {
        this.starData = res;
      }
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

  confirmedstar(row: any) {
    this.api.confirmedstar(row.id, this.tokenStorage.getUser()[0].username).subscribe(res => {
      if (res.result) {
        alert(res.message);
        this.getStar()
      } else {
        alert(res.message);
      }
    })
  }

  deletestar(row: any) {
    let obj = {
      id: row.id,
      name: row.name
    }
    this.api.deletestar(obj, this.tokenStorage.getUser()[0].username).subscribe(res => {
      if (res.result) {
        alert(res.message)
        this.getStar()
      } else {
        alert(res.message)
      }
    })
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
