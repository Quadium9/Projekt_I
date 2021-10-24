import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login-system',
  templateUrl: './login-system.component.html',
  styleUrls: ['./login-system.component.scss']
})
export class LoginSystemComponent implements OnInit {

  constructor(private http:HttpClient ) {}
  url = "http://127.0.0.1:5000/login-system"

  ngOnInit(): void {
  }

  Getlogin(data:any){
    console.log(data)
    this.http.post(this.url, data).subscribe((result)=>{
      console.log(result)
    })
    return this.http.post(this.url, data)
  }
}