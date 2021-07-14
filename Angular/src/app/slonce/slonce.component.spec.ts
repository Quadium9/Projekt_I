import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SlonceComponent } from './slonce.component';

describe('SlonceComponent', () => {
  let component: SlonceComponent;
  let fixture: ComponentFixture<SlonceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SlonceComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SlonceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
