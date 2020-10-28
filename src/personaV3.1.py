class Persona():
    def __init__(self, nombre, apellido, DNI, vacunas):
        self.DNI=DNI
        self.apellido=apellido
        self.nombre=nombre
        self.vacunas=vacunas

    def VerNombre(self):
        return self.nombre.capitalize()

    def VerApellido(self):
        return self.apellido.capitalize()

    def VerDNI(self):
        return self.DNI

    def VerVacunas(self):
        return self.vacunas

    def cambiar_nombre(self, nombre):
        self.nombre=nombre

    def cambiar_apellido(self, apellido):
        self.apellido=apellido

vacunas=["BCG","HPV","Doble"]

nombre=input("ingrese nombre: ")

apellido=input("ingrese apellido: ")

DNI= input("ingrese DNI: ")

persona1 = Persona(nombre, apellido, DNI, vacunas)

print("tus datos son:\n")
print(f"Nombre: {persona1.VerNombre()}")
print(f"Apellido: {persona1.VerApellido()}")
print(f"DNI: {persona1.VerDNI()}")
print(f"Vacunas: {persona1.VerVacunas()}")

Respuesta_0= input("son correctos? 's' 'n' : ")

if Respuesta_0 == "n" :

    i=True
    while i==True :

        Respuesta_1=input("que deseas cambiar? 'nombre' 'apellido' : ")

        if Respuesta_1 == "nombre" :

            nombre=input("ingrese nuevamente su nombre: ")
            persona1.cambiar_nombre(nombre)

        if Respuesta_1 == "apellido" :

            apellido=input("ingrese nuevamente su apellido: ")
            persona1.cambiar_apellido(apellido)

        print("tus datos son:\n")
        print(f"Nombre: {persona1.VerNombre()}")
        print(f"Apellido: {persona1.VerApellido()}")
        print(f"DNI: {persona1.VerDNI()}")
        print(f"Vacunas: {persona1.VerVacunas()}")

        Respuesta_0= input("son correctos? 's' 'n' : ")
        if Respuesta_0 == "s" :
            break

vacunas=["BCG","HPV","Doble"]

nombre=input("ingrese otro nombre: ")

apellido=input("ingrese otro apellido: ")

DNI= input("ingrese otro DNI: ")

yo=Persona(nombre,apellido,DNI,vacunas)

print("\ndatos de persona1:")
print(f"Nombre: {persona1.VerNombre()}")
print(f"Apellido: {persona1.VerApellido()}")
print(f"DNI: {persona1.VerDNI()}")
print(f"Vacunas: {persona1.VerVacunas()}")

print("\ndatos de yo:")
print(f"Nombre: {yo.VerNombre()}")
print(f"Apellido: {yo.VerApellido()}")
print(f"DNI: {yo.VerDNI()}")
print(f"Vacunas: {yo.VerVacunas()}")
