liste = []
i=0
nombre=int(input("nombre d'entier a saisir :"))
while i<nombre:
  n=int(input("entre un nombre :"))
  liste.append(n)
  i=i+1
  
def findMax():
  return max(liste)
  
  
  

print(findMax())
  