import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api.service';

@Component({
  selector: 'app-constellation-more-info',
  templateUrl: './constellation-more-info.component.html',
  styleUrls: ['./constellation-more-info.component.scss']
})
export class ConstellationMoreInfoComponent implements OnInit {

  constructor(private api: ApiService, private router: Router) { }

  ngOnInit(): void {
    if (this.api.CONSTELLATION == null){
      this.router.navigate["/"];
    }
    document.getElementById("name").textContent = 'Gwiazdozbiór ' + this.api.CONSTELLATION.name;
    document.getElementById("dec").textContent = this.api.CONSTELLATION.declination + '°';
    document.getElementById("rec").textContent = this.api.CONSTELLATION.rectascension + 'h';
    document.getElementById("area").textContent = this.api.CONSTELLATION.area;
    document.getElementById("skyside").textContent = this.api.CONSTELLATION.sky_side;
    document.getElementById("symbolism").textContent = this.api.CONSTELLATION.symbolism; 
    this.api.numberofstar(this.api.CONSTELLATION.id).subscribe(res =>{
      document.getElementById("starnumber").textContent = res.numb;
      console.log(res.numb)
    });
    
  }
}
