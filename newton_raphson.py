import numpy as np

def newton_raphson(f, f_prime, x0, tol):
    # P-1: La función f(x) y su derivada f'(x) ya están dadas como parámetros
    
    # P-2: Inicializar variables
    x_prev = x0  # x_{i-1}
    x_next = x0  # x_i, el punto inicial
    i=0
    
    while True:
        # P-2: Aplicar la relación de recurrencia para encontrar el siguiente punto
        x_next = x_prev - f(x_prev) / f_prime(x_prev)
        print(f"{i}\t{x_prev}\t{x_next}")
        i+=1
        # P-3: Criterio de parada
        if np.abs(x_next - x_prev) <= tol:
            print(f"{x_next} - {x_prev} = {np.abs(x_next - x_prev)}")
            break
        
        x_prev = x_next  # Actualizar x_{i-1} para la siguiente iteración
        
        # Caso Contrario (cc): Volver a P-2
    
    return x_next

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la función f(x) y su derivada f'(x)
    # Por ejemplo, para f(x) = x^2 - 4, f'(x) = 2x
    def my_function(x):
        return np.e ** (-x) + x**3
    
    def my_function_prime(x):
        return -np.e ** (-x) + 3*x**2
    
    # Parámetros
    x0 = -1.9  # Valor inicial
    m = 0
    n = 6
    tol = 0.5*10**(m-n+1)
    
    print("Tolerancia: ", tol)
    print(f"m={m}")
    print(f"n={n}")

    # Llamar al método de Newton-Raphson
    root = newton_raphson(my_function, my_function_prime, x0, tol)
    print(f"La raíz aproximada es: {root}")