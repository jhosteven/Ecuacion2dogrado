import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if discriminante < 0:
        return "No tiene soluciones reales"
    elif discriminante == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (x1, x2)


if __name__ == "__main__":
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))
    resultado = resolver_ecuacion_cuadratica(a, b, c)
    print("Las soluciones de la ecuación son:", resultado)
