# Lista global para almacenar tareas
tasks = []

# Agrega una tarea a la lista de tareas
def add_task(name):
    tasks.append(name)
    print(f"Tarea agregada: {name}")

# Elimina una tarea de la lista según su índice
def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)  # Elimina la tarea en el índice dado
        print(f"Tarea eliminada: {removed_task}")
    else:
        print("Índice de tarea inválido.")

# Lista todas las tareas almacenadas en la lista
def list_tasks():
    print("Lista de tareas:")
    i = 1  # Inicializa el contador en 1
    for task in tasks:
        print(f"{i}: {task}")  # Imprime el número de tarea seguido del nombre de la tarea
        i+= 1

# Agregar tareas a la lista global
add_task("Comprar leche")
add_task("Estudiar Python")
add_task("Ir al gimnasio")

# Listar las tareas actuales
list_tasks()

# Eliminar la segunda tarea (índice 1)
delete_task(1)

# Listar las tareas después de la eliminación
list_tasks()


# -----------------
# ANÁLISIS
# En la programación estructurada, el enfoque principal se basa en el uso de funciones, variables globales, y un flujo de control claro y lineal.

# Las funciones add_task, delete_task, y list_tasks encapsulan las operaciones específicas que se realizan sobre las tareas. Esto sigue el principio de dividir un programa en pequeñas partes manejables (funciones) que realizan tareas específicas.
# Variables Globales:

# La lista tasks es una variable global que almacena todas las tareas. Es accesible y modificable por todas las funciones, lo que simplifica la manipulación de los datos, aunque también puede llevar a riesgos si no se maneja cuidadosamente.

# FLUJO DE CONTROL SECUENCIAL:
# El código sigue un flujo de control secuencial, donde las funciones se ejecutan en el orden en que se llaman. No hay saltos en el flujo ni estructuras complejas que podrían dificultar la lectura y comprensión del código.

# USO DE CONDICIONALES Y BUCLES:
# Se utilizan condicionales (if) para verificar la validez de los índices en delete_task, y bucles (for) para iterar sobre la lista de tareas en list_tasks. Estos son elementos básicos en la programación estructurada que ayudan a controlar el flujo del programa de manera predecible.

# SIMPLICIDAD Y CLARIDAD:
# El código es simple, directo y fácil de entender. No hay conceptos avanzados como clases o herencia

# MENOR SOBRECARGA INICIAL:
# El desarrollo inicial es rápido, ya que no necesitas diseñar un modelo de clases complejo

# ESCALABILIDAD LIMITADA:
# A medida que el programa crece, el manejo de la lista global tasks y la adición de nuevas funcionalidades puede volverse complicado. No hay una estructura clara para expandir o modificar el código sin afectar otras partes del programa

# MANTENIBILIDAD:
# Con el tiempo, el código puede volverse difícil de mantener. A medida que se añaden más funciones y se modifica la lista global, puede ser difícil seguir el flujo de datos y entender cómo interactúan las distintas partes del programa.

# RIESGO POR USO DE VARIABLES GLOBALES:
# El uso de variables globales puede llevar a errores difíciles de rastrear, especialmente si varias funciones modifican la misma lista. 