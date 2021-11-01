import { Component, Input, OnInit } from '@angular/core';
import { ApiService } from '../shared/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-more-info-star',
  templateUrl: './more-info-star.component.html',
  styleUrls: ['./more-info-star.component.scss']
})
export class MoreInfoStarComponent implements OnInit {

  constructor(private api: ApiService, private router:Router) {}

  ngOnInit(): void {
    if (this.api.STAR == null){
      this.router.navigate(['/search-star']);
    }
    console.log(this.api.STAR)
    document.getElementById("starname").textContent = this.api.STAR.name;
    document.getElementById("starid").textContent = this.api.STAR.id;
    document.getElementById("starconstellation").textContent = this.api.STAR.constellation_name;
    document.getElementById("starbrightness").textContent = this.api.STAR.brightness;
    document.getElementById("stardeclination").textContent = this.api.STAR.declination;
    document.getElementById("stardiscaverer").textContent = this.api.STAR.discaverer_name + " " + this.api.STAR.discaverer_lastname;
    document.getElementById("stardistance").textContent = this.api.STAR.distance;
    document.getElementById("starsymbol").textContent = this.api.STAR.greek_symbol;
    document.getElementById("starmass").textContent = this.api.STAR.mass;
    document.getElementById("starspeed").textContent = this.api.STAR.radial_speed;
    document.getElementById("starrectascension").textContent = this.api.STAR.rectascension;
    document.getElementById("startype").textContent = this.api.STAR.star_type;
       
  }

}
