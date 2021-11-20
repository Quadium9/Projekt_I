import { Component, OnInit } from '@angular/core';
import { ApiService } from '../shared/api.service';

@Component({
  selector: 'app-constellation-info',
  templateUrl: './constellation-info.component.html',
  styleUrls: ['./constellation-info.component.scss']
})
export class ConstellationInfoComponent implements OnInit {

  drawingdata !: any;

  constructor(private api: ApiService) { }

  ngOnInit(): void {
  }
}
