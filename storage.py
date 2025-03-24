import json
import os

# Nombre del archivo donde se guardarán las tareas
TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Carga las tareas desde el archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    if os.path.exists(TASKS_FILE):  # Verifica si el archivo existe
        with open(TASKS_FILE, "r") as file:
            try:
                tasks = json.load(file)  # Carga las tareas desde el archivo
                return tasks
            except json.JSONDecodeError:
                # Si el archivo está corrupto o vacío, retorna una lista vacía
                return []
    else:
        # Si el archivo no existe, retorna una lista vacía
        return []

def save_tasks(tasks):
    """
    Guarda las tareas en el archivo JSON.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)  # Guarda las tareas con formato legible