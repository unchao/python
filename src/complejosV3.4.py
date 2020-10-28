class complejos():
    def __init__(self,nreal,nimaginario):
        self.nreal=nreal
        self.nimaginario=nimaginario
        self.numero_complejo= nreal + nimaginario

    def suma(self,c2):
        return c1.numero_complejo + c2.numero_complejo

    def suma_conjugado(self,c2):
        return (c1.numero_complejo + c2.numero_complejo).conjugate()

    def suma_opuesto(self,c2):
        return (c1.numero_complejo + c2.numero_complejo) *-1

    def resta(self,c2):
        return c1.numero_complejo - c2.numero_complejo

    def resta_conjugado(self,c2):
        return (c1.numero_complejo - c2.numero_complejo).conjugate()

    def resta_opuesto(self,c2):
        return (c1.numero_complejo - c2.numero_complejo) *-1

    def multiplicacion(self,c2):
        return c1.numero_complejo * c2.numero_complejo

    def multiplicacion_conjugado(self,c2):
        return (c1.numero_complejo * c2.numero_complejo).conjugate()

    def multiplicacion_opuesto(self,c2):
        return (c1.numero_complejo * c2.numero_complejo) *-1

    def division(self,c2):
        return c1.numero_complejo / c2.numero_complejo

    def division_conjugado(self,c2):
        return (c1.numero_complejo / c2.numero_complejo).conjugate()

    def division_opuesto(self,c2):
        return (c1.numero_complejo / c2.numero_complejo) *-1

r1=input("ingrese el primer real: ")
i1=input("ingrese el primer real: ") + "i"
r2=input("ingrese el segundo real: ")
i2=input("ingrese el primer real: ") + "i"

i1, i2=i1.replace('i','j'), i2.replace('i','j')

r1, i1, r2, i2=int(r1), complex(i1), int(r2), complex(i2)

c1=complejos(r1,i1)
c2=complejos(r2,i2)

operacion=input("Ingrese operación ( + , - , * , / ): ")

if operacion=="+":

    print(f"suma: {complejos.suma(c1,c2)}")
    print(f"conjugado: {complejos.suma_conjugado(c1,c2)}")
    print(f"opuesto: {complejos.suma_opuesto(c1,c2)}")
    print(f"resultado real: {r1+r2}")

elif operacion=="-":

    print(f"resta: {complejos.resta(c1,c2)}")
    print(f"conjugado: {complejos.resta_conjugado(c1,c2)}")
    print(f"opuesto: {complejos.resta_opuesto(c1,c2)}")
    print(f"resultado real: {r1-r2}")


elif operacion=="*":

    print(f"multiplicacion: {complejos.multiplicacion(c1,c2)}")
    print(f"conjugado: {complejos.multiplicacion_conjugado(c1,c2)}")
    print(f"opuesto: {complejos.multiplicacion_opuesto(c1,c2)}")
    print(f"resultado real: {r1*r2}")


elif operacion=="/":

    print(f"division: {complejos.division(c1,c2)}")
    print(f"conjugado: {complejos.division_conjugado(c1,c2)}")
    print(f"opuesto: {complejos.division_opuesto(c1,c2)}")
    print(f"resultado real: {r1/r2}")
