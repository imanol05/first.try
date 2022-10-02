from builtins import input, print


def recortar(num, lim_inf, lim_sup):
    if num < lim_inf:
        return print(lim_inf)
    elif num > lim_sup:
        return print(lim_sup)
    else:
        return print(num)

print("El programa pedira al usuario tres numeros, el primero sera un numero cualquiera, el segundo sera el limite superior y el tercero, el limite superiorDevolvera los valores del limite que supere el numero si es que supera los limites, y el mismo numero si no los supera")
num = int(input("Ingrese un numero:"))
lim_inf = int(input("Ingrese un valor para el limite inferior:"))
lim_sup = int(input("Ingrese un valor para el limite superior:"))
while lim_inf > lim_sup:
    print("Los limites ingresados no cumplen con la consigna, por favor recuerde el limite inferior no puede superar al superior y visceversa")
    lim_inf = int(input("Ingrese un valor para el limite inferior:"))
    lim_sup = int(input("Ingrese un valor para el limite superior:"))    
recortar(num,lim_inf,lim_sup)