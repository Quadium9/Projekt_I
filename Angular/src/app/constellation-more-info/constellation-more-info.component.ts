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
        var dist: number = +resu[i].indistance;
        br = dist/br*1.5;
        let decin: number;
        let recin: number;
        let decout: number;
        let recout: number;
        //Star in
        decin = 3 * resu[i].xstarin + i * 25
        recin = 3 * resu[i].ystarin + i * 25
        decout = 3 * resu[i].xstarout + i * 25
        recout = 3 * resu[i].ystarout + i * 25
        console.log(decin, recin)
        this.circle(br, decin, recin);
        //this.line(decin, recin, decout, recout)
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