import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-search-star',
  templateUrl: './search-star.component.html',
  styleUrls: ['./search-star.component.scss']
})
export class SearchStarComponent implements OnInit {

  constructor() { HttpClient}

  ngOnInit(): void {
  }

  private value:string;
  items = [];

  GetSearchValue(value:string){
    console.log(value)
    this.RequestSearch(value)
  }

  RequestSearch(name:string){
    let data =''
    fetch('http://127.0.0.1:5000/to-json-star').then(function(response){
      return response.json();
    }).then(function(myJson){
      data = myJson
      console.log(data) 
    })
  }
}
