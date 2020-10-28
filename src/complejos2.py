class operaciones():
    def __init__(self,Numero_Real_0, Numero_Real_1, Numero_Imaginario_0, Numero_Imaginario_1, Complejo_0, Complejo_1, Resultado):
        self.Real_0=Numero_Real_0
        self.Imaginario_0=Numero_Imaginario_0
        self.Real_1=Numero_Real_1
        self.Imaginario_1=Numero_Imaginario_1
        self.Resultado=Resultado
        self.Complejo_0=Complejo_0
        self.Complejo_1=Complejo_1

    def suma(self):

        Numero_Imaginario_0, Numero_Imaginario_1= Numero_Imaginario_0.replace('i','j'), Numero_Imaginario_1.replace('i','j')

        Numero_Real_0, Numero_Imaginario_0= int(Numero_Real_0), complex(Numero_Imaginario_0)
        Numero_Real_0, Numero_Imaginario_1= int(Numero_Real_1), complex(Numero_Imaginario_1)

        Complejo_0=operaciones(Numero_Real_0 + Numero_Imaginario_0)
        Complejo_1=operaciones(Numero_Real_1 + Numero_Imaginario_1)

        return self.Complejo_0

Numero_Real_0="1"
Numero_Imaginario_0="2i"
Numero_Real_1="3"
Numero_Imaginario_1="4i"
# Numero_Real_0=input("ingrese el primer numero real: ")
# Numero_Imaginario_0=input("ingrese el primer numero imaginario: ")
# Numero_Real_1=input("ingrese el segundo numero real: ")
# Numero_Imaginario_1=input("ingrese el segundo numero imaginario: ")
Complejo_0=operaciones(Numero_Real_0 + Numero_Imaginario_0)

suma()

print(operaciones.suma())

