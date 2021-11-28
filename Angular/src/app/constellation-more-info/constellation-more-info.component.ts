import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { ApiService } from '../shared/api.service';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-constellation-more-info',
  templateUrl: './constellation-more-info.component.html',
  styleUrls: ['./constellation-more-info.component.scss']
})
export class ConstellationMoreInfoComponent implements OnInit {

  image:string;

  constructor(private api: ApiService, private router: Router, private cookieService: CookieService, private sanitizer:DomSanitizer) { }

  ngOnInit(): void {
    if (this.cookieService.get('CONSTELLATION') == null) {
      this.router.navigate["/constellation"];
    }
    document.getElementById("name").textContent = 'Gwiazdozbiór ' + this.cookieService.get('CONSTELLATION-name')
    document.getElementById("dec").textContent = this.cookieService.get('CONSTELLATION-declination') + '°';
    document.getElementById("rec").textContent = this.cookieService.get('CONSTELLATION-rectascension') + 'h';
    document.getElementById("area").textContent = this.cookieService.get('CONSTELLATION-area');
    document.getElementById("skyside").textContent = this.cookieService.get('CONSTELLATION-sky_side');
    document.getElementById("symbolism").textContent = this.cookieService.get('CONSTELLATION-symbolism')
    this.api.imageConstellations(this.cookieService.get('CONSTELLATION-id')).subscribe(res => {
      document.getElementById('star_number').textContent = res.star_number;
      this.image = '../../assets/photo/Constellations/' + res.picture;
    })
  }

  star_list(){
    this.router.navigate(['/star-list']);
  }
}