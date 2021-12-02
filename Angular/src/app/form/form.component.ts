import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { StarModel } from '../search-star/search-star.model';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.scss']
})
export class FormComponent implements OnInit {

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

  constructor(private tokenStorage: TokenStorageService, private formBuilder: FormBuilder, private api: ApiService) { }

  ngOnInit(): void {
    if (this.tokenStorage.getToken() == null) {
      window.location.replace("/login-system")
    }
    this.formValue = this.formBuilder.group({
      inputname: null,
      inputrecth: null,
      inputrectm: null,
      inputrects: null,
      inputdeclh: null,
      inputdeclm: null,
      inputdecls: null,
      inputconstellation: null,
      inputtype: ['Unknown'],
      inputspeed: [''],
      inputdistance: [''],
      inputbrightness: [''],
      inputmass: ['']
    })
    this.firstname = this.tokenStorage.getUser()[0].firstname;
    this.lastname = this.tokenStorage.getUser()[0].lastname;
  }

  postStarDetails() {
    this.nameNull = true;
    this.recNull = true;
    this.decNull = true;
    this.recError = true;
    this.decError = true;
    this.cosntellationNull = true;
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
    this.starModelObj.discavererid = this.tokenStorage.getUser()[0].id;
    this.starModelObj.mass = this.formValue.value.inputmass;
    this.starModelObj.radial_speed = this.formValue.value.inputspeed;
    this.starModelObj.star_type = this.formValue.value.inputtype;
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
    if (this.formValue.value.inputrecth == 24 && this.formValue.value.inputrectm > 0 || this.formValue.value.inputrects > 0){
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
    if (this.formValue.value.inputdeclh == (-90) && this.formValue.value.inputdeclm > 0 || this.formValue.value.inputdecls > 0) {
      this.decError = false;
    }
    if (this.formValue.value.inputdeclh == 90 && this.formValue.value.inputdeclm > 0 || this.formValue.value.inputdecls > 0) {
      this.decError = false;
    }
    if (this.cosntellationNull && this.nameNull && this.decNull && this.recNull) {
      this.api.postAddStar(this.starModelObj, this.tokenStorage.getUser()[0].username).subscribe(res => {
        if (res.result) {
          alert("Wysłano formularz o nowej gwieżdzie");
          this.formValue.reset();
        } else {
          alert(res.message)
        }
      },
      )
    }
  }
}
