float dt = 0.01;
float g = 9.81;
int originalScale;
int SCALE = 50, SPEEDUP = 2;

ArrayList<Pendulum> pendulums = new ArrayList<Pendulum>();
float xOrigin = 0, yOrigin = 0;

void setup()
{
  size(600, 600);
  originalScale = SCALE;
  colorMode(HSB, 360, 100, 100);
  float[] angles = new float[]{PI/4, PI/3, PI/2.5, PI/2.2, PI/2, PI/1.5};
  float[] lengths = new float[]{1, 1, 1, 1, 1, 1};
  float[] masses = new float[]{0.9, 1, 0.9, 1, 0.9, 1};
  
  int pends = 50;
  
  float hueStep = 360.0 / pends;

  for(int i = 0; i < pends; i++)
  {
    for(int j = 0; j < angles.length; j++)
      angles[j] += 0.0001;
     pendulums.add(new Pendulum(6, angles, lengths, masses, color(i*hueStep, 80, 70)));
  }
}

void mouseDragged()
{
  if(mouseButton == RIGHT)
    return;
  float dx = mouseX - pmouseX;
  xOrigin += dx;
  float dy = mouseY - pmouseY;
  yOrigin += dy;
}

void mouseWheel(MouseEvent event) {
  float e = event.getCount();
  if (e>0)
  {
    SCALE--;
  }
  else if (e < 0)
  {
    SCALE++;
  }
}

void draw() {
  background(0);
  stroke(255);
  for(int i = 0; i < SPEEDUP; i++){
      for(Pendulum p: pendulums)
        p.step();
  }
  translate(width/2 + xOrigin, height/2 + yOrigin);
  
  for(Pendulum p: pendulums)
        p.render();
}
