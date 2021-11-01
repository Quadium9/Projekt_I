import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators'


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public STAR:any;

  constructor(private httpclient: HttpClient) { }

  url_add_star = "http://127.0.0.1:5000/add_new_star"
  url_get_Star_by_name = "http://127.0.0.1:5000/get_one_star_by_name/"

  postAddStar(data: any){
    return this.httpclient.post<any>(this.url_add_star, data).pipe(map((res:any)=>{
      return res;
    }))
  }
  getStarByName(data: string){
    return this.httpclient.get<any>(this.url_get_Star_by_name + data).pipe(map((res:any)=>{
      return res;
    }))
  }
}
