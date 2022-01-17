import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { StarModel } from '../search-star/search-star.model';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-edit-form',
  templateUrl: './edit-form.component.html',
  styleUrls: ['./edit-form.component.scss']
})
export class EditFormComponent implements OnInit {

  constructor(private tokenStorage: TokenStorageService, private formBuilder: FormBuilder, private api: ApiService, private router: Router) { }

  form: any = {
    name: null,
    recth: null,
    rectm: null,
    rects: null,
  };
  formValue !: FormGroup;
  starModelObj: StarModel = new StarModel;
  firstname: string;
  lastname: string;

  // Error field
  nameNull: boolean = true;
  recNull: boolean = true;
  decNull: boolean = true;
  cosntellationNull: boolean = true;
  recError: boolean = true;
  decError: boolean = true;

  ngOnInit(): void {
    if (this.tokenStorage.getToken() == null) {
      window.location.replace("/login-system")
    }
    if (this.api.STAR == null) {
      this.router.navigate(['/form-list']);
    }
    this.createfrom()
  }

  createfrom() {
    console.log(this.api.STAR)
    this.formValue = this.formBuilder.group({
      inputname: this.api.STAR.name,
      inputrecth: this.api.STAR.rectascensionh,
      inputrectm: this.api.STAR.rectascensionm,
      inputrects: this.api.STAR.rectascensions,
      inputdeclh: this.api.STAR.declinationh,
      inputdeclm: this.api.STAR.declinationm,
      inputdecls: this.api.STAR.declinations,
      inputconstellation: this.api.STAR.constellation_name,
      inputtype: this.api.STAR.star_type,
      inputspeed: this.api.STAR.radial_speed,
      inputdistance: this.api.STAR.distance,
      inputbrightness: this.api.STAR.brightness,
      inputmass: this.api.STAR.mass
    })
    this.firstname = this.api.STAR.discaverer_name
    this.lastname = this.api.STAR.discaverer_lastname
  }

  postStarDetails() {
    this.nameNull = true;
    this.recNull = true;
    this.decNull = true;
    this.recError = true;
    this.decError = true;
    this.cosntellationNull = true;
    this.starModelObj.id = this.api.STAR.id;
    this.starModelObj.name = this.formValue.value.inputname;
    this.starModelObj.brightness = this.formValue.value.inputbrightness;
    this.starModelObj.constellation = this.formValue.value.inputconstellation;
    this.starModelObj.declinationh = this.formValue.value.inputdeclh;
    this.starModelObj.declinationm = this.formValue.value.inputdeclm;
    this.starModelObj.declinations = this.formValue.value.inputdecls;
    this.starModelObj.rectascensionh = this.formValue.value.inputrecth;
    this.starModelObj.rectascensionm = this.formValue.value.inputrectm;
    this.starModelObj.rectascensions = this.formValue.value.inputrects;
    this.starModelObj.distance = this.formValue.value.inputdistance;
    this.starModelObj.discavererid = this.tokenStorage.getUser()[0].id
    this.starModelObj.mass = this.formValue.value.inputmass;
    this.starModelObj.radial_speed = this.formValue.value.inputspeed;
    this.starModelObj.star_type = this.formValue.value.inputtype;
    this.starModelObj.username = this.tokenStorage.getUser()[0].username

    if (this.formValue.value.inputname == null) {
      this.nameNull = false;
    }
    if (this.formValue.value.inputrecth == null || this.formValue.value.inputrectm == null || this.formValue.value.inputrects == null) {
      this.recNull = false;
    }
    if (this.formValue.value.inputdeclh == null || this.formValue.value.inputdeclm == null || this.formValue.value.inputdecls == null) {
      this.decNull = false;
    }
    if (this.formValue.value.inputconstellation == null || this.formValue.value.inputconstellation == "Podaj nazwę gwiazdozbioru") {
      this.cosntellationNull = false;
    }
    if (this.formValue.value.inputrecth == 24 && (this.formValue.value.inputrectm > 0 || this.formValue.value.inputrects > 0)){
      this.recError = false;
    }
    if (this.formValue.value.inputrecth > 24 || this.formValue.value.inputrectm > 60 || this.formValue.value.inputrects > 60){
      this.recError = false;
    }
    if (this.formValue.value.inputrecth < 0 || this.formValue.value.inputrectm < 0 || this.formValue.value.inputrects < 0){
      this.recError = false;
    }
    if (this.formValue.value.inputdeclh > 90 || this.formValue.value.inputdeclm > 60 || this.formValue.value.inputdecls > 60) {
      this.decError = false;
    } 
    if (this.formValue.value.inputdeclh < (-90) || this.formValue.value.inputdeclm < (-60) || this.formValue.value.inputdecls < (-60)) {
      this.decError = false;
    }
    if (this.formValue.value.inputdeclh == (-90) && (this.formValue.value.inputdeclm > 0 || this.formValue.value.inputdecls > 0)) {
      this.decError = false;
    }
    if (this.formValue.value.inputdeclh == 90 && (this.formValue.value.inputdeclm > 0 || this.formValue.value.inputdecls > 0)) {
      this.decError = false;
    }
    if (this.cosntellationNull && this.nameNull && this.decNull && this.recNull) {
      this.api.editStar(this.starModelObj).subscribe(res => {
        if (res.message) {
          alert(res.message);
          this.router.navigate['/form-list']
        } else {
          alert(res.message);
        }
      },
      )
    }
  }
}
