

print("--------------------------")
print("-----mayor de 2 enteros---")
print("--------------------------")

#input

x=int(input("digite el valor de x: "))
y=int(input("digite el valor de y: "))

#processing

if x == y:
    print("los numeros son iguales")
else:
    if x>y:
      mayor = x
    else: 
      mayor = y

    print("El mayor entre" , str(x) , " y " , str(y) , " es " , str(mayor))