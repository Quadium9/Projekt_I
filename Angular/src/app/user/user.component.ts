import { Component, OnInit } from '@angular/core';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';

let x = 1

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {

  userData !: any;
  endData: boolean = false;
  message: string = null;

  constructor(private api: ApiService, private tokenStorage: TokenStorageService) { }

  ngOnInit(): void {
    x = 1
    if (this.tokenStorage.getToken() == null) {
      window.location.replace("/login-system")
    } else {
      this.getUser()
    }
  }

  getUser() {
    this.api.getAllUser(this.tokenStorage.getUser()[0].username, 1).subscribe(res => {
      if (res.result) {
        alert(res.message);
      } else {
        this.userData = res;
      }
    })
  }
  nextpage() {
    this.endData = false
    let page = x + 1
    x = x + 1
    this.api.getAllUser(this.tokenStorage.getUser()[0].username, page).subscribe(res => {
      if (res.result == false) {
        alert(res.message);
        x = 1
      } else {
        if (res[0] == null) {
          this.message = "Koniec danych"
          this.endData = true;
        }
        this.userData = res;
      }
    })
  }
  previouspage() {
    this.message = null;
    this.endData = false
    let page = x - 1
    x = x - 1
    this.api.getAllUser(this.tokenStorage.getUser()[0].username, page).subscribe(res => {
      if (res.result == false) {
        alert(res.message);
        x = 1
      } else {
        this.userData = res;
      }
    })
  }

  userToAdmin(row: any) {
    this.api.userToAdmin(row, this.tokenStorage.getUser()[0].username).subscribe(res => {
      alert(res.message)
      this.getUser()
    })
  }

  adminToUser(row: any) {
    this.api.adminToUser(row, this.tokenStorage.getUser()[0].username).subscribe(res => {
      alert(res.message)
      this.getUser()
    })
  }

  searchUser(name) {
    if (name == "") {
      alert("Proszę wpisać nazwę użytkownika");
    } else {
      this.api.getUserByName(name, this.tokenStorage.getUser()[0].username).subscribe(res => {
        if (res.result) {
          this.message = res.message;
        } else {
          this.userData = res;
        }
      })
    }
  }
}
