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

  ngOnInit(): void {
    this.ctx = this.canvas.nativeElement.getContext('2d');
    this.animate();
  }
  animate(): void {
    this.ctx.fillStyle = 'white';
    const DMetod = new drawingMetod(this.ctx);
    DMetod.Fill_circle(10, 100, 200);
    DMetod.Fill_circle(10, 300, 200);
    DMetod.Line(100,200,300,200);

  }
}

export class drawingMetod {

  constructor(private ctx: CanvasRenderingContext2D) { }

  Fill_circle(r: number, x: number, y: number) {
    this.ctx.beginPath();
    this.ctx.arc(x,y,r,0,2*Math.PI);
    this.ctx.fillStyle = "white";
    this.ctx.fill();
    this.ctx.stroke();
  }

  Line(Sx:number, Sy:number, Ex:number, Ey:number){
    this.ctx.beginPath();
    this.ctx.moveTo(Sx,Sy);
    this.ctx.lineTo(Ex,Ey);
    this.ctx.strokeStyle ="white";
    this.ctx.lineWidth = 3;
    this.ctx.stroke();
  }
}

