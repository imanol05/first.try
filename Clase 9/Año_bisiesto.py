def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 !=0) or año % 400 == 0:
        return "El año", año, "es bisiesto"
    else:
        return "El año", año, "no es bisiesto"

while True:
    año = int(input("Por favor ingrese un año para averiguar si es bisiesto:"))
    if año.isdigit():
        año = int(año)
        print(año_bisiesto(año))
        break
    else:
        print("El valor ingresado no es valido, ingrese un valor correcto")
        continue