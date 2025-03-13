import tkinter as tk
from tkinter import messagebox
import app  # Importamos la lógica desde app.py

# Función para actualizar la lista de tareas en la interfaz
def update_listbox():
    listbox.delete(0, tk.END)  # Borra la lista actual
    for i, task in enumerate(app.list_tasks()):
        status = "✔️" if task["completed"] else "❌"
        listbox.insert(tk.END, f"{i+1}. {task['name']} {status}")

# Función para añadir tarea
def add_task():
    task = entry.get()
    if task:
        app.add_task(task)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Error", "La tarea no puede estar vacía.")

# Función para eliminar tarea
def remove_task():
    try:
        selected = listbox.curselection()[0]  # Obtiene la selección
        app.remove_task(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")

# Función para completar tarea
def complete_task():
    try:
        selected = listbox.curselection()[0]
        app.complete_task(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para completar.")

# Función para editar tarea
def edit_task():
    try:
        selected = listbox.curselection()[0]
        new_name = entry.get()
        if new_name:
            app.edit_task(selected, new_name)
            entry.delete(0, tk.END)
            update_listbox()
        else:
            messagebox.showwarning("Error", "El nuevo nombre no puede estar vacío.")
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para editar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Entrada de texto para nueva tarea
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Botones
btn_add = tk.Button(root, text="Añadir", command=add_task)
btn_add.pack()

btn_complete = tk.Button(root, text="Completar", command=complete_task)
btn_complete.pack()

btn_edit = tk.Button(root, text="Editar", command=edit_task)
btn_edit.pack()

btn_remove = tk.Button(root, text="Eliminar", command=remove_task)
btn_remove.pack()

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Cargar tareas iniciales
update_listbox()

# Ejecutar la aplicación
root.mainloop()
