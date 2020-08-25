#Faça um programa que pergunte o preço de três produtos einforme
#qual produto você deve comprar,sabendo que a decisão é sempre pelo mais barato.
p1 = input("Digite o 1° preço: ")
p2 = input("Digite o 2° preço: ")
p3 = input("Digite o 3° preço: ")

if p1 < p2 and p1 < p3:
    print("O preço menor é o primeiro: ", p1)
elif p2 < p1 and  p2 < p3:
    print("O preço menor é o segundo: ", p2)
elif p3 < p1 and p3 < p2:
    print("O preço menor é o terceiro: ", p3)

elif p1 == p2 and p1 and p2 < p3:
    print ('O produto 1 e 2 são os mais baratos!!')
elif p1 == p3 and p1 and p3 < p2:
    print ('O produto 1 e 3 são os mais baratos!!')
elif p2 == p3 and p2 and p3 < p1:
    print ('O produto 1 e 2 são os mais baratos!!')
    
else:
    print ('Todos os preços são iguais!!')
    
