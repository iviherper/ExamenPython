'''
Created on 10 mar. 2021

@author: Ivi
'''

num1 = int(input("Dame el numero entero inicial:"))
num2 = int(input("Dime cuantos valores quieres:"))
i = 0
lista = []
if num2 >= 0:
    while num2 > i:
        lista.append(num1)
        num1=num1+1
        i=i+1
    if lista.__len__()>0:
        print(lista)
else:
    print("La cantidad de valores no puede ser negativa!")