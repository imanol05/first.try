from builtins import input, print


def area_rectangulo (base, altura):
    return print("El area de su rectangulo de base:",base,"y altura:",altura,"es de:", base * altura)
print("Este programa calcula el area de un rectangulo en base a una 'base' y una 'altura' ingresada por teclado'")
base = int(input("Por favor ingrese la base del rectangulo:"))
altura = int(input("Por favor ingrese la altura del rectangulo:"))
while base == altura:
    print("Joven sabe usted que los rectangulos tienen diferentes medidas en su 'altura' y su 'base' no?")
    base = int(input("Por favor ingrese la base del rectangulo:"))
    altura = int(input("Por favor ingrese la altura del rectangulo:"))
area_rectangulo(base , altura)