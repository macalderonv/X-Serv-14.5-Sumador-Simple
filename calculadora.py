#!/usr/bin/python3
#Maria de los Ángeles Calderón Velasco

import sys

def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return None

funciones = {
    'suma': suma,
    'resta': resta,
    'multiplicacion': multiplicacion,
    'division': division
}

if __name__ == "__main__":   
    if len(sys.argv) != 4:
        print("No es correcto el numero de argumentos => ./calculadora.py <operacion> <numero1> <numero2>")
        sys.exit(1)

    try:
        numero1 = float(sys.argv[2])
        numero2 = float(sys.argv[3])
    except ValueError:
        print("Numeros erroneos")
        sys.exit(1)

    result = argv[1](numero1, numero2)
    print(result)
    sys.exit(0)
