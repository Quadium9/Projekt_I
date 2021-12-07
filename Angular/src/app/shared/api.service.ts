import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators'


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public STAR: any;
  public CONSTELLATION: any;

  constructor(private httpclient: HttpClient) { }

  url_add_star = "http://127.0.0.1:5000/star/dd_new_star/";
  url_get_Star_by_name = "http://127.0.0.1:5000/star/get_star_by_name/";
  url_get_form_list_NO = "http://127.0.0.1:5000/star/form-list-admin-NO/";
  url_get_form_list_YES = "http://127.0.0.1:5000/star/form-list-admin-YES/";
  url_delete_star = "http://127.0.0.1:5000/star/delete-star/";
  url_confirm_star = "http://127.0.0.1:5000/star/confirmed-star/";
  url_get_all_user = "http://127.0.0.1:5000/user/get-all-user/";
  url_admin_to_user = "http://127.0.0.1:5000/user/admin-to-user/";
  url_user_to_admin = "http://127.0.0.1:5000/user/user-to-admin/";
  url_edit_star = "http://127.0.0.1:5000/star/edit-star";
  url_all_constellations = "http://127.0.0.1:5000/constellation/all-constellations";
  url_update_user = "http://127.0.0.1:5000/user/update-user";
  url_constellation_image = "http://127.0.0.1:5000/constellation/constellation_image/";
  url_get_star_by_constellation = "http://127.0.0.1:5000/star/get_star_by_constellation/";
  url_get_user_by_name = "http://127.0.0.1:5000/user/get-user-by-name/";


  getUserByName(username:string, loged:string){
    return this.httpclient.get(this.url_get_user_by_name + username + "/" + loged).pipe(map((res:any) =>{
      return res;
    }))
  }
  postAddStar(data: any, username:string) {
    return this.httpclient.post<any>(this.url_add_star + username, data).pipe(map((res: any) => {
      return res;
    }))
  }
  getStarByName(data: string) {
    return this.httpclient.get<any>(this.url_get_Star_by_name + data).pipe(map((res: any) => {
      return res;
    }))
  }
  getFormListNO(data: string, nrpage: number) {
    return this.httpclient.get<any>(this.url_get_form_list_NO + data + '/' + nrpage).pipe(map((res: any) => {
      return res;
    }))
  }
  getFormListYES(data: string, nrpage: number) {
    return this.httpclient.get<any>(this.url_get_form_list_YES + data + '/' + nrpage).pipe(map((res: any) => {
      return res;
    }))
  }
  deletestar(data: any, username: string) {
    return this.httpclient.post(this.url_delete_star + username, data).pipe(map((res: any) => {
      return res;
    }))
  }
  confirmedstar(id: number, username: string) {
    return this.httpclient.get(this.url_confirm_star + id + '/' + username).pipe(map((res: any) => {
      return res;
    }))
  }
  getAllUser(data: string, nrpage: number) {
    return this.httpclient.get(this.url_get_all_user + data + '/' + nrpage).pipe(map((res: any) => {
      return res;
    }))
  }
  adminToUser(data: any, username: string) {
    return this.httpclient.post(this.url_admin_to_user + username, data).pipe(map((res: any) => {
      return res;
    }))
  }
  userToAdmin(data: any, username: string) {
    return this.httpclient.post(this.url_user_to_admin + username, data).pipe(map((res: any) => {
      return res;
    }))
  }
  editStar(data: any) {
    return this.httpclient.post(this.url_edit_star, data).pipe(map((res: any) => {
      return res;
    }))
  }
  allconstellations() {
    return this.httpclient.get(this.url_all_constellations).pipe(map((res: any) => {
      return res;
    }))
  }
  imageConstellations(data: string) {
    return this.httpclient.get(this.url_constellation_image + data).pipe(map((res: any) => {
      return res;
    }))
  }
  updateuser(data: any) {
    return this.httpclient.post(this.url_update_user, data).pipe(map((res: any) => {
      return res;
    }))
  }
  getstarbyconstellation(data:string){
    return this.httpclient.get(this.url_get_star_by_constellation + data).pipe(map((res:any) => {
      return res;
    }))
  }
}
