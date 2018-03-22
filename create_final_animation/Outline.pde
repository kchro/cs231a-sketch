
class Outline{
  PImage[] images;
  float xpos;
  float ypos;
  int imageCount;
  int frame; //image frame
  
  Outline(String file, int count, float x, float y, int w) {
    xpos = x;
    ypos = y;
    imageCount = count;
    images = new PImage[imageCount];
    for (int i = 0; i < imageCount; i++) {
      String filename = file + str(i) + ".png";
      PImage temp_img = loadImage(filename);
      int h_factor = ((w / temp_img.width) * temp_img.height);
      temp_img.resize(w,h_factor);
      images[i] = temp_img;
    }
  }
  void display_move(float dx, float dy) {
    frame = (frame+1) % imageCount;
    image(images[frame], xpos, ypos);
    move(dx, dy);
  }
  
  void display_pos(float x, float y) {
    frame = (frame+1) % imageCount;
    image(images[frame], x, y);
    xpos = x;
    ypos = y;
  }

  void display() {
    frame = (frame+1) % imageCount;
    image(images[frame], xpos, ypos);
  }
  
  
  void move(float dx, float dy) {
    xpos += dx;
    ypos += dy;
  }
  
  int getWidth() {
    return images[0].width;
  }
  
  int getHeight() {
    return images[0].height;
  }

}