for(int x=0; x<H; x++) 
  for(int y=0; y<W; y++){ 
    out[x,y]=0; 
    for(int z=0; z<D; z++) 
      for(int i=-h/2; i<h/2; i++) 
        for(int j=-w/2; j<w/2; j++) 
           out[x,y] += T[x+i, y+j, z] * filter[i+h/2, j+w/2, z]; 
    out[x,y] = activation(out[x,y]);//функция активации 
  }
