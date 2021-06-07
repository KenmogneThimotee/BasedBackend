import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-file-select',
  templateUrl: './file-select.component.html',
  styleUrls: ['./file-select.component.css']
})
export class FileSelectComponent implements OnInit {

  url : string ;
  constructor() {
    this.url = '' ;
   }

  ngOnInit(): void {
  }

  name = 'Angular 4';
 
  onSelectFile(event) {
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();

      reader.readAsDataURL(event.target.files[0]); // read file as data url

      reader.onload = (event) => { // called once readAsDataURL is completed
        this.url = event.target.result;
      }
    }
  }

}
