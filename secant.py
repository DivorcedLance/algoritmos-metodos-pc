import numpy as np

def secant_method(f, x0, x1, tol):
    # P-1: La función f(x) ya está dada como un parámetro
    
    # P-2: Inicializar variables
    x_prev2 = x0  # x_{i-2}
    x_prev1 = x1  # x_{i-1}
    x_next = x1   # x_i, el punto inicial
    i=1
    
    print(f"{i}\t{x_prev2}")
    while True:
        # P-2: Aplicar la regla de recurrencia para encontrar el siguiente punto
        numerator = f(x_prev2) * x_prev1 - f(x_prev1) * x_prev2
        denominator = f(x_prev2) - f(x_prev1)
        
        if denominator == 0:  # Para evitar divisiones por cero
            return "Denominador se hizo cero. Método falló."
        
        x_next = numerator / denominator
        
        i+=1
        print(f"{i}\t{x_prev2}\t{x_prev1}\t{x_next}")
        
        # P-3: Criterio de parada
        if np.abs(x_next - x_prev1) <= tol:
            break
        
        x_prev2 = x_prev1  # Actualizar x_{i-2} para la siguiente iteración
        x_prev1 = x_next   # Actualizar x_{i-1} para la siguiente iteración
        
        # Caso Contrario (cc): Volver a P-2
    
    return x_next

# Ejemplo de uso
if __name__ == "__main__":
    # Definir la función para la cual encontrar la raíz
    def my_function(x):
        return np.sinh(x)/x-2
    
    # Parámetros
    x0 = -3
    x1 = -2
    k=6
    tol = 0.5 * 10**(-k)
    
    print("Tolerancia: ", tol)
    print(f"k={6}")

    # Llamar al método de la secante
    root = secant_method(my_function, x0, x1, tol)
    print(f"La raíz aproximada es: {root}")