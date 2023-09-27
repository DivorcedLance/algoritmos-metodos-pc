import numpy as np

def regula_falsi(f, a, b, tol):
    # P-1: Comprobar si los signos de f(a) y f(b) son iguales. Si es así, no hay raíz en el intervalo.
    if np.sign(f(a)) == np.sign(f(b)):
        return "No se garantiza que haya una raíz en el intervalo [a, b]"

    # Inicializar variables
    i=0
    x_prev = a  # x_{i-1}
    c = a       # x_i, el punto inicial
    print(f"i\ta \tb\tc")
    while True:
        # P-2: Calcular el "promedio ponderado" (x_i)
        c = (f(b) * a - f(a) * b) / (f(b) - f(a))
        
        print(f"{i}\t{a}\t{b}\t{c}")
        i+=1
        
        # Evaluar la función en el punto ponderado
        fc = f(c)
        
        # P-3: Actualizar [a, b] en función de la evaluación de f en los extremos y en el punto ponderado
        if np.sign(fc) == np.sign(f(a)):
            a = c
        else:
            b = c
        
        # P-4: Criterio de parada
        if np.abs(c - x_prev) <= tol:
            print(np.abs(c - x_prev))
            break
        
        x_prev = c  # Actualizar x_{i-1} para la siguiente iteración
        
        # Caso Contrario (cc): Volver a P-2
    
    return c

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la función para la cual encontrar la raíz
    def my_function(x):
        return x**2*np.sin(x)-1
    
    # Parámetros
    a = 1
    b = 2
    m = 0
    n = 2
    tol = 0.5*10**(m-n+1)
    
    print("Tolerancia: ", tol)
    print(f"m={m}")
    print(f"n={n}")

    # Llamar al método de Regula Falsi
    root = regula_falsi(my_function, a, b, tol)
    print(f"La raíz aproximada es: {root}")