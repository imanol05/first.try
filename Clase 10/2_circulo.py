from builtins import input, print
from cmath import pi


def area_circulo (radio):
    return print("El area del circulo es de:", pi * radio ** 2)
print("Este programa calcula el area de un circulo")
radio = int(input("Por favor ingrese el valor del radio:"))

area_circulo(radio)