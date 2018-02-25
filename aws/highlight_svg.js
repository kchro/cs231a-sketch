// to get image_paths...
// in python
// >> import os
// >> ios.listdir('guitar')
// copy output and paste here
const image_paths = ['n02676566_307-1.svg', 'n02676566_307-2.svg', 'n02676566_307-3.svg']

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

let image_index = 0;

/**
 * load_next
 * ---------
 * button onclick function to load the next image
 */
function load_next() {
  console.log('image '+(image_index+1)+' out of '+image_paths.length);

  if (image_index > image_paths.length - 1) {
    console.log('no more images');
    return;
  }

  load_svg(image_paths[image_index]);
  image_index++;
}

/**
 * main
 */
load_next();
