from builtins import input, print


lista = []
def relacion(lista):
    if lista[0] == lista[1]:
        return print("### 0 ###")
    if lista[0] > lista[1]:
        return print("### 1 ###")
    if lista[0] < lista[1]:
        return print("### -1 ###")

print("El programa almacenara numeros y segun la relacion 'mayor-menor o igual' que tenga devolvera un '1', '-1' o un '0'")

num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese un segundo numero:"))
lista.append(num1)
lista.append(num2)
relacion(lista)