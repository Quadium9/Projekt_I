import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-search-star',
  templateUrl: './search-star.component.html',
  styleUrls: ['./search-star.component.scss']
})
export class SearchStarComponent implements OnInit {

  constructor() { HttpClient }

  ngOnInit(): void {
  }

  GetSearchValue(name: string) {
    let http = "http://127.0.0.1:5000/get_one_star_by_name/" + name;
    let data: any = [];
    try{
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
/*
      for (let i = 0; i < data.length; i++) {
        let div2 = document.createElement("div");
        div2.textContent = "Nazwa gwiazdy: " + data[i].name;
        div2.setAttribute("style", "width:100%; text-align:center; padding:1%;");
        div2.setAttribute("id", "" + i)
        div.appendChild(div2);
      }*/
    })}
    catch(e:unknown){
      
    }
  }

  RemoveNode(){
    let div = document.getElementById("resultbox");
    if (div.hasChildNodes()) {
      let len: any = div.hasChildNodes.length;
      for (var i in len) {
        let rem = document.getElementById("" + i)
        rem.remove
      }
    }
  }
}
