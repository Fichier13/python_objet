import math
class TrianglePascal:
    def __init__(self,n):
      self.n = n

        
        
    def trace(self):
        
      
        
        result = []  
        for count in range(self.n): 
            row = [] 
            for element in range(count + 1): 
                
                res=int((math.factorial(count)) / ((math.factorial(element)) * math.factorial(count -element)))
                
                row.append(res)
               
                
            result.append(row)
            print(row)
            
       
         
        return result
    
    
  
        
         
        
         

 



t=TrianglePascal(9)
t.trace()

