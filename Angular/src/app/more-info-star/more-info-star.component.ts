import { Component, OnInit } from '@angular/core';
import { ApiService } from '../shared/api.service';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-more-info-star',
  templateUrl: './more-info-star.component.html',
  styleUrls: ['./more-info-star.component.scss']
})
export class MoreInfoStarComponent implements OnInit {

  constructor(private api: ApiService, private router:Router, private cookieService: CookieService) {}

  mapdiv: boolean = false;
  km:number = 0;
  result:number = 0;

  ngOnInit(): void {
    document.getElementById("starname").textContent = this.cookieService.get("STAR-name");
    document.getElementById("starid").textContent = this.cookieService.get("STAR-id");
    document.getElementById("starconstellation").textContent =  this.cookieService.get("STAR-constellation_name");
    document.getElementById("starbrightness").textContent = this.cookieService.get("STAR-brightness") + " L☉";
    document.getElementById("stardeclination").textContent = this.cookieService.get("STAR-declinationh") + "h " + this.cookieService.get("STAR-declinationm") + "m " + this.cookieService.get("STAR-declinations") + "s";
    document.getElementById("stardiscaverer").textContent = this.cookieService.get("STAR-discaverer_name") + " " + this.cookieService.get("STAR-discaverer_lastname");
    document.getElementById("stardistance").textContent = this.cookieService.get("STAR-distance") + " l.y.";
    document.getElementById("starsymbol").textContent = this.cookieService.get("STAR-greek_symbol");
    document.getElementById("starmass").textContent = this.cookieService.get("STAR-mass") + " M☉";
    document.getElementById("starspeed").textContent = this.cookieService.get("STAR-radial_speed") + " km/s";
    document.getElementById("starrectascension").textContent = this.cookieService.get("STAR-rectascensionh") + "° " + this.cookieService.get("STAR-rectascensionm")  + "′ " + this.cookieService.get("STAR-rectascensions") + "″";
    document.getElementById("startype").textContent = this.cookieService.get("STAR-star_type");
    document.getElementById("num").textContent = "0%";
  }

  getSliderValue(event) {
    document.getElementById("num").textContent = event.target.value + "%";
    var procent:number = +event.target.value;
    this.km = 1080000000 * procent;
    let mat:number = +this.cookieService.get("STAR-distance");
    mat = mat / (procent/100);
    if (this.cookieService.get("STAR-distance") == ""){
      document.getElementById("result").textContent = "Dystans od Słońca jest wymagany"
    } else{
      this.result = mat;
    }
 }

 showMap(){
  this.mapdiv = !this.mapdiv;
 }
}
