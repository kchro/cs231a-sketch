// to get image_paths...
// in python
// >> import os
// >> ios.listdir('guitar')
// copy output and paste here
const image_paths = ['n02676566_307-1.svg', 'n02676566_307-2.svg', 'n02676566_307-3.svg']

// global variable for indexing image
let image_index = -1;

/**
 * load_svg
 * --------
 * XMLHttpRequest to load SVG file dynamically into the DOM
 */
function load_svg(path) {
  let xhr = new XMLHttpRequest();
  xhr.open("GET","guitar_subset/"+path,false);
  // Following line is just to be on the safe side;
  // not needed if your server delivers SVG with correct MIME type
  xhr.overrideMimeType("image/svg+xml");
  xhr.send("");

  let container = document.getElementById("svgContainer");
  let svg = xhr.responseXML.documentElement;

  if (container.firstElementChild) {
    container.removeChild(container.firstElementChild);
  }

  container.appendChild(svg);
}

/**
 * print
 * -----
 * Print message at the console bar for client
 */
function print(str) {
  let btn_console = document.getElementById("console");
  btn_console.innerHTML = str;
}

/**
 * load_next
 * ---------
 * button onclick function to load the next image
 */
function load_prev() {
  if (image_index == 0) {
    print('no previous images');
    return;
  }

  image_index--;
  print('image '+(image_index+1)+' out of '+image_paths.length);
  load_svg(image_paths[image_index]);
}

/**
 * load_next
 * ---------
 * button onclick function to load the next image
 */
function load_next() {
  if (image_index == image_paths.length - 1) {
    print('no more images');
    return;
  }

  image_index++;
  print('image '+(image_index+1)+' out of '+image_paths.length);
  load_svg(image_paths[image_index]);
}
