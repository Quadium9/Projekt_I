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
    this.http.post('http://127.0.0.1:5000/login-system',JSON.parse(this.password))
   /* function httpCall(method:'user-data', url:'http://127.0.0.1:5000/login-system', data:any, callback:(result:any)=>any){
      var xhr = new XMLHttpRequest();
      xhr.open(method, url, true);
      if (callback) xhr.onload = function() { callback(JSON.parse(this[login],this[password])); };
      if (data != null) {
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify(data));
    }
      else xhr.send();
    }*/
  }
}
