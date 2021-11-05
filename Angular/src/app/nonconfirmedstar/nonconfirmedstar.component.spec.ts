import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NonconfirmedstarComponent } from './nonconfirmedstar.component';

describe('NonconfirmedstarComponent', () => {
  let component: NonconfirmedstarComponent;
  let fixture: ComponentFixture<NonconfirmedstarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NonconfirmedstarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NonconfirmedstarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
