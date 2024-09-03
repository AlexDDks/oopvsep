#include <stdio.h>  // Biblioteca est�ndar de entrada/salida
#include <string.h> // Biblioteca para manejar cadenas de caracteres

#define MAX_TASKS 10    // N�mero m�ximo de tareas
#define MAX_LENGTH 50   // Longitud m�xima de una tarea

char tasks[MAX_TASKS][MAX_LENGTH]; // Arreglo bidimensional para almacenar tareas
int task_count = 0;                // Contador de tareas actuales

// Funci�n para agregar una tarea
void add_task(char task[]) {
    if (task_count < MAX_TASKS) { // Verifica si se pueden agregar m�s tareas
        strcpy(tasks[task_count], task); // Copia la tarea al arreglo
        task_count++;                    // Incrementa el contador de tareas
        printf("Tarea agregada: %s\n", task); // Muestra un mensaje de confirmaci�n
    } else {
        printf("No se pueden agregar m�s tareas.\n"); // Mensaje de error si el l�mite de tareas se ha alcanzado
    }
}

// Funci�n para eliminar una tarea
void delete_task(int index) {
    int i; // Declaraci�n de la variable de control del bucle antes del bucle for
    if (index >= 0 && index < task_count) { // Verifica si el �ndice es v�lido
        for (i = index; i < task_count - 1; i++) {
            strcpy(tasks[i], tasks[i + 1]); // Mueve las tareas siguientes un lugar hacia atr�s
        }
        task_count--; // Reduce el contador de tareas
        printf("Tarea eliminada.\n"); // Muestra un mensaje de confirmaci�n
    } else {
        printf("�ndice de tarea inv�lido.\n"); // Mensaje de error si el �ndice no es v�lido
    }
}

// Funci�n para listar todas las tareas
void list_tasks() {
    int i; // Declaraci�n de la variable de control del bucle antes del bucle for
    printf("Lista de tareas:\n"); // Encabezado de la lista de tareas
    for (i = 0; i < task_count; i++) { 
        printf("%d: %s\n", i + 1, tasks[i]); // Imprime cada tarea con su n�mero correspondiente
    }
}

int main() {
    // Agregar algunas tareas
    add_task("Comprar leche");
    add_task("Estudiar C");
    add_task("Ir al gimnasio");

    // Listar tareas actuales
    list_tasks();

    // Eliminar la segunda tarea (�ndice 1)
    delete_task(1);

    // Listar tareas despu�s de la eliminaci�n
    list_tasks();

    return 0; // Indica que el programa termin� con �xito
}

