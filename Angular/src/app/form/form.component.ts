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

  
  constructor(private tokenStorage: TokenStorageService, private formBuilder: FormBuilder, private api: ApiService) { }

  ngOnInit(): void {
    if (this.tokenStorage.getToken() == null) {
      window.location.replace("/")
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
    console.log(this.starModelObj)
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
    this.api.postAddStar(this.starModelObj).subscribe(res => {
      if (res.result) {
        alert("Wysłano formularz o nowej gwieżdzie");
        this.formValue.reset();
      } else {
        alert(res.message);
      }
    },
    )
  }
}
