import { Component, OnInit } from '@angular/core';
import { ApiService } from '../shared/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-more-info-star',
  templateUrl: './more-info-star.component.html',
  styleUrls: ['./more-info-star.component.scss']
})
export class MoreInfoStarComponent implements OnInit {

  constructor(private api: ApiService, private router:Router) {}

  km:number;
  result:number;

  ngOnInit(): void {
    if (this.api.STAR == null){
      this.router.navigate(['/search-star']);
    }
    document.getElementById("starname").textContent = this.api.STAR.name;
    document.getElementById("starid").textContent = this.api.STAR.id;
    document.getElementById("starconstellation").textContent = this.api.STAR.constellation_name;
    document.getElementById("starbrightness").textContent = this.api.STAR.brightness + " L☉";
    document.getElementById("stardeclination").textContent = this.api.STAR.declinationh + "h " + this.api.STAR.declinationm + "m " + this.api.STAR.declinations + "s";
    document.getElementById("stardiscaverer").textContent = this.api.STAR.discaverer_name + " " + this.api.STAR.discaverer_lastname;
    document.getElementById("stardistance").textContent = this.api.STAR.distance + " l.y.";
    document.getElementById("starsymbol").textContent = this.api.STAR.greek_symbol;
    document.getElementById("starmass").textContent = this.api.STAR.mass + " M☉";
    document.getElementById("starspeed").textContent = this.api.STAR.radial_speed + " km/s";
    document.getElementById("starrectascension").textContent = this.api.STAR.rectascensionh + "° " + this.api.STAR.rectascensionh  + "′ " + this.api.STAR.rectascensionh + "″";
    document.getElementById("startype").textContent = this.api.STAR.star_type;
    document.getElementById("num").textContent = "50%";
  }

  getSliderValue(event) {
    document.getElementById("num").textContent = event.target.value + "%";
    var procent:number = +event.target.value;
    this.km = 1080000000 * procent;
    var mat = this.api.STAR.distance / (procent/100);
    if (this.api.STAR.distance == ""){
      document.getElementById("result").textContent = "Dystans od Słońca jest wymagany"
    } else{
      this.result = mat;
    }

 }
}
