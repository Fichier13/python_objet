import math

class Fraction:
   
   
    def __init__(self,num,den):
      self.num = num
      self.den = den

    
    
    def val(self):
        res=0
        if self.den==0:
            res=-1
            return res
        else:
            res=self.num/self.den
            return res
        
            
           
    
  
        
    def inverse(self):
         n=Fraction(self.num,self.den)
         n.num=self.den
         n.den=self.num
         return n
    def __str__(self):
        return f"{self.num}/{self.den}"
        
             
  
fraction=Fraction(12,89)
fraction.num=10
print(fraction.val())
inverse=fraction.inverse()
print(inverse.val())
print(inverse)