class Pendulum {
  
 float[] thetas, lens;
 float[] old_thetas;
 int numBodies;
 float[] masses;
 color col;
 float sumOfMasses;
 
 Pendulum (int nBodies, float[] angles, float[] lengths, float[] masses, color c)
 {
   this.col = c;
   this.numBodies = nBodies;
   this.masses = new float[numBodies];
   this.thetas = new float[numBodies];
   this.old_thetas = new float[numBodies];
   this.lens = new float[numBodies];
   arrayCopy(masses, this.masses);
   arrayCopy(angles, this.thetas);
   arrayCopy(lengths, this.lens);
   arrayCopy(this.thetas, this.old_thetas);
   for(int i = 0; i < numBodies; i++)
     sumOfMasses += masses[i];
 }
 
 float getThetaDot(int index)
 {
   return this.thetas[index] - this.old_thetas[index];
 }
 
 float[][] getAccels()
 {
   float[][] R_matrix = new float[this.numBodies][1];
   float[][] coeff_matrix = new float[this.numBodies][this.numBodies];
    for (int w = 0; w < this.numBodies; w++){
      
        float Lambda_w = this.lens[w]*this.sumOfMasses;
        
        float F_w_sum = 0;
        float R_w_sum = 0;
        for(int i = 0; i < this.numBodies; i++)
        {
          for(int j = 0; j < i; j++)
          {
            F_w_sum += this.masses[i]*this.lens[j]*getThetaDot(j)*sin(this.thetas[j]-this.thetas[w]);
            if(j != w)
              R_w_sum += this.masses[i]*this.lens[j]*getThetaDot(j)*(getThetaDot(j) - getThetaDot(w))*sin(this.thetas[j]-this.thetas[w]);
          }
        }
        float F_w = getThetaDot(w)*F_w_sum - g*sin(this.thetas[w])*this.sumOfMasses;
        float R_w = F_w + R_w_sum;
        R_matrix[w][0] = R_w;
        
        float[] matrix_row = new float[this.numBodies];
        
        for (int k = 0; k < this.numBodies; k++){
            if(k == w){
                matrix_row[k] = Lambda_w;
                continue;
            }
            matrix_row[k] = lens[k]*cos(this.thetas[k] - this.thetas[w])*(sumOfMasses - this.masses[w]);
        }
        
        coeff_matrix[w] = matrix_row;
    }
    float[][] output = multiplyMatrices(invertMatrix(coeff_matrix), R_matrix); //Inverse
    return output;
 }
 
 void step()
 {
   float[][] accels = getAccels();
   for(int i = 0; i < thetas.length; i++)
   {
     step_verlet(i, accels[i][0]);
   }
 }
 
 void step_verlet(int index, float theta_accel)
 {   
   float vel_x = getThetaDot(index);

   this.old_thetas[index] = this.thetas[index];

   this.thetas[index] += vel_x + theta_accel * dt*dt;
 }
  
 void step_semiimplicit()
 {
   
 }
 
 void step_rungekutta()
 {
   
 }
 
 void render()
 {

   stroke(col);
   beginShape();
   vertex(0, 0);
   float prev_x = 0;
   float prev_y = 0;
   for(int i = 0; i < this.numBodies; i++)
   {
     float xPos = prev_x + lens[i]*sin(thetas[i])*SCALE;
     float yPos = prev_y + lens[i]*cos(thetas[i])*SCALE;
     prev_x = xPos;
     prev_y = yPos;
     vertex(xPos, yPos);
     fill(255);
     circle(xPos,  yPos, SCALE*5/originalScale);
     noFill();
   }
   endShape();
 }
 
}
