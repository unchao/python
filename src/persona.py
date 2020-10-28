class Persona():
    def __init__(self,DNI,apellido,nombre,Vacunas):
        self.DNI=DNI
        self.apellido=apellido
        self.Nombre=nombre
        self.Vacunas=Vacunas

    def VerNombre(self):
        return self.Nombre

    def VerApellido(self):
        return self.apellido

    def VerVacunas(self):
        return self.Vacunas

    def VerDNI(self):
        return self.DNI

Vacunas=["BCG","HPV","Doble"]

nombre=input("ingrese nombre: ")

apellido=input("ingrese apellido: ")

DNI=input("ingrese DNI: ")

Respuesta_0=input("su DNI es correcto?: 'si' 'no': ")

yo=Persona(DNI, apellido, nombre, Vacunas)

if Respuesta_0=="no":
    DNI=input("ingrese DNI nuevamente: ")
    yo=Persona(DNI, apellido, nombre, Vacunas)

Respuesta_1=input(f"te llamas {yo.VerNombre()} {yo.VerApellido()}, es correcto?: ")

if Respuesta_1=="no":
    Respuesta_1=input("que deseas cambiar, nombre o apellido?: ")

    if Respuesta_1=="nombre":
        nombre=input("ingrese su nombre nuevamente: ")
        yo=Persona(DNI, apellido, nombre, Vacunas)
    
    if Respuesta_1=="apellido":
        apellido=input("ingrese su apellido nuevamente: ")
        yo=Persona(DNI, apellido, nombre, Vacunas)

print(f"te llamas {yo.VerNombre()} {yo.VerApellido()}, tu DNI es {yo.VerDNI()}, y tus vacunas son {yo.VerVacunas()} ")
