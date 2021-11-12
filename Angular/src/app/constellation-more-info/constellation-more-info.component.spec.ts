import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConstellationMoreInfoComponent } from './constellation-more-info.component';

describe('ConstellationMoreInfoComponent', () => {
  let component: ConstellationMoreInfoComponent;
  let fixture: ComponentFixture<ConstellationMoreInfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConstellationMoreInfoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConstellationMoreInfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
