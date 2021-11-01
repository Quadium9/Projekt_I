import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoreInfoStarComponent } from './more-info-star.component';

describe('MoreInfoStarComponent', () => {
  let component: MoreInfoStarComponent;
  let fixture: ComponentFixture<MoreInfoStarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MoreInfoStarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MoreInfoStarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
