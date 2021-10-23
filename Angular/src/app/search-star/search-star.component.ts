import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-search-star',
  templateUrl: './search-star.component.html',
  styleUrls: ['./search-star.component.scss']
})
export class SearchStarComponent implements OnInit {
  Star: Array<StarData> = [];
  constructor(private http: HttpClient) {
   }

  ngOnInit(): void {
  }

  GetSearchValue(name: string) {
    let http = "http://127.0.0.1:5000/get_one_star_by_name/" + name;
    let data: any = [];
    try {
      fetch(http).then(function (response) {
        return response.json();
      }).then(function (myJson) {
        data = myJson
        console.log(data)
        let div2 = document.getElementById("name");
        div2.textContent = "Nazwa gwiazdy: " + data[0].name;
        let div3 = document.getElementById("brightness");
        div3.textContent = "Jasnosc gwiazdy: " + data[0].brightness;
        let div4 = document.getElementById("constellation_name");
        div4.textContent = "Gwiazdozbiór: " + data[0].constellation_name;
        let div5 = document.getElementById("discaverer_name");
        div5.textContent = "Nazwa odkrywcy: " + data[0].discaverer_name;
        let div6 = document.getElementById("distance");
        div6.textContent = "Dystans: " + data[0].distance;
        let div7 = document.getElementById("greek_symbol");
        div7.textContent = "Symbol grecki: " + data[0].greek_symbol;
        let div8 = document.getElementById("mass");
        div8.textContent = "Masa: " + data[0].mass;
        let div9 = document.getElementById("radial_speed");
        div9.textContent = "Prędkość radialna: " + data[0].radial_speed;
        let div10 = document.getElementById("rectascension");
        div10.textContent = "Rektascencja: " + data[0].rectascension;
        let div11 = document.getElementById("declination");
        div11.textContent = "Deklinacja: " + data[0].declination;
        let div12 = document.getElementById("star_type");
        div12.textContent = "Typ gwiazdy: " + data[0].star_type;
      })
    }
    catch (e: unknown) {
    }
  }


  getStar(name: string) {
    let url = 'http://127.0.0.1:5000/get_one_star_by_name/test';
    this.http.get(url).toPromise().then(data =>{
      for(let id in data){
        this.Star.push(data[id].id)
      }
    });
  }
}

export interface StarData {
  id: number,
  name: string,
  brightness: string,
  constellation_name: string,
  declination: string,
  discaverer_name: string,
  distance: string,
  greek_symbol: string,
  mass: number,
  radial_speed: number,
  rectascension: string,
  star_type: string,
}
