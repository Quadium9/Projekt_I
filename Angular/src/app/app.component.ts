import { Component } from '@angular/core';
import { TokenStorageService } from './_services/token-storage.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  private rules: string;
  isLoggedIn = this.tokenStorageService.isLoggedIn;
  showAdminBoard = false;
  showUserBoard = false;
  username?: string;

  constructor(private tokenStorageService: TokenStorageService) { }
  
  ngOnInit(): void {
    this.isLoggedIn = !!this.tokenStorageService.getToken();

    if (this.isLoggedIn) {
      const user = this.tokenStorageService.getUser();
      this.rules = user[0].rules;
      
      if (this.rules === 'admin'){
        this.showAdminBoard = true;
        console.log('admin');
      }
      if (this.rules === 'user'){
        console.log('user')
      }

      //this.showAdminBoard = this.rules.includes('admin');
      //this.showUserBoard = this.rules.includes('user');

      this.username = user.username;
    }
  }
  
  logout(): void {
    this.tokenStorageService.signOut();
    window.location.reload();
  }
}
