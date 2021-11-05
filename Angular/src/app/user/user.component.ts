import { Component, OnInit } from '@angular/core';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';


@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {

  userData !: any;
  OBJ = "rules";

  constructor(private api: ApiService, private tokenStorage:TokenStorageService) { }

  ngOnInit(): void {
    if(this.tokenStorage.getToken() == null){
      window.location.replace("/")
    }else{
      this.getUser()
    }
  }

  getUser(){
    this.api.getAllUser().subscribe(res => {
      if (res.result){
        alert(res.message);
      }else {
        this.userData = res;
      }
    })
  }

  userToAdmin(row:any){
    this.api.userToAdmin(row).subscribe(res =>{
      alert(res.message)
      this.getUser()
    })
  }

  adminToUser(row:any){
    this.api.adminToUser(row).subscribe(res =>{
      alert(res.message)
      this.getUser()
    })
  }
}
