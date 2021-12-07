import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

const AUTH_API = "http://127.0.0.1:5000/user/"

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    return this.http.post(AUTH_API + 'login-system',{
      username,
      password
    }, httpOptions);
  }

  register(firstname: string, lastname: string, username: string, email: string, password: string): Observable<any> {
    return this.http.post(AUTH_API + 'register-user', {
      firstname,
      lastname,
      username,
      email,
      password
    }, httpOptions);
  }
}
