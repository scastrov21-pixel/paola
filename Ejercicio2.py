# Ejercicio 2 (numerado como 3 en el enunciado): Gestión de estudiantes

estudiantes = []  # Lista global donde guardaremos los estudiantes

def agregar_estudiante(nombre, nota):
    """
    Agrega un estudiante a la lista
    Parámetros: nombre (str), nota (float/int)
    """
    estudiante = {
        "nombre": nombre,
        "nota": nota
    }
    estudiantes.append(estudiante)
    print(f"→ Estudiante {nombre} agregado con nota {nota}")


def mostrar_estudiantes():
    """Muestra todos los estudiantes registrados"""
    if not estudiantes:
        print("No hay estudiantes registrados aún.")
        return
    
    print("\nLista de estudiantes:")
    print("-" * 40)
    for est in estudiantes:
        print(f"{est['nombre']:20} | Nota: {est['nota']}")
    print("-" * 40)


def calcular_promedio():
    """Calcula y retorna el promedio general de notas"""
    if not estudiantes:
        return 0.0
    
    suma = 0
    for est in estudiantes:
        suma += est["nota"]
    
    promedio = suma / len(estudiantes)
    return round(promedio, 2)


# Pruebas ejercicio 2
print("\nEjercicio 2 - Gestión de estudiantes\n")

agregar_estudiante("Ana María", 4.5)
agregar_estudiante("Carlos", 3.2)
agregar_estudiante("Sofía", 4.8)
agregar_estudiante("Diego", 2.9)

mostrar_estudiantes()

print(f"Promedio general: {calcular_promedio()}")
print("-" * 50)
