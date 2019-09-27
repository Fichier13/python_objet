import re
with open("/users/mmath/echange/odyssey.txt","r") as f:
    motif=re.compile("\w+")
    mots=[]
    for ligne in f:
       
        l=motif.findall(ligne)
        for mot in l:
                mots.append(mot)
        print(mots)
            
        
        
    
 