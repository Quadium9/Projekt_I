import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';

const STAR = "";

@Component({
  selector: 'app-confirmedstar',
  templateUrl: './confirmedstar.component.html',
  styleUrls: ['./confirmedstar.component.scss']
})
export class ConfirmedstarComponent implements OnInit {

  errorMessage = "";
  noStar = false;
  starData !: any;

  constructor(private api: ApiService, private router: Router, private tokenStorage:TokenStorageService) { }

  ngOnInit(): void {
    if(this.tokenStorage.getToken() == null){
      window.location.replace("/")
    }else{
      this.getStar()
    }
  }
  getStar() {
    this.api.getFormListYES().subscribe(res => {
      if (res == null) {
        this.errorMessage = "Bląd wyszukiwania"
      } else {
        this.starData = res;
      }
    })
  }

  moreInfo(row:any) {
    this.api.STAR = row;
    this.router.navigate(['/star-more-info']);
  }

  deletestar(row:any){
    this.api.deletestar(row).subscribe(res=>{
      if(res.result){
        alert(res.message)
        this.getStar()
      }else{
        alert(res.message)
      }
    })
  }

  edit(row:any){
    this.api.STAR = row;
    this.router.navigate(['/edit-form']);
  }
}
