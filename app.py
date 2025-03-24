import storage  # Importamos el módulo de persistencia

# Cargar tareas al iniciar la aplicación
tasks = storage.load_tasks()

def add_task(nombre):
    """Agrega una nueva tarea a la lista y guarda los cambios."""
    tasks.append({"nombre": nombre, "completada": False})
    storage.save_tasks(tasks)  # Guarda las tareas después de agregar una nueva

def list_tasks():
    """Devuelve la lista de tareas con su estado."""
    return tasks

def remove_task(task_index):
    """Elimina una tarea por su índice y guarda los cambios."""
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        storage.save_tasks(tasks)  # Guarda las tareas después de eliminar una

def complete_task(indice):
    """Marca una tarea como completada si el índice es válido y guarda los cambios."""
    if 0 <= indice < len(tasks):
        tasks[indice]["completada"] = True
        storage.save_tasks(tasks)  # Guarda las tareas después de completar una

def edit_task(task_index, new_name):
    """Edita el nombre de una tarea y guarda los cambios."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["nombre"] = new_name  # Corregimos el nombre del campo a "nombre"
        storage.save_tasks(tasks)  # Guarda las tareas después de editar