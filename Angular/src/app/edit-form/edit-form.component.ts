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

  ngOnInit(): void {
    if (this.tokenStorage.getToken() == null) {
      window.location.replace("/login-system")
    }
    if (this.api.STAR == null){
      this.router.navigate(['/form-list']);
    }
    this.createfrom()
  }

  createfrom(){
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
    this.firstname = this.tokenStorage.getUser()[0].firstname;
    this.lastname = this.tokenStorage.getUser()[0].lastname;
  }

  postStarDetails() {
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
      alert("Nazwa jest wymagana");
      return 0;
    }
    if (this.formValue.value.inputrecth == null || this.formValue.value.inputrectm == null || this.formValue.value.inputrects == null) {
      alert("Rektascencja jest wymagana");
      return 0;
    }
    if (this.formValue.value.inputdeclh == null || this.formValue.value.inputdeclm == null || this.formValue.value.inputdecls == null) {
      alert("Deklinacja jest wymagana");
      return 0;
    }
    if (this.formValue.value.inputconstellation == null) {
      alert("Gwiazdozbiór jest wymagany");
      return 0;
    }
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
