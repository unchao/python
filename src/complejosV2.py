
r1=input("ingrese el primer numero real: ")
i1=input("ingrese el primer numero imaginario: ")
r2=input("ingrese el segundo numero real: ")
i2=input("ingrese el segundo numero imaginario: ")

i1, i2=i1.replace('i','j'), i2.replace('i','j')

r1, i1, r2, i2=int(r1), complex(i1), int(r2), complex(i2)

c1=(r1 + i1)
c2=(r2 + i2)

respuesta = input("que quiere hacer, 'sumar' , 'restar' , 'multiplicar' o 'dividir': ")

print("\nhaciendo magia...\n")

print("################\n")

if respuesta == "sumar" :
    
    resultado_suma=c1+c2
    resultado_suma_con_I=str (resultado_suma)
    resultado_suma_conjugado=resultado_suma.conjugate()
    resultado_suma_opuesto=resultado_suma * -1

    print(f"la suma compleja es : {resultado_suma_con_I.replace('j','i')}")

    print(f"el conjugado de este numero es: {resultado_suma_conjugado} ")

    print(f"el opuesto de este numero : {resultado_suma_opuesto}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")
    
    if R_real == "s" :
        print(f"la suma real es {r1+r2}")

if respuesta == "restar" :

    resultado_resta=c1-c2
    resultado_resta_con_I= str(resultado_resta)
    resultado_resta_conjugado=resultado_resta.conjugate()
    resultado_resta_opuesto=resultado_resta * -1
        
    print(f"la resta compleja es : {resultado_resta_con_I.replace('j','i')}")

    print(f"el conjugado de este numero es: {resultado_resta_conjugado}")

    print(f"el opuesto de este numero es: {resultado_resta_opuesto}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")
    
    if R_real== "s" :
        print(f"la resta real es {r1-r2}")

if respuesta== "multiplicar":

    resultado_multiplicacion=c1*c2
    resultado_multiplicacion_con_i=str(resultado_multiplicacion)
    resultado_multiplicacion_conjugado=resultado_multiplicacion.conjugate()
    resultado_multiplicacion_opuesto=resultado_multiplicacion * -1

    print(f"la multiplicacion es: {resultado_multiplicacion_con_i.replace('j','i')}")

    print(f"el conjugado de este numero es: {resultado_multiplicacion_conjugado}")

    print(f"el opuesto de este numero es: {resultado_multiplicacion_opuesto}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")
    
    if R_real== "s" :
        print(f"la multiplicacion real es {r1*r2}")

if respuesta== "dividir":

    resultado_division=c1/c2
    resultado_division_con_i=str(resultado_division)
    resultado_division_conjugado=resultado_division.conjugate()
    resultado_division_opuesto=resultado_division * -1

    print(f"la division es: {resultado_division_con_i.replace('j','i')}")

    print(f"el conjugado de este numero es: {resultado_division_conjugado}")

    print(f"el opuesto de este numero es {resultado_division_opuesto}")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")
    
    if R_real== "s" :
        print(f"la division real es {r1/r2}")