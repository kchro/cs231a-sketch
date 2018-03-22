Feature eye1;
Feature eye2;
Feature nose;
Feature mouth;
Outline face1;
PImage face_img;
float face_x = 100; // center of face
float face_y = 100; //center of face
float face_w = 300;
float face_h = 400;
float drag = 30.0;

void setup() {
  size(800, 800);
  background(255, 255, 255);
  frameRate(5);
  face_x = width / 2.0;
  face_y = height / 2.0;
  //tint(0,0,0);
  eye1 = new Feature("eye1/eye_", 78, face_x - (face_w / 4.0) - (face_w / 10.0), face_y - (face_h / 4.0) - (face_h / 10.0),int(face_w / 4));
  eye2 = new Feature("eye2/eye_", 78, face_x + (face_w / 4.0) - (face_w / 10.0), face_y - (face_h / 4.0) - (face_h / 10.0),int(face_w / 4));
  nose = new Feature("nose/nose_", 78, face_x - (face_w / 10.0), face_y - (face_h / 8.0) - (face_h / 10.0),int(face_w / 4));
  mouth = new Feature("mouth/mouth_", 78, face_x - (face_w / 10.0), face_y + (face_h / 4.0) - (face_h / 10.0),int(face_w / 4));
  face1 = new Outline("outline/face_", 1, face_x - (face_w/ 2.0), face_y  - (face_h/ 2.0),int(face_w));
  face_img = loadImage("outline/face_2.png");
}

void draw() { 
  background(255, 255, 255);
  if (int(frameCount / 10) % 4 == 0){
    face_h -= 10;
    face_w += 10;
    face_x += 0;
    face_y += 0;
  }else if(int(frameCount / 10) % 3 == 0){
    face_h += 10;
    face_x += 0;
    face_y += 0;
  }else if(int(frameCount / 10) % 2 == 0){
    face_h -= 10;
    face_w -= 10;
    face_x += 0;
    face_y += 0;
  }else{
    face_h += 10;
    face_x += 0;
    face_y += 0;
  }
  
  //add quadratics to introduce rotation
  float eye_x1 = face_x - (face_w / 4.0) - (face_w / 10.0);
  float eye_x2 = face_x + (face_w / 4.0) - (face_w / 10.0);
  float eye_y = face_y - (face_h / 4.0) - (face_h / 10.0);
  float nose_x = face_x - (face_w / 10.0);
  float nose_y = face_y - (face_h / 8.0) - (face_h / 10.0);
  float mouth_x = face_x - (face_w / 10.0);
  float mouth_y = face_y + (face_h / 4.0) - (face_h / 10.0);
  
  //face1.display_move(dx,dy);
  image(face_img,face_x - (face_w/ 2.0), face_y  - (face_h/ 2.0),face_w,face_h);
  nose.display_pos(nose_x, nose_y);
  mouth.display_pos(mouth_x, mouth_y);
  eye1.display_pos(eye_x1,eye_y);
  eye2.display_pos(eye_x2,eye_y);
  //face1.display_pos(face_x - (face_w/ 2.0), face_y  - (face_h/ 2.0));
  
  saveFrame("demo/####.png");
  
}