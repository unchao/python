class complejos():
    def __init__(self, nReal, nImaginario):
        self.nReal = nReal
        self.nImaginario = nImaginario

    def crear_complejo(self):
        return self.nReal + self.nImaginario

    def suma_complejo(c1,c2):
        return c1 + c2

    def suma_conjugado(suma_complejo):
        return suma_complejo.conjugate()

    def suma_opuesto(suma_complejo):
        return suma_complejo * -1

    def suma_real(r1,r2):
        return r1+r2

    def resta(c1,c2):
        return c1-c2

    def resta_conjugado(resta):
        return resta.conjugate()

    def resta_opuesto(resta):
        return resta * -1

    def resta_real(r1,r2):
        return r1-r2

    def multiplicacion(c1,c2):
        return c1*c2

    def multiplicacion_conjugado(multiplicacion):
        return multiplicacion.conjugate()

    def multiplicacion_opuesto(multiplicacion):
        return multiplicacion * -1

    def multiplicacion_real(r1,r2):
        return r1*r2

    def division(c1,c2):
        return c1/c2

    def division_conjugado(division):
        return division.conjugate()

    def division_opuesto(division):
        return division * -1

    def division_real(r1,r2):
        return r1/r2


r1=input("ingrese el primer numero real: ")
i1=input("ingrese el primer numero imaginario: ") + "i"
r2=input("ingrese el segundo numero real: ")
i2=input("ingrese el segundo numero imaginario: ") + "i"

i1, i2=i1.replace('i','j'), i2.replace('i','j')

r1, i1, r2, i2=int(r1), complex(i1), int(r2), complex(i2)

#crear los onjetos complejos y despues asignarles a cada objeto su propio complejo
c1 = complejos(r1,i1)
c2 = complejos(r2,i2)
c1=complejos.crear_complejo(c1)
c2=complejos.crear_complejo(c2)
#llamadas para no escribir siempre todos los metodos de la clase complejos
call_suma = complejos.suma_complejo(c1,c2)
call_sumarreal = complejos.suma_real(r1,r2)
call_resta = complejos.resta(c1,c2)
call_restareal = complejos.resta_real(r1,r2)
call_multiplicacion = complejos.multiplicacion(c1,c2)
call_multiplicacionreal= complejos.multiplicacion_real(r1,r2)
call_division = complejos.division(c1,c2)
call_divisionreal = complejos.division_real(r1,r2)

respuesta = input("que quiere hacer, 'sumar' , 'restar' , 'multiplicar' o 'dividir': ")

if respuesta == "sumar" :

    print(f"la suma es {str(call_suma).replace('j', 'i')}\n")

    print(f"el conjugado es {str(complejos.suma_conjugado(call_suma)).replace('j', 'i')}\n")

    print(f"el opuesto es {str(complejos.suma_opuesto(call_suma)).replace('j', 'i')}\n")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real == "s" :
        print(f"la suma real es {call_sumarreal}")

if respuesta == "restar" :

    print(f"la resta es {str(call_resta).replace('j', 'i')}\n")

    print(f"el conjugado es {str(complejos.resta_conjugado(call_resta)).replace('j', 'i')}\n")

    print(f"el opuesto es {str(complejos.resta_opuesto(call_resta)).replace('j', 'i')}\n")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real == "s" :
        print(f"la suma real es {call_restareal}")

if respuesta== "multiplicar":

    print(f"la multiplicacion es {str(call_multiplicacion).replace('j', 'i')}\n")

    print(f"el conjugado es {str(complejos.multiplicacion_conjugado(call_multiplicacion)).replace('j', 'i')}\n")

    print(f"el opuesto es {str(complejos.multiplicacion_opuesto(call_multiplicacion)).replace('j', 'i')}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real == "s" :
        print(f"la suma real es {call_multiplicacionreal}")


if respuesta == "dividir" :

    print(f"la division es {str(call_division).replace('j', 'i')}\n")

    print(f"el conjugado es {str(complejos.division_conjugado(call_division)).replace('j', 'i')}\n")

    print(f"el opuesto es {str(complejos.division_opuesto(call_division)).replace('j', 'i')}\n")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real == "s" :
        print(f"la suma real es {call_divisionreal}")
