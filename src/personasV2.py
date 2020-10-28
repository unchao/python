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

i = True
while i==True:

    DNI=input("ingrese DNI: ")

    Respuesta_0=input("su DNI es correcto?: 'si' 'no': ")

    if Respuesta_0=="si":
        break

yo=Persona(DNI, apellido, nombre, Vacunas)

if Respuesta_0=="no":
    DNI=input("ingrese DNI nuevamente: ")
    yo=Persona(DNI, apellido, nombre, Vacunas)

Respuesta_1=input(f"te llamas {yo.VerNombre()} {yo.VerApellido()}, es correcto?: 'si' 'no' : ")

i = True
while i==True:
    if Respuesta_1=="no":
        Respuesta_1=input("que deseas cambiar, nombre o apellido?: ")

        if Respuesta_1=="nombre":
            nombre=input("ingrese su nombre nuevamente: ")
            yo=Persona(DNI, apellido, nombre, Vacunas)

        if Respuesta_1=="apellido":
            apellido=input("ingrese su apellido nuevamente: ")
            yo=Persona(DNI, apellido, nombre, Vacunas)

        Respuesta_1=input(f"te llamas {yo.VerNombre()} {yo.VerApellido()}, es correcto?: 'si' 'no' : ")
        if Respuesta_1=="si":
            break

print(f"Eres {yo.VerNombre()} {yo.VerApellido()}, tu DNI es {yo.VerDNI()}, y tus vacunas son {yo.VerVacunas()} \n")

Respuesta_Modificar=input("\ndeseas cambiar algunas de estas cosas? 'si' 'no' : ")

i=True
while i==True:
    if Respuesta_Modificar == "si":
        Respuesta_Que=input("que deseas modificar? 'nombre' 'apellido' : ")

        if Respuesta_Que == "nombre":
            nombre=input("ingrese su nombre nuevamente: ")
            yo=Persona(DNI, apellido, nombre, Vacunas)

        if Respuesta_Que=="apellido":
            apellido=input("ingrese su apellido nuevamente: ")
            yo=Persona(DNI, apellido, nombre, Vacunas)

    print(f"te llamas {yo.VerNombre()} {yo.VerApellido()}, tu DNI es {yo.VerDNI()}, y tus vacunas son {yo.VerVacunas()} \n")
    Respuesta_1=input("Es correcto? 'si' 'no' : ")
    if Respuesta_1=="si":
        break
