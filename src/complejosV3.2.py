class complejos():
    def __init__(self, nReal, nImaginario):
        self.nReal=nReal
        self.nImaginario=nImaginario

    def complejo(self):

        return self.nReal + self.nImaginario

    def suma(Ncomplejo1, Ncomplejo2):

        suma_compleja=Ncomplejo1 + Ncomplejo2

        return suma_compleja

    def resta(Ncomplejo1, Ncomplejo2):

        resta_compleja=Ncomplejo1 - Ncomplejo2

        return resta_compleja

    def multiplicacion(Ncomplejo1, Ncomplejo2):

        multiplicacion_compleja=Ncomplejo1 * Ncomplejo2

        return multiplicacion_compleja

    def division(Ncomplejo1, Ncomplejo2):

        division_compleja=Ncomplejo1 / Ncomplejo2

        return division_compleja

r1=input("ingrese el primer numero real: ")
i1=input("ingrese el primer numero imaginario: ") + "i"
r2=input("ingrese el segundo numero real: ")
i2=input("ingrese el segundo numero imaginario: ") + "i"

i1, i2=i1.replace('i','j'), i2.replace('i','j')

r1, i1, r2, i2=int(r1), complex(i1), int(r2), complex(i2)

Ncomplejo1=complejos(r1, i1)

Ncomplejo2= complejos(r2, i2)

Ncomplejo1_con_I = str (Ncomplejo1.complejo())

Ncomplejo2_con_I = str (Ncomplejo2.complejo())

suma_compleja = complejos.suma(Ncomplejo1.complejo(),Ncomplejo2.complejo())

resta_compleja= complejos.resta(Ncomplejo1.complejo(),Ncomplejo2.complejo())

multiplicacion_compleja= complejos.multiplicacion(Ncomplejo1.complejo(),Ncomplejo2.complejo())

division_compleja= complejos.division(Ncomplejo1.complejo(),Ncomplejo2.complejo())

respuesta = input("que quiere hacer, 'sumar' , 'restar' , 'multiplicar' o 'dividir': ")

print("\nhaciendo magia...\n")

print("################\n")

if respuesta == "sumar" :

    suma_conjugado=suma_compleja.conjugate()
    suma_opuesto=suma_compleja * -1
    suma_compleja= str(suma_compleja)

    print(f"la suma compleja es : {suma_compleja.replace('j','i')}")

    print(f"el conjugado de este numero es: {suma_conjugado.replace('j','i')} ")

    print(f"el opuesto de este numero : {suma_opuesto.replace('j','i')}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real == "s" :
        print(f"la suma real es {r1+r2}")

if respuesta == "restar" :

    resta_conjugado=resta_compleja.conjugate()
    resta_opuesto=resta_compleja * -1
    resta_compleja= str(resta_compleja)

    print(f"la resta compleja es : {resta_compleja.replace('j','i')}")

    print(f"el conjugado de este numero es: {resta_conjugado.replace('j','i')}")

    print(f"el opuesto de este numero es: {resta_opuesto.replace('j','i')}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real== "s" :
        print(f"la resta real es {r1-r2}")

if respuesta== "multiplicar":

    multiplicacion_conjugado=multiplicacion_compleja.conjugate()
    multiplicacion_opuesto=multiplicacion_compleja * -1
    multiplicacion_compleja=str(multiplicacion_compleja)

    print(f"la multiplicacion es: {multiplicacion_compleja.replace('j','i')}")

    print(f"el conjugado de este numero es: {multiplicacion_conjugado.replace('j','i')}")

    print(f"el opuesto de este numero es: {multiplicacion_opuesto.replace('j','i')}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real== "s" :
        print(f"la multiplicacion real es {r1*r2}")

if respuesta== "dividir":

    division_conjugado=division_compleja.conjugate()
    division_opuesto=division_compleja * -1
    division_compleja=str(division_compleja)

    print(f"la division es: {division_compleja.replace('j','i')}")

    print(f"el conjugado de este numero es: {division_conjugado.replace('j','i')}")

    print(f"el opuesto de este numero es {division_opuesto.replace('j','i')}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")

    if R_real== "s" :
        print(f"la division real es {r1/r2}")
