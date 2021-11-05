import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfirmedstarComponent } from './confirmedstar.component';

describe('ConfirmedstarComponent', () => {
  let component: ConfirmedstarComponent;
  let fixture: ComponentFixture<ConfirmedstarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConfirmedstarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfirmedstarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
