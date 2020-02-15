num=int(input("Digite um número inteiro:"))
s=0
while(num>0):
    r=num%10
    num=num//10
    s=s+r
print(s)
