import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-draw-const',
  templateUrl: './draw-const.component.html',
  styleUrls: ['./draw-const.component.scss']
})


export class DrawConstComponent implements OnInit {
  @ViewChild('canvas', { static: true })
  canvas: ElementRef<HTMLCanvasElement>;
  private ctx: CanvasRenderingContext2D;

  constructor() {
  }
  global_id: number;

  ngOnInit(): void {
    this.ctx = this.canvas.nativeElement.getContext('2d');
    this.animate();
  }
  animate(): void {
    this.ctx.fillStyle = 'white';
    const DMetod = new drawingMetod(this.ctx);
    DMetod.Fill_circle(5,100,100);
    DMetod.Line(100,100,200,200);
    DMetod.Fill_circle(10,200,200);
    /*
    let drawing_constellation:any = DMetod.GetSearchValue("21")
    console.log(drawing_constellation + 1)
    for (var i in drawing_constellation){
      let first:any = DMetod.GetSearchStar(drawing_constellation[i].star_name_in);
      DMetod.Fill_circle(first.brightness, first.rectascension, first.declination);
      console.log(first.brightness, first.rectascension, first.declination)
      let second:any = DMetod.GetSearchStar(drawing_constellation[i].star_name_out);
      DMetod.Fill_circle(second.brightness, second.rectascension, second.declination);
      DMetod.Line(first.rectascension, second.rectascension, first.declination, second.declination)
    }
    */
  }
}


export class drawingMetod {

  constructor(private ctx: CanvasRenderingContext2D) { }

  dataglobal:any
  Fill_circle(r: number, x: number, y: number) {
    this.ctx.beginPath();
    this.ctx.arc(x, y, r, 0, 2 * Math.PI);
    this.ctx.fillStyle = "white";
    this.ctx.fill();
    this.ctx.stroke();
  }

  Line(Sx: number, Sy: number, Ex: number, Ey: number) {
    this.ctx.beginPath();
    this.ctx.moveTo(Sx, Sy);
    this.ctx.lineTo(Ex, Ey);
    this.ctx.strokeStyle = "white";
    this.ctx.lineWidth = 3;
    this.ctx.stroke();
  }

  GetSearchValue(name: string) {
    let http = "http://127.0.0.1:5000/data-for-image/" + name;
    let data: any = [];
    fetch(http).then(function (response) {
      return response.json();
    }).then(function (myJson) {
      data = myJson
      return data
    })
  }

  GetSearchStar(name: string) {
    let http = "http://127.0.0.1:5000/get_one_star/" + name;
    let data: any = [];
    fetch(http).then(function (response) {
      return response.json();
    }).then(function (myJson) {
      data = myJson
      return data
    })
  }
}

