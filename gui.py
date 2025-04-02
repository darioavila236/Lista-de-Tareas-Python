import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
import app

# Configuración inicial
style = Style(theme='flatly')
root = style.master
root.title("Gestor de Tareas Avanzado")
root.geometry("650x550")

# Variables de estilo
COLOR_PRIMARY = '#2c3e50'
COLOR_SECONDARY = '#ecf0f1'
FONT_TITLE = ('Helvetica', 18, 'bold')
FONT_BODY = ('Helvetica', 12)

# Marco principal
main_frame = tk.Frame(root, padx=20, pady=20, bg=COLOR_SECONDARY)
main_frame.pack(expand=True, fill=tk.BOTH)

# Título
tk.Label(
    main_frame,
    text="Gestor de Tareas",
    font=FONT_TITLE,
    bg=COLOR_SECONDARY,
    fg=COLOR_PRIMARY
).pack(pady=(0, 20))

# Marco de entrada
input_frame = tk.Frame(main_frame, bg=COLOR_SECONDARY)
input_frame.pack(fill=tk.X, pady=10)

entry = tk.Entry(
    input_frame,
    font=FONT_BODY,
    relief=tk.FLAT,
    highlightthickness=1,
    highlightbackground='#bdc3c7',
    highlightcolor='#3498db'
)
entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

# Botones de acción
buttons_frame = tk.Frame(main_frame, bg=COLOR_SECONDARY)
buttons_frame.pack(fill=tk.X, pady=10)

button_style = {
    'font': ('Helvetica', 10, 'bold'),
    'borderwidth': 0,
    'relief': tk.FLAT,
    'padx': 10,
    'pady': 5
}

tk.Button(
    buttons_frame,
    text="➕ Añadir",
    command=lambda: add_task(),
    bg='#2ecc71',
    fg='white',
    **button_style
).pack(side=tk.LEFT, padx=5)

tk.Button(
    buttons_frame,
    text="✓ Completar",
    command=lambda: complete_task(),
    bg='#3498db',
    fg='white',
    **button_style
).pack(side=tk.LEFT, padx=5)

tk.Button(
    buttons_frame,
    text="✏ Editar",
    command=lambda: edit_task(),
    bg='#f39c12',
    fg='white',
    **button_style
).pack(side=tk.LEFT, padx=5)

tk.Button(
    buttons_frame,
    text="🗑 Eliminar",
    command=lambda: remove_task(),
    bg='#e74c3c',
    fg='white',
    **button_style
).pack(side=tk.LEFT, padx=5)

# Lista de tareas
list_frame = tk.Frame(main_frame, bg=COLOR_SECONDARY)
list_frame.pack(expand=True, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    list_frame,
    font=FONT_BODY,
    yscrollcommand=scrollbar.set,
    selectbackground='#3498db',
    selectforeground='white',
    activestyle='none',
    borderwidth=0,
    highlightthickness=0,
    bg='white'
)
listbox.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

# Pie de página
tk.Label(
    main_frame,
    text="© 2023 Gestor de Tareas | Python + ttkbootstrap",
    font=('Helvetica', 8),
    bg=COLOR_SECONDARY,
    fg='#7f8c8d'
).pack(pady=(20, 0))

# Funciones actualizadas
def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(app.list_tasks()):
        status = "✓" if task["completada"] else "✗"
        color = "#2ecc71" if task["completada"] else "#e74c3c"
        listbox.insert(tk.END, f"  {i+1}. {task['nombre']}")
        listbox.itemconfig(i, {'fg': color})

def add_task():
    task_name = entry.get()
    if task_name:
<<<<<<< HEAD
        app.add_task(task_name)  # Usamos la función actualizada de app.py
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Error", "La tarea no puede estar vacía.")

# Función para eliminar tarea
def remove_task():
    try:
        selected = listbox.curselection()[0]  # Obtiene la selección
        app.remove_task(selected)  # Usamos la función actualizada de app.py
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar.")
=======
        app.add_task(app.tasks, task_name)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Error", "La tarea no puede estar vacía", parent=root)
>>>>>>> gui

def complete_task():
    try:
        selected = listbox.curselection()[0]
<<<<<<< HEAD
        app.complete_task(selected)  # Usamos la función actualizada de app.py
=======
        app.complete_task(app.tasks, selected)
>>>>>>> gui
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para completar", parent=root)

def edit_task():
    try:
        selected = listbox.curselection()[0]
        new_name = entry.get()
        if new_name:
<<<<<<< HEAD
            app.edit_task(selected, new_name)  # Usamos la función actualizada de app.py
=======
            app.edit_task(selected, new_name)
>>>>>>> gui
            entry.delete(0, tk.END)
            update_listbox()
        else:
            messagebox.showwarning("Error", "El nuevo nombre no puede estar vacío", parent=root)
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para editar", parent=root)

def remove_task():
    try:
        selected = listbox.curselection()[0]
        app.remove_task(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar", parent=root)

# Eventos
entry.bind('<Return>', lambda e: add_task())
listbox.bind('<Double-Button-1>', lambda e: edit_task())

# Carga inicial
update_listbox()
entry.focus()

# Iniciar aplicación
root.mainloop()
