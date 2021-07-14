import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-slonce',
  templateUrl: './slonce.component.html',
  styleUrls: ['./slonce.component.scss']
})
export class SlonceComponent implements OnInit {
  url = 'http://127.0.0.1:5000/to-json-star' 
  items = []
  /*Solar radius */
  starsize = 0.1542 * 10
  
  constructor(private http: HttpClient) {
    this.http.get<Istar>(this.url).toPromise().then(
      data => {
        for (let name in data)
          if (data.hasOwnProperty(name)) {
            this.items.push(data[name])
          }
      }
    )
  }

  ngOnInit(): void {
  }
}

export interface Istar{
  id: number;
  name: string;
  distance: number;
}