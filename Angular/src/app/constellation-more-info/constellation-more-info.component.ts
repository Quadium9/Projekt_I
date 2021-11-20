import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { ApiService } from '../shared/api.service';

@Component({
  selector: 'app-constellation-more-info',
  templateUrl: './constellation-more-info.component.html',
  styleUrls: ['./constellation-more-info.component.scss']
})
export class ConstellationMoreInfoComponent implements OnInit {

  @ViewChild("mycanvas", { static: true })
  canvas: ElementRef<HTMLCanvasElement>;
  private ctx: CanvasRenderingContext2D

  constructor(private api: ApiService, private router: Router, private cookieService: CookieService) { }

  ngOnInit(): void {
    if (this.cookieService.get('CONSTELLATION') == null) {
      this.router.navigate["/constellation"];
    }
    this.ctx = this.canvas.nativeElement.getContext('2d');
    document.getElementById("name").textContent = 'Gwiazdozbiór ' + this.cookieService.get('CONSTELLATION-name')
    document.getElementById("dec").textContent = this.cookieService.get('CONSTELLATION-declination') + '°';
    document.getElementById("rec").textContent = this.cookieService.get('CONSTELLATION-rectascension') + 'h';
    document.getElementById("area").textContent = this.cookieService.get('CONSTELLATION-area');
    document.getElementById("skyside").textContent = this.cookieService.get('CONSTELLATION-sky_side');
    document.getElementById("symbolism").textContent = this.cookieService.get('CONSTELLATION-symbolism');
    this.getData(this.cookieService.get('CONSTELLATION-id'))
  }
  getData(id: string) {
    this.api.imagedataconst(id).subscribe(resu => {
      console.log(resu)
      let i = 0;
      for (i; i < resu.length; i++) {
        var br: number = +resu[i].inbrightness;
        let decin: number;
        let recin: number;
        let decout: number;
        let recout: number;
        //Star in
        decin = 500 + (resu[i].xstarin)
        if (resu[i].ystarin < 0) {
          recin = 1000 + (resu[i].ystarin)
        } else {
          recin = 500 + resu[i].ystarin;
        }
        console.log(decin, recin)
        this.circle(br / 30, decin, recin);
        //this.line(decin,recin, decout, recout)
      }
    })
  }


  circle(r: number, x: number, y: number) {
    this.ctx.beginPath();
    this.ctx.arc(x, y, r, 0, 2 * Math.PI);
    this.ctx.fillStyle = "white";
    this.ctx.fill();
    this.ctx.stroke();
  }
  line(Sx: number, Sy: number, Ex: number, Ey: number) {
    this.ctx.beginPath();
    this.ctx.moveTo(Sx, Sy);
    this.ctx.lineTo(Ex, Ey);
    this.ctx.strokeStyle = "white";
    this.ctx.lineWidth = 1;
    this.ctx.stroke();
  }
}