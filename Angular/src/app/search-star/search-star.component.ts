import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api.service';

const STAR = "";

@Component({
  selector: 'app-search-star',
  templateUrl: './search-star.component.html',
  styleUrls: ['./search-star.component.scss']
})
export class SearchStarComponent implements OnInit {

  errorMessage = "";
  noStar = false;
  starData !: any;
  constructor(private api: ApiService, private router: Router) {
  }
  ngOnInit(): void {
  }

  getStar(name: string) {
    this.api.getStarByName(name).subscribe(res => {
      if (res == null) {
        this.errorMessage = "Bląd wyszukania gwiazdy"
      } else {
        this.starData = res;
      }
    })
  }
  moreInfo(row:any) {
    this.api.STAR = row;
    this.router.navigate(['/star-more-info']);
  }
}