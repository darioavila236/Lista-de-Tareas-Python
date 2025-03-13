tasks = []  # Lista de tareas (diccionarios con "name" y "completed")

def add_task(tareas, nombre):
    """Agrega una nueva tarea a la lista."""
    tareas.append({"nombre": nombre, "completada": False})

def list_tasks():
    """Devuelve la lista de tareas con su estado."""
    return tasks

def remove_task(task_index):
    """Elimina una tarea por su índice."""
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)

def complete_task(tareas, indice):
    """Marca una tarea como completada si el índice es válido."""
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True

def edit_task(task_index, new_name):
    """Edita el nombre de una tarea."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["name"] = new_name
