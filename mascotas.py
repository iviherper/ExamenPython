'''
Created on 12 mar. 2021

@author: Ivi
'''
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def ver_nombre(self):
        print(self.nombre)

    def ver_especie(self):
        print(self.especie)
        
    def ver_edad(self):
        print(self.edad)
            
    def __str__(self):
        print(self.nombre,"es un",self.especie)

class Perro(Mascota):
    persigue=""
    def __persigue_gatos__(self):
        print(self.nombre,self.persigue)


tobi = Perro("Tobi","Perro", 3)
tobi.persigue="persigue gatos"

persi = Mascota("Persi","Gato",1)

moli = Perro("Moli","Perro", 2)
moli.persigue="no persigue gatos"

Cani = Mascota("Cani","Canario",4)

anki = Mascota("Anki","Gato",2)

print("Punto 1")
tobi.__str__()
persi.__str__()
moli.__str__()
Cani.__str__()
anki.__str__()

print("Punto 2")
print(persi.nombre,persi.edad,persi.especie)
print(anki.nombre,anki.edad,anki.especie)

print("Punto 3")
Cani.ver_nombre()
Cani.ver_edad()
Cani.ver_especie()

print("Punto 4")
tobi.__persigue_gatos__()
moli.__persigue_gatos__()
