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
    let lhtml = document.getElementById("list");
    let list: string [] = ["cs", "css", "csss", "kI","kII","kIII","hiue"]
    for (let i = 0; i < list.length; i++) {
      let div = document.createElement("div");
      let href = document.createElement("a");
      href.textContent = list [i];
      div.appendChild(href);
      this.renderer.setStyle(div,'width','50%')
      this.renderer.setStyle(div,'float','left')
      this.renderer.setStyle(div,'border-style','solid')
      this.renderer.setStyle(div,'border-width','1px')
      lhtml.appendChild(div);
    }
  }
}
