tasks = []  # Lista de tareas (diccionarios con "name" y "completed")

def add_task(task):
    """Añade una tarea a la lista."""
    tasks.append({"name": task, "completed": False})

def list_tasks():
    """Devuelve la lista de tareas con su estado."""
    return tasks

def remove_task(task_index):
    """Elimina una tarea por su índice."""
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)

def complete_task(task_index):
    """Marca una tarea como completada."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True

def edit_task(task_index, new_name):
    """Edita el nombre de una tarea."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["name"] = new_name
