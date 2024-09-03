class Task:
     # Constructor que inicializa la tarea con un nombre
    def __init__(self, name):
        self.name = name
        # self es una convención y se refiere a la instancia actual que se está creando, en donde podemos acceder a los atributos y métodos de la clase desde dentro de la misma clase
        
    # Método para devolver el nombre de la tarea cuando se imprime. Recordemos que los métodos no se duplican en cada instancia, sino que viven en la clase y ahora la instancia puede acceder a estos métodos.
    def __str__(self):
        return self.name
        # Cada que definimos un método en la clase, el primer parámetro debe ser self


class TaskManager:
    def __init__(self):
        # Constructor que inicializa una lista vacía de tareas
        self.tasks = []
    
    # Método para agregar una tarea al final de la lista. Acordémonos que ahora la instancia de la clase TaskManager tiene acceso a cada uno de estos métodos que viven en la clase
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarea agregada: {task}")
    
    # Método para eliminar una tarea en un índice dado
    def delete_task(self, index):
        if 0 <= index < len(self.tasks): # Verifica si el índice es válido (mayor a cero, menor que la longitud de la lista)
            removed_task = self.tasks.pop(index) # Elimina la tarea de la lista por su índice y la guarda para futura consulta
            print(f"Tarea eliminada: {removed_task}") #Muestra la tarea eliminada
        else:
            print("Índice de tarea inválido.") #Si el índice no es válido

    def list_tasks(self):
        # Método para listar todas las tareas con su índice
        print("Lista de tareas:")
        i = 1 #Variable para visualización
        for task in self.tasks: #Iteramos en todos los elementos de la lista
            print(f"{i}: {task}") #Imprimimos "bonito" 
            i += 1  # Incrementa el contador en cada iteración




# Crear instancias de Task
tarea1 = Task("Comprar leche")
# tarea2 = Task("Estudiar Python")
# tarea3 = Task("Ir al gimnasio")

# Instancia de la clase TaskManager
manager = TaskManager()


# Agregar las tareas al TaskManager
manager.add_task(tarea1)
# manager.add_task(tarea2)
# manager.add_task(tarea3)

# Listar tareas actuales
manager.list_tasks()

# Eliminar la segunda tarea (índice 1)
manager.delete_task(1)

# # Listar tareas después de la eliminación
# manager.list_tasks()

# --------------------
# ANÁLISIS
# Principales recursos utilizados, relacionados a POO

# CLASES Y OBJETOS
# Task y TaskManager son clases que definen plantillas para crear objetos.  Cuando creas instancias de estas clases (como tarea1 = Task("Comprar leche") y manager = TaskManager()), estás creando objetos que contienen tanto datos (atributos) como comportamientos (métodos).

# ENCAPSULAMIENTO
# Los datos y métodos relacionados con una tarea están encapsulados dentro de la clase Task, y los relacionados con la gestión de tareas están encapsulados en TaskManager.
# self.name en Task y self.tasks en TaskManager son ejemplos de atributos que se gestionan dentro de sus respectivas clases.

# ABSTRACCION:
# La POO permite abstraer la complejidad del sistema de gestión de tareas.
# Como usuario de la clase TaskManager, no necesitas saber cómo se implementa internamente la lista de tareas; solo usas métodos como add_task, delete_task, y list_tasks para interactuar con ella.

# MODULARIDAD:
# Las clases Task y TaskManager están separadas, lo que facilita el manejo y la organización del código.
# Puedes trabajar en la clase Task sin preocuparte por los detalles de TaskManager, y viceversa.

# REUTILIZACIÓN DE CÓDIGO:
# Puedes reutilizar las clases Task y TaskManager en diferentes contextos sin necesidad de duplicar código.
# Por ejemplo, si necesitas otro tipo de gestor (quizás TaskManagerConPrioridades), puedes reutilizar Task y extender TaskManager.

# FACILIDAD DE MANTENIMIENTO
# La encapsulación y la modularidad facilitan el mantenimiento. Si hay un error en la gestión de tareas, sabes que probablemente esté en TaskManager. Si hay un error en la representación de una tarea, sabes que estará en Task.