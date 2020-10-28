#class complejos():
#    def __init__(self,nreal,nimaginario):
#        self.nreal = nreal
#        self.nimaginario = nimaginario
#        self.numero_complejo= complex(nreal, nimaginario)

#    def suma(self,c2):
#        return self.numero_complejo + c2.numero_complejo

#c1=complejos(1,2)
#c2=complejos(3,4)


#print(type(c1.numero_complejo))
#print(c1.suma(c2))

class complejos():
    def __init__(self,nreal,nimaginario):
        self.nreal=nreal
        self.nimaginario=nimaginario
        self.numero_complejo= complex(nreal , nimaginario)

    def suma(self,c2):
        return self.numero_complejo + c2.numero_complejo

    def suma_conjugado(self,c2):
        return (self.numero_complejo + c2.numero_complejo).conjugate()

    def suma_opuesto(self,c2):
        resultado= self.numero_complejo + c2.numero_complejo
        return -resultado

    def resta(self,c2):
        return self.numero_complejo - c2.numero_complejo

    def resta_conjugado(self,c2):
        resultado = self.numero_complejo - c2.numero_complejo
        return resultado.conjugate()

    def resta_opuesto(self,c2):
        resultado = self.numero_complejo - c2.numero_complejo
        return -resultado

    def multiplicacion(self,c2):

        primer_parentesis = self.nreal*c2.nreal - self.nimaginario*c2.nimaginario
        segundo_parentesis = self.nreal*c2.nimaginario + self.nimaginario*c2.nreal
        return  primer_parentesis + complex(str(segundo_parentesis)+ "j")

    def multiplicacion_conjugado(self,c2):
        primer_parentesis = self.nreal*c2.nreal - self.nimaginario*c2.nimaginario
        segundo_parentesis = self.nreal*c2.nimaginario + self.nimaginario*c2.nreal
        resultado = primer_parentesis + complex(str(segundo_parentesis) + "j")
        return resultado.conjugate()

    def multiplicacion_opuesto(self,c2):
        resultado = self.numero_complejo * c2.numero_complejo
        return -resultado

    def division(self,c2):
        a = self.nreal
        b = self.nimaginario
        c = c2.nreal
        d = c2.nimaginario
        fraccion1 = (a*c + b*d) / (c**2 + d**2)
        fraccion2 = complex(str(b*c - a*d)+"j") / (c**2 + d**2)
        return fraccion1 + fraccion2

    def division_conjugado(self,c2):
        a = self.nreal
        b = self.nimaginario
        c = c2.nreal
        d = c2.nimaginario
        fraccion1 = (a*c + b*d) / (c**2 + d**2)
        fraccion2 = complex(str(b*c - a*d)+"j") / (c**2 + d**2)
        resultado = fraccion1 + fraccion2
        return resultado.conjugate()

    def division_opuesto(self,c2):
        respuesta = self.numero_complejo / c2.numero_complejo
        return -respuesta

    def poner_i(self):
        str(self)
        return self.replace('j','i')

r1=input("ingrese el primer real: ")
i1=input("ingrese el primer imaginario: ")
r2=input("ingrese el segundo real: ")
i2=input("ingrese el primer imaginario: ")

#i1, i2=i1.replace('i','j'), i2.replace('i','j')

r1, i1, r2, i2=int(r1), int(i1), int(r2), int(i2)

c1=complejos(r1,i1)
c2=complejos(r2,i2)

operacion=input("Ingrese operacion ( + , - , * , / ): ")

if operacion=="+":

    print(f"suma: {c1.poner_i(c1.suma(c2))}")
    print(f"conjugado: {c1.poner_i(c1.suma_conjugado(c2))}")
    print(f"opuesto: {c1.poner_i(c1.suma_opuesto(c2))}")
    print(f"resultado real: {r1+r2}")

elif operacion=="-":

    print(f"resta: {c1.resta(c2)}")
    print(f"conjugado: {c1.resta_conjugado(c2)}")
    print(f"opuesto: {c1.resta_opuesto(c2)}")
    print(f"resultado real: {r1-r2}")


elif operacion=="*":

    print(f"multiplicacion: {c1.multiplicacion(c2)}")
    print(f"conjugado: {c1.multiplicacion_conjugado(c2)}")
    print(f"opuesto: {c1.multiplicacion_opuesto(c2)}")
    print(f"resultado real: {r1*r2}")


elif operacion=="/":

    print(f"division: {c1.division(c2)}")
    print(f"conjugado: {c1.division_conjugado(c2)}")
    print(f"opuesto: {c1.division_opuesto(c2)}")
    print(f"resultado real: {'{0:,.2f}'.format(float(r1/r2))}")
