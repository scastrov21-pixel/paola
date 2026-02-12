# Taller: Funciones en Python


# Ejercicio 1: Conversión de temperaturas

def convertir_temperaturas(celsius):
    """
    Convierte una temperatura en °C a °F y K
    Entrada: temperatura en grados Celsius (número)
    Salida: diccionario con las tres escalas
    """
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    return {
        "Celsius": celsius,
        "Fahrenheit": round(fahrenheit, 2),
        "Kelvin": round(kelvin, 2)
    }


# Pruebas ejercicio 1
print("Ejercicio 1 - Conversión de temperaturas")
print(convertir_temperaturas(25))
print(convertir_temperaturas(0))
print(convertir_temperaturas(-10))
print(convertir_temperaturas(100))
print("-" * 50)






