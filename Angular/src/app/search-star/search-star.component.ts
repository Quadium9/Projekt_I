import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { from } from 'rxjs';

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
    let data: any;
    fetch(http).then(function (response) {
      return response.json();
    }).then(function (myJson) {
      data = myJson
      console.log(data)
      let div = document.getElementById("resultsearch");
      let div2 = document.createElement("div");
      div2.textContent = data.name;
      let div3 = document.createElement("div");
      div3.textContent = data.id;
      div.appendChild(div2);
      div.appendChild(div3);
    })

  }
}
