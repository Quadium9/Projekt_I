import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators'


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public STAR:any;

  constructor(private httpclient: HttpClient) { }

  url_add_star = "http://127.0.0.1:5000/add_new_star";
  url_get_Star_by_name = "http://127.0.0.1:5000/get_one_star_by_name/";
  url_get_form_list_NO = "http://127.0.0.1:5000/form-list-admin-NO";
  url_get_form_list_YES = "http://127.0.0.1:5000/form-list-admin-YES";
  url_delete_star = "http://127.0.0.1:5000/delete-star";
  url_confirm_star = "http://127.0.0.1:5000/confirmed-star/";
  url_get_all_user = "http://127.0.0.1:5000/get-all-user";
  url_admin_to_user = "http://127.0.0.1:5000/admin-to-user";
  url_user_to_admin = "http://127.0.0.1:5000/user-to-admin";
  url_edit_star = "http://127.0.0.1:5000/edit-star";

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
  getFormListNO(){
    return this.httpclient.get<any>(this.url_get_form_list_NO).pipe(map((res:any)=>{
      return res;
    }))
  }
  getFormListYES(){
    return this.httpclient.get<any>(this.url_get_form_list_YES).pipe(map((res:any)=>{
      return res;
    }))
  }
  deletestar(data: any){
    return this.httpclient.post(this.url_delete_star, data).pipe(map((res:any)=>{
      return res;
    }))
  }
  confirmedstar(id: number){
    return this.httpclient.get(this.url_confirm_star + id).pipe(map((res:any)=>{
      return res;
    }))
  }
  getAllUser(){
    return this.httpclient.get(this.url_get_all_user).pipe(map((res:any)=>{
      return res;
    }))
  }
  adminToUser(data: any){
    return this.httpclient.post(this.url_admin_to_user, data).pipe(map((res:any)=>{
      return res;
    }))
  }
  userToAdmin(data: any){
    return this.httpclient.post(this.url_user_to_admin, data).pipe(map((res:any)=>{
      return res;
    }))
  }
  editStar(data: any){
    return this.httpclient.post(this.url_edit_star, data).pipe(map((res:any)=>{
      return res;
    }))
  }
}
