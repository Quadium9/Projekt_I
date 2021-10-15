import { Component, OnInit, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-constellation-list',
  templateUrl: './constellation-list.component.html',
  styleUrls: ['./constellation-list.component.scss']
})
export class ConstellationListComponent implements OnInit {

  constructor(private renderer: Renderer2) {
  }

  ngOnInit(): void {
    let url = "http://127.0.0.1:5000/to-jsonC"
    let data = [];
    fetch(url).then(function (response) {
      return response.json();
    }).then(function (myJson) {
      data = myJson
      console.log(data)
      let lhtml = document.getElementById("list");
      for (let i = 0; i < data.length; i++) {
        let div = document.createElement("div");
        let href = document.createElement("a");
        href.textContent = data[i].name;
        div.appendChild(href);
        div.setAttribute("style", "width:50%; float:left; border-style:solid; border-width:1px;");
        lhtml.appendChild(div);
      }
    })
  }
}
