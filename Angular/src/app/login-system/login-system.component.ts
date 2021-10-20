import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login-system',
  templateUrl: './login-system.component.html',
  styleUrls: ['./login-system.component.scss']
})
export class LoginSystemComponent implements OnInit {

  constructor() { }
  private login:string;
  private http:HttpClient;
  private password:string;


  ngOnInit(): void {
  }

  Getlogin(login:string, password:string){
    console.log(login, password)
    let http = "http://127.0.0.1:5000/login-system/user-login=" + login +"&user-password="+ password;
    let data: any = [];
    fetch(http).then(function (response) {
      return response.json();
    }).then(function (myJson) {
      data = myJson
      console.log(data)
    })
  }
}
