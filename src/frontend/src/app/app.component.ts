import { Component, OnInit } from '@angular/core';
import { environment } from '../environments/environments';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  ngOnInit() {
    (window as any).alkaliInitData = environment.alkaliInitData;
    // const script = document.createElement('script');
    // script.src = 'src/assets/styles/263a44e27250fde14e9f38b59415f9f6b10169e6.js';
    // document.body.appendChild(script);
    const script = document.createElement('script');
    script.src = 'assets/styles/263a44e27250fde14e9f38b59415f9f6b10169e6.js';
    document.body.appendChild(script);
  }
}
