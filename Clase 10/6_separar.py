from builtins import input, print


lista = []
pares = []
impares = []
def separar(lista):
    for pop in lista:
        if pop % 2 == 0:
            pares.append(pop)
        elif pop % 2 != 0:
            impares.append(pop)       
    return (pares, impares)
print("El programa separara de una lista los numeros pares e impares y los ordena de menor a mayor")
while True:
    num = int(input("Ingrese un numero por teclado:"))
    
    if num == 0:
        break
    lista.append(num)

print("La lista con numeros pares e impares es:",lista)
separar(lista)
impares.sort()
pares.sort()
print("Los numeros impares son:",impares,"\ny los pares son:",pares)
