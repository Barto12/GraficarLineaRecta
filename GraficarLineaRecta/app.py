import matplotlib.pyplot as plt
import numpy as np


def graficar_linea_recta(m, b):
    x = np.linspace(-10, 10, 400)
    y = m * x + b

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'y = {m}x + {b}', color='b')
    plt.title('Gráfica de Línea Recta')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


def graficar_ecuacion_cuadratica(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x ** 2 + b * x + c

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}', color='r')
    plt.title('Gráfica de Ecuación Cuadrática')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Graficar Línea Recta")
        print("2. Graficar Ecuación Cuadrática")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            try:
                m = float(input("Ingrese el valor de m: "))
                b = float(input("Ingrese el valor de b: "))
                graficar_linea_recta(m, b)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        elif opcion == '2':
            try:
                a = float(input("Ingrese el valor de a: "))
                b = float(input("Ingrese el valor de b: "))
                c = float(input("Ingrese el valor de c: "))
                graficar_ecuacion_cuadratica(a, b, c)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")


if __name__ == "__main__":
    menu()
