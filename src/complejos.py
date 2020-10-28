r1=input("ingrese el primer numero real: ")
i1=input("ingrese el primer numero imaginario: ")
r2=input("ingrese el segundo numero real: ")
i2=input("ingrese el segundo numero imaginario: ")

i1, i2=i1.replace('i','j'), i2.replace('i','j')

r1, i1, r2, i2=int(r1), complex(i1), int(r2), complex(i2)

respuesta = input("que quiere hacer, 'sumar' o 'restar': ")

print("\nhaciendo magia...\n")

print("################\n")

if respuesta == "sumar" :
    
    resultado_suma_real=r1+r2
    resultado_suma_imaginaria=i1+i2
    resultado_suma_imaginaria=str (resultado_suma_imaginaria)

    print(f"la suma compleja es :({resultado_suma_real},{resultado_suma_imaginaria.replace('j','i')})")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")
    
    if R_real == "s" :
        print(f"la suma real es {r1+r2}")

if respuesta == "restar" :

    resultado_resta_real=r1-r2
    resultado_resta_imaginaria=i1-i2
    resultado_resta_imaginaria= str(resultado_resta_imaginaria)
        
    print(f"la resta compleja es :({resultado_resta_real},{resultado_resta_imaginaria.replace('j','i')})")

    R_real=input("\ndesea ver el resultado real? 's' 'n' : ")
    
    if R_real== "s" :
        print(f"la resta real es {r1-r2}")

print(f"resultado imaginario fuera del if: {resultado_suma_imaginaria}")

resultado_suma_imaginaria= complex(resultado_suma_imaginaria)

print(type(resultado_suma_imaginaria))

resultado_suma_imaginaria= resultado_suma_imaginaria * -1

print(resultado_suma_imaginaria)