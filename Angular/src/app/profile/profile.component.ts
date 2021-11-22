import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ApiService } from '../shared/api.service';
import { AuthService } from '../_services/auth.service';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  currentUser: any;
  click: boolean = false;
  errorMessage: string = "";
  error: boolean = false;
  usernamenull: boolean = false;
  passwordoldnull: boolean = false;
  passwordnewnull: boolean = false;
  passwordoldmin: boolean = false;
  passwordnewmin: boolean = false;

  constructor(private token: TokenStorageService, private formBuilder: FormBuilder, private api: ApiService) { }

  ngOnInit(): void {
    if (this.token.getToken() == null) {
      window.location.replace("/")
    }
    this.currentUser = this.token.getUser()[0];
  }

  upclick() {
    this.click = !this.click;
    this.errorMessage = "";
    this.error = false;
  }

  updateuser(username, passwordold, passwordnew) {
    if (username == "" || passwordold == "" || passwordnew == "") {
      this.error = !this.error;
    } else {
      let data = {
        id: this.currentUser.id,
        username: username,
        passwordold: passwordold,
        passwordnew: passwordnew
      }
      this.api.updateuser(JSON.parse(JSON.stringify(data))).subscribe(res => {
        if (res.result) {
          this.click = !this.click;
          this.errorMessage = res.message;
        } else {
          this.errorMessage = res.message;
        }
      })
    }
  }
}
