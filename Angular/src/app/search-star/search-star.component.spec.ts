import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchStarComponent } from './search-star.component';

describe('SearchStarComponent', () => {
  let component: SearchStarComponent;
  let fixture: ComponentFixture<SearchStarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchStarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchStarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
