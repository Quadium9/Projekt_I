import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../shared/api.service';
import { TokenStorageService } from '../_services/token-storage.service';


@Component({
  selector: 'app-form-list',
  templateUrl: './form-list.component.html',
  styleUrls: ['./form-list.component.scss']
})
export class FormListComponent implements OnInit {

  showconf: boolean = false;
  shownonconf: boolean = false;
  showsus: boolean = false;

  constructor( private tokenStorage:TokenStorageService) {}

  ngOnInit(): void {
    if(this.tokenStorage.getToken() == null){
      window.location.replace("/")
    }
    this.shownonconfirmed()
  }
  
  showconfirmed(){
    this.showconf = true;
    this.shownonconf = false;
    this.showsus = false;
  }
  shownonconfirmed(){
    this.showconf = false;
    this.shownonconf = true;
    this.showsus = false;
  }
  showuser(){
    this.showconf = false;
    this.shownonconf = false;
    this.showsus = true;
  }
}
