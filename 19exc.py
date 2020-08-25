#Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = []
for i in range(3):
    elemento = int(input("Digite um numero: "))
    lista.append(elemento)

lista.sort(reverse = True)
print(lista)
