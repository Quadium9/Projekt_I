import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-stars',
  templateUrl: './stars.component.html',
  styleUrls: ['./stars.component.scss']
})
export class StarsComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
   
interface Deserializable {
  getTypes(): Object;
}
class Member implements Deserializable {
  id: number;
  getTypes(){
    return {};
  }
}

class ExampleClass implements Deserializable {
  mainId: number;
  firstMember: Member;
  secondMemeber: Member;

  getTypes(){
    return {
      firstMember: Member,
      secondMember: Member
    };
  }
}

function deserialize(json, clazz) {
  var instance = new clazz(),
      types = instance.getTypes();

  for(var prop in json) {
      if(!json.hasOwnProperty(prop)) {
          continue;
      }

      if(typeof json[prop] === 'object') {
          instance[prop] = deserialize(json[prop], types[prop]);
      } else {
          instance[prop] = json[prop];
      }
  }

  return instance;
}

var json = {
  mainId: 42,
  firstMember: {
      id: 1337
  },
  secondMember: {
      id: -1
  }
};

var instance = deserialize(json, ExampleClass);
console.log(instance);
  }
}
