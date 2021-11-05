import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-nonconfirmedstar',
  templateUrl: './nonconfirmedstar.component.html',
  styleUrls: ['./nonconfirmedstar.component.scss']
})
export class NonconfirmedstarComponent implements OnInit {

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
    this.api.getFormListNO().subscribe(res => {
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

  confirmedstar(row:any) {
    this.api.confirmedstar(row.id).subscribe(res=>{
      if (res.result){
        alert(res.message);
        this.getStar()
      }else{
        alert(res.message);
      }
    })
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
}
