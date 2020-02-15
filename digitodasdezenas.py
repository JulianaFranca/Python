x=int(input("Digite um número inteiro:"))
unidade=x%10
x=(x-unidade)//10
dezena=x%10
print("O dígito das dezenas é",dezena)
