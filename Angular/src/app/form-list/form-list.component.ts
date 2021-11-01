import { Component, OnInit } from '@angular/core';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-form-list',
  templateUrl: './form-list.component.html',
  styleUrls: ['./form-list.component.scss']
})
export class FormListComponent implements OnInit {

  constructor(private tokenStorage: TokenStorageService) {}

  ngOnInit(): void {
    if(this.tokenStorage.getToken() == null){
      window.location.replace("/")
    }
  }

}
