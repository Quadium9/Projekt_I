import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api.service';

@Component({
  selector: 'app-constellation-list',
  templateUrl: './constellation-list.component.html',
  styleUrls: ['./constellation-list.component.scss']
})
export class ConstellationListComponent implements OnInit {

  constellationdata !: any;

  constructor(private api: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.getConst()
  }

  getConst(){
    this.api.allconstellations().subscribe(res=>{
      this.constellationdata = res;
    })
  }
  moreInfo(row:any) {
    this.api.CONSTELLATION = row;
    this.router.navigate(['/constellation-more-info']);
  }
}
