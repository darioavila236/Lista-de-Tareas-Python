import tkinter as tk
from tkinter import messagebox
import app  # Importamos la lógica desde app.py

# Función para actualizar la lista de tareas en la interfaz
def update_listbox():
    listbox.delete(0, tk.END)  # Borra la lista actual
    for i, task in enumerate(app.list_tasks()):
        status = "✔️" if task["completada"] else "❌"
        listbox.insert(tk.END, f"{i+1}. {task['nombre']} {status}")

# Función para añadir tarea
def add_task():
    task_name = entry.get()
    if task_name:
        app.add_task(app.list_tasks(), task_name)  # Usamos la lista de `app`
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Error", "La tarea no puede estar vacía.")

# Función para eliminar tarea
def remove_task():
    try:
        selected = listbox.curselection()[0]  # Obtiene la selección
        app.remove_task(selected)  # `remove_task` ya maneja la lista interna
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")

# Función para completar tarea
def complete_task():
    try:
        selected = listbox.curselection()[0]
        app.complete_task(app.list_tasks(), selected)  # Pasamos la lista de `app`
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para completar.")

# Función para editar tarea
def edit_task():
    try:
        selected = listbox.curselection()[0]
        new_name = entry.get()
        if new_name:
            app.edit_task(selected, new_name)  # `edit_task` ya usa la lista de `app`
            entry.delete(0, tk.END)
            update_listbox()
        else:
            messagebox.showwarning("Error", "El nuevo nombre no puede estar vacío.")
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para editar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Título de la aplicación
title_label = tk.Label(root, text="Gestor de Tareas", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Entrada de texto para nueva tarea
entry = tk.Entry(root, width=40, font=("Helvetica", 12))
entry.pack(pady=10)

# Frame para los botones
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Botones con estilos
btn_add = tk.Button(button_frame, text="Añadir", command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
btn_add.grid(row=0, column=0, padx=5)

btn_complete = tk.Button(button_frame, text="Completar", command=complete_task, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
btn_complete.grid(row=0, column=1, padx=5)

btn_edit = tk.Button(button_frame, text="Editar", command=edit_task, bg="#FF9800", fg="white", font=("Helvetica", 10, "bold"))
btn_edit.grid(row=0, column=2, padx=5)

btn_remove = tk.Button(button_frame, text="Eliminar", command=remove_task, bg="#F44336", fg="white", font=("Helvetica", 10, "bold"))
btn_remove.grid(row=0, column=3, padx=5)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12))
listbox.pack(pady=10)

# Cargar tareas iniciales
update_listbox()

# Ejecutar la aplicación
root.mainloop()