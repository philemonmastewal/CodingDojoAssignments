import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Retro Barcode Generator';
  colors = [ 'Aqua', 'Aquamarine', 'Cyan', 'DarkTurquoise', 'DeepSkyBlue', 'LightSkyBlue', 'MediumSpringGreen', 'MediumTurquoise', 'Turquoise', 'Blue' ]
  a: number = (Math.floor(Math.random() * 12)) +2;
  b: number = (Math.floor(Math.random() * 12)) +2;
  c: number = (Math.floor(Math.random() * 12)) +2;
  d: number = (Math.floor(Math.random() * 12)) +2;
  e: number = (Math.floor(Math.random() * 12)) +2;
  f: number = (Math.floor(Math.random() * 12)) +2;
  g: number = (Math.floor(Math.random() * 12)) +2;
  h: number = (Math.floor(Math.random() * 12)) +2;
  i: number = (Math.floor(Math.random() * 12)) +2;
  j: number = (Math.floor(Math.random() * 12)) +2;
  k: number = (Math.floor(Math.random() * 12)) +2;

}
