'''
Created on 12 mar. 2021

@author: Ivi
'''
concursantes = {("Javi","Madrid"):25,("Marta","Cuenca"):21,("Nacho","Toledo"):19,("Loli","Segovia"):22}
ciudades = []
nombres=[]

for clave in concursantes.__iter__():
    ciudades.append(clave[1])
    nombres.append(clave[0])
    
edades = concursantes.values()

print(ciudades)
print(nombres)
print(edades)