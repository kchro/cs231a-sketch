Feature eye1;
Feature eye2;
Feature nose;
Feature mouth;
Outline face1;
float face_x = 100;
float face_y = 100;
float face_w = 400;
float face_h = 400;
float drag = 30.0;

void setup() {
  size(600, 600);
  background(255, 255, 255);
  frameRate(5);
  float eye_x = face_x + (face_w / 3.0);
  float eye_y = face_y + (face_w / 5.0);
  eye1 = new Feature("eye/eye_", 4, eye_x, eye_y,int(face_w / 5));
  eye2 = new Feature("eye/eye_", 4, eye_x + (face_w / 3.0), eye_y,int(face_w / 5));
  nose = new Feature("nose/nose_", 4, eye_x + (face_w / 6.0), eye_y + (face_w / 6.0),int(face_w / 5));
  mouth = new Feature("mouth/mouth_", 4, eye_x + (face_w / 8.0), eye_y + (face_w / 3.0),int(face_w / 5));
  face1 = new Outline("outline/face_", 1, face_x, face_y,int(face_w));
}

void draw() { 
  background(255, 255, 255);
  if (int(frameCount / 10) % 4 == 0){
    face_h -= 10;
    face_x += -2;
    face_y += -4;
  }else if(int(frameCount / 10) % 3 == 0){
    face_h += 10;
    face_x += 3;
    face_y += 2;
  }else if(int(frameCount / 10) % 2 == 0){
    face_h -= 10;
    face_x += 3;
    face_y += -1;
  }else{
    face_h += 10;
    face_x += -2;
    face_y += 1;
  }
  
  //add quadratics to introduce rotation
  float eye_x1 = face_x + (face_w / 3.0);
  float eye_x2 = face_x + (face_w / 6.0);
  float eye_y = face_y + (face_h / 5.0);
  float nose_x = face_x + (face_w / 4.5);
  float nose_y = face_y + (face_h / 3.0);
  float mouth_x = face_x + (face_w / 4.0);
  float mouth_y = face_y + (face_h / 1.5);
  
  //face1.display_move(dx,dy);
  nose.display_pos(nose_x, nose_y);
  mouth.display_pos(mouth_x, mouth_y);
  eye1.display_pos(eye_x1,eye_y);
  eye2.display_pos(eye_x2,eye_y);
  
  saveFrame("demo/####.png");
  
}
