

def disect_float(f):
      f = float(f); #fixes passing integers
      sign = 0x00; #positive
      exp = 0;
      mant = 0;
      if(f < 0): #make f positive, store the sign
        sign = '-'; #negative
        f = -f;
      #get the mantissa by itself
      while(f % 1 > 0): #exp is positive
        f*=2
        exp+=1
      #while(f % 1 > 0):
      tf = f/2;
      while(tf % 1 <= 0): #exp is negative
        exp-=1;
        f=tf;
        tf=f/2;
        if(exp < -1024): break;
      mant=int(f);
      return sign, mant-1, exp;

print disect_float(7.0)
