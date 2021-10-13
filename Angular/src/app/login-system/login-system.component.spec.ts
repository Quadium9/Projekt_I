import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginSystemComponent } from './login-system.component';

describe('LoginSystemComponent', () => {
  let component: LoginSystemComponent;
  let fixture: ComponentFixture<LoginSystemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginSystemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginSystemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
