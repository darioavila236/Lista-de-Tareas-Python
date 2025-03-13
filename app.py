tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Tarea '{task}' añadida.")

def list_tasks():
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print("Lista de tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Tarea '{removed_task}' eliminada.")
    else:
        print("Número de tarea inválido.")

while True:
    print("\nOpciones:")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

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
        break
    else:
        print("Opción no válida.")
