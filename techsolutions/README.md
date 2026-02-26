# 🏢 TechSolutions S.A.S. — Sistema de Gestión de Servicios

> Proyecto de Grado | Programación Orientada a Objetos en Python | Semestre 5

---

## 📋 Descripción

Sistema modular desarrollado en **Python** para la empresa **TechSolutions S.A.S.**, que presta servicios tecnológicos como desarrollo de software, soporte técnico, consultoría y auditorías QA.

El sistema permite:
- ✅ Registrar y gestionar clientes
- ✅ Administrar un catálogo de servicios
- ✅ Generar cotizaciones con cálculo dinámico de costos
- ✅ Aplicar descuentos configurables (Patrón Strategy)
- ✅ Enviar notificaciones automáticas
- ✅ Menú interactivo por consola

---

## 🗂️ Estructura del Proyecto

```
techsolutions/
│
├── clientes.py         → Clase Cliente y RepositorioClientes
├── servicios.py        → Servicios (Herencia) y CatalogoServicios
├── facturacion.py      → Cotizacion y Estrategias de Descuento
├── notificaciones.py   → GestorNotificaciones
├── main.py             → Menú interactivo (punto de entrada)
│
├── diagrama_uml.png    → Diagrama UML de clases
└── README.md           → Este archivo
```

---

## 🧠 Conceptos de POO Aplicados

| Concepto | Dónde se aplica |
|---|---|
| **Clases y Objetos** | `Cliente`, `Cotizacion`, `CatalogoServicios` |
| **Herencia** | `Servicio` → `DesarrolloSoftware`, `SoporteTecnico`, `Consultoria`, `AuditoriaQA` |
| **Polimorfismo** | Cada servicio implementa `calcular_costo()` de forma distinta |
| **Encapsulamiento** | Atributos privados `__` con `@property` |
| **Clases Abstractas** | `Servicio` y `EstrategiaDescuento` con `ABC` |
| **Patrón Strategy** | Descuentos intercambiables sin modificar `Cotizacion` |
| **Métodos especiales** | `__str__`, `__repr__` en `Cliente` y `Servicio` |
| **Métodos estáticos** | `GestorNotificaciones` con `@staticmethod` |

---

## 🖥️ Diagrama UML de Clases

![Diagrama UML](diagrama_uml.png)

---

## ⚙️ Requisitos

- Python 3.8 o superior
- No requiere librerías externas

---

## 🚀 Cómo ejecutar

**1. Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/techsolutions.git
cd techsolutions
```

**2. Ejecuta el sistema:**
```bash
python main.py
```

---

## 🗺️ Menú del Sistema

```
TECHSOLUTIONS S.A.S. — Sistema de Gestión
══════════════════════════════════════════
   [1]  Gestión de Clientes
   [2]  Ver Catálogo de Servicios
   [3]  Crear Cotización
   [4]  Historial de Cotizaciones
   [5]  Enviar Notificación
   [0]  Salir
```

---

## 💰 Catálogo de Servicios

| Servicio | Unidad | Precio |
|---|---|---|
| Desarrollo de Software | Por hora | $85.000 COP |
| Soporte Técnico | Plan mensual + horas extra | $350.000 + $40.000/h |
| Consultoría | Por sesión | $200.000 COP |
| Auditoría QA | Por proyecto | $1.200.000 COP |

---

## 🎯 Tipos de Descuento

| Descuento | Condición | Ahorro |
|---|---|---|
| Sin descuento | — | 0% |
| Empresarial | Cliente tipo empresa | 15% |
| Por volumen | Total > $1.000.000 | 10% |
| Promoción especial | Configurable | % personalizado |

---

## 👨‍💻 Autor

**[Tu nombre completo]**  
Estudiante de Ingeniería / Tecnología en Sistemas  
Semestre 5 | [Nombre de tu institución]  
[Tu correo o LinkedIn]

---

## 📄 Licencia

Este proyecto fue desarrollado con fines académicos.
