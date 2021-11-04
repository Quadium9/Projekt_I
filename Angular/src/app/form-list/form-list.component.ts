import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';

const STAR = "";

@Component({
  selector: 'app-form-list',
  templateUrl: './form-list.component.html',
  styleUrls: ['./form-list.component.scss']
})
export class FormListComponent implements OnInit {

  errorMessage = "";
  noStar = false;
  starData !: any;

  constructor(private http: HttpClient, private api: ApiService, private router: Router, private tokenStorage:TokenStorageService) {}

  ngOnInit(): void {
    if(this.tokenStorage.getToken() == null){
      window.location.replace("/")
    }
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
