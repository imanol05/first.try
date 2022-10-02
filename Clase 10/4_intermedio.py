from builtins import input, print


def intermedio(num1,num2):
    return print("El numero intermedio de",num1, "y", num2, "es:",(num1+num2)/2)
print("El programa le pedira al usuario dos numeros y le devolvera el numero intermedio entre los dos")
num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese un segundo numero:"))
intermedio(num1, num2)
