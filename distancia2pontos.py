import math

x=float(input("Digite o valor de x:"))
y=float(input("Digite o valor de y:"))
x1=float(input("Digite o valor de x1:"))
y1=float(input("Digite o valor de y1:"))

distancia=math.sqrt((x-x1)**2 + (y-y1)**2)

if(distancia>=10):
    print("longe")
else:
    print("perto")
