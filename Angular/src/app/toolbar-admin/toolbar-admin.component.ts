import { Component, OnInit } from '@angular/core';
import { UserService } from '../_services/user.service';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-toolbar-admin',
  templateUrl: './toolbar-admin.component.html',
  styleUrls: ['./toolbar-admin.component.scss']
})
export class ToolbarAdminComponent implements OnInit {
  
  constructor(private tokenStorageService: TokenStorageService) { }

  ngOnInit(): void {
    if(this.tokenStorageService.getToken() == null){
      window.location.replace("/")
    }
  }

  logout(): void {
    this.tokenStorageService.isLoggedIn = false;
    this.tokenStorageService.signOut();
    window.location.reload();
  }
}
