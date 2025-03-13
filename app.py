tasks = []  # Lista para almacenar las tareas, cada tarea será un diccionario con "nombre" y "estado"

def add_task(task):
    tasks.append({"name": task, "completed": False})  # Se añade la tarea con estado "Pendiente"
    print(f"Tarea '{task}' añadida.")

def list_tasks():
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print("\nLista de tareas:")
        for i, task in enumerate(tasks, 1):
            status = "✔️ Completada" if task["completed"] else "❌ Pendiente"
            print(f"{i}. {task['name']} - {status}")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Tarea '{removed_task['name']}' eliminada.")
    else:
        print("Número de tarea inválido.")

def complete_task(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True  # Marcar como completada
        print(f"Tarea '{tasks[task_number - 1]['name']}' marcada como completada.")
    else:
        print("Número de tarea inválido.")

while True:
    print("\nOpciones:")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")

    option = input("Elige una opción: ")

    if option == "1":
        task = input("Escribe la tarea: ")
        add_task(task)
    elif option == "2":
        list_tasks()
    elif option == "3":
        list_tasks()
        task_number = int(input("Número de la tarea a eliminar: "))
        remove_task(task_number)
    elif option == "4":
        list_tasks()
        task_number = int(input("Número de la tarea a completar: "))
        complete_task(task_number)
    elif option == "5":
        break
    else:
        print("Opción no válida.")
