# Ejercicio 3 (numerado como 4 en el enunciado): Análisis de ventas

def analizar_ventas(lista_ventas):
    """
    Analiza una lista de ventas y retorna:
    - venta mayor
    - venta menor
    - promedio
    """
    if not lista_ventas:
        return {
            "mayor": 0,
            "menor": 0,
            "promedio": 0
        }
    
    mayor = max(lista_ventas)
    menor = min(lista_ventas)
    promedio = sum(lista_ventas) / len(lista_ventas)
    
    return {
        "mayor": mayor,
        "menor": menor,
        "promedio": round(promedio, 2)
    }


# Pruebas ejercicio 3
ventas = [1200, 850, 1020, 2100, 1750, 980]

print("\nEjercicio 3 - Análisis de ventas")
resultado = analizar_ventas(ventas)

print(f"Ventas registradas: {ventas}")
print(f"Venta mayor   : ${resultado['mayor']}")
print(f"Venta menor   : ${resultado['menor']}")
print(f"Promedio ventas: ${resultado['promedio']}")
print("-" * 50)