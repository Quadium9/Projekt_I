import { Component, OnInit } from '@angular/core';
import { AuthService } from '../_services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  form: any = {
    firstname: null,
    lastname: null,
    username: null,
    email: null,
    password: null,
    password2: null
  };

  //Error field
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.isSignUpFailed = false;
    const { firstname, lastname, username, email, password, password2 } = this.form;

    if (password != password2) {
      this.isSignUpFailed = true;
      this.errorMessage = "Hasła są niezgodne";
    }
    if (!this.isSignUpFailed) {
      this.authService.register(firstname, lastname, username, email, password).subscribe(
        data => {
          if (data.result == false) {
            this.isSignUpFailed = true;
            this.errorMessage = data.message;
          } else {
            this.isSuccessful = true;
          }
        },
        err => {
          this.errorMessage = err.error.message;
          this.isSignUpFailed = true;
        }
      );
    }
  }
}
