class operaciones():
    def __init__(self,num1,num2,resultado):
        self.Numero_Complejo_1=num1
        self.Numero_Complejo_2=num2
        self.resultado=resultado

    def operacion_suma(self):

        resultado=num1+num2

        return self.resultado
    
r1=input("ingrese el primer numero real: ")
i1=input("ingrese el primer numero imaginario: ")
r2=input("ingrese el segundo numero real: ")
i2=input("ingrese el segundo numero imaginario: ")

i1, i2=i1.replace('i','j'), i2.replace('i','j')

r1, i1=int(r1), complex(i1)
r2, i2=int(r2), complex(i2)

num1=(r1 + i1)
num2=(r2 + i2)
resultado=None
print(num1)

suma=operaciones(num1,num2,resultado)

respuesta=input("que desea hacer, sumar o restar? : ")

if respuesta=="sumar":

    operacion_suma()
    suma=operaciones(num1,num2,resultado)

print(operaciones.operacion_suma())
