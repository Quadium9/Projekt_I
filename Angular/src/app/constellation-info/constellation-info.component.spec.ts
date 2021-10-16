import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConstellationInfoComponent } from './constellation-info.component';

describe('ConstellationInfoComponent', () => {
  let component: ConstellationInfoComponent;
  let fixture: ComponentFixture<ConstellationInfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConstellationInfoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConstellationInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
