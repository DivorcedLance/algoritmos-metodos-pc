import numpy as np

def fixed_point_method(g, x0, tol):
    # P-1: La función g(x) ya está dada como un parámetro.
    
    # P-2: Inicializar variables
    x_prev = x0  # x_{i-1}
    x_next = x0  # x_i, el punto inicial
    i=0
    
    while True:
        # P-2: Aplicar la relación de recurrencia para encontrar el siguiente punto
        x_next = g(x_prev)
        
        print(f"{i}\t{x_prev}\t{x_next}")
        i+=1
        
        # P-3: Criterio de parada
        if np.abs(x_next - x_prev) <= tol:
            break
        
        x_prev = x_next  # Actualizar x_{i-1} para la siguiente iteración
        
        # Caso Contrario (cc): Volver a P-2
    
    return x_next

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la función de iteración g(x)
    # Por ejemplo, para f(x) = x^2 - 4, una posible g(x) sería g(x) = sqrt(4 - x)
    def my_g_function(x):
        return 1/np.sin(x)
    
    # Parámetros
    x0 = 1.5  # Valor inicial
    m = 0
    n = 2
    tol = 0.5*10**(m-n+1)
    
    print("Tolerancia: ", tol)
    print(f"m={m}")
    print(f"n={n}")

    # Llamar al método del Punto Fijo
    root = fixed_point_method(my_g_function, x0, tol)
    print(f"La raíz aproximada es: {root}")