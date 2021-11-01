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
  starModelObj : StarModel = new StarModel;
  firstname:string;
  lastname:string;

  constructor(private tokenStorage: TokenStorageService, private formBuilder: FormBuilder, private api: ApiService) { }

  ngOnInit(): void {
    if(this.tokenStorage.getToken() == null){
      window.location.replace("/")
    }
    this.formValue =  this.formBuilder.group({
      inputname: [''],
      inputrecth: [''],
      inputrectm: [''],
      inputrects: [''],
      inputdeclh: [''],
      inputdeclm: [''],
      inputdecls: [''],
      inputconstellation: [''],
      inputtype: ['Unknown'],
      inputspeed: [''],
      inputdistance: [''],
      inputbrightness: [''],
      inputmass: ['']
    })
    this.firstname = this.tokenStorage.getUser()[0].firstname;
    this.lastname = this.tokenStorage.getUser()[0].lastname;
  }

  postStarDetails(){
    this.starModelObj.name = this.formValue.value.inputname;
    this.starModelObj.brightness = this.formValue.value.inputbrightness;
    this.starModelObj.constellation = this.formValue.value.inputconstellation;
    this.starModelObj.declination = this.formValue.value.inputdeclh + "h " + this.formValue.value.inputdeclm + "m " + this.formValue.value.inputdecls + "s";
    this.starModelObj.rectascension = this.formValue.value.inputrecth + "h " + this.formValue.value.inputrectm + "m " + this.formValue.value.inputrects + "s";
    this.starModelObj.distance = this.formValue.value.inputdistance;
    this.starModelObj.discavererid = this.tokenStorage.getUser()[0].id
    this.starModelObj.mass = this.formValue.value.inputmass;
    this.starModelObj.radial_speed = this.formValue.value.inputspeed;
    this.starModelObj.star_type = this.formValue.value.inputtype;

    console.log(this.starModelObj)
    this.api.postAddStar(this.starModelObj).subscribe(res=>{
      if(res.message){
        alert(res.message);
      }else{
      alert("Wysłano formularz o nowej gwieżdzie");
      this.formValue.reset();
    }
    }, 
   )
  }
}
