import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DrawConstComponent } from './draw-const.component';

describe('DrawConstComponent', () => {
  let component: DrawConstComponent;
  let fixture: ComponentFixture<DrawConstComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DrawConstComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DrawConstComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
