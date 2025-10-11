La mayoría de los estudiantes tienen dificultades para organizar sus tareas, esto puede llevar a que olviden entregas de trabajos, tareas, proyectos, 
que acumulen responsabilidades y les ocasione estrés por no tener un control de sus pendientes, 
la falta de un sistema sencillo para visualizar y registrar sus tareas hace que su planeación sea ineficiente afectando así su rendimiento académico. 

Es por eso que para mejorar la organización de los estudiantes, se desarrollará un programa como To-Do List el cual te permitirá agregar nuevas tareas,visualizar todas tus tareas, 
te dejará marcar y ver las que tienes pendientes y las que ya completaste. 
Con esta herramienta los estudiantes podrán tener un mejor control sobre su agenda, planificar mejor y priorizar lo que deben hacer, de esta forma se promueve una mejor administración 
del tiempo y se puede llegar a reducir el estrés que se acumula debido a la acumulación de tareas. 

Algoritmos
def agregar_tareas
Entrada: el nombre de la tarea, y si si quieres agregar otra o no
Proceso: se inicia un ciclo dondo se repite hasta que el usuario diga que no quiere agregar más tareas. Si el usuario no escribe nada se mostrara un mensaje "no se puede agregar", si el ususario escribe el nombre de la tarea, agrega esa tarea  a la lista con el estado "pendiente", y se mostrara el mensaje de "tarea agregada", luego se le preguntará si quiere agregar otra, si responde que si, el ciclo se repite, si responde que no el ciclo se detiene
Salida: se decuelve la lista de tareas

def mostrar_tareas
Entrada: lista de tareas
Proceso: si en la lista no hay tareas, mostrará mensaje de no tienes tareas y termina. Si si hay tareas, muestra titulo (lista de tareas), luego recorre una por una las tareas de la lista y ve su nombre y estado (pendiente o completada, imprime la lista completa con números, estado y nombre de la tarea
Salida: lista de tareas con su número, nombre y estado (pendiente o completada)

def completar_tarea
Entrada: "Número de la tarea a completar:" 2 
Proceso: Revisa que la haya tareas en la la lista, si no hay mostrará un mensaje, si si hay mostrará la lista completa, pedirá al usuario el número de la tarea para marcar como completa, si escribe un número que no concuerde mostrará mensaje, si el número es correcto, regresara el nombre de la tarea y que esta completada
Salida: mensaje, regresa el estado de la tarea como "completada"
