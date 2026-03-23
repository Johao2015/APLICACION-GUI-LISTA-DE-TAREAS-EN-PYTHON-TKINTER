"""
Aplicación GUI de Lista de Tareas
Autor: Johao Flores

Descripción:
Aplicación sencilla usando Tkinter que permite:
- Añadir tareas
- Marcar tareas como completadas
- Eliminar tareas
"""

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas - Johao Flores")
        self.root.geometry("400x400")

        # Lista interna para almacenar tareas y su estado
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task_event)  # Evento Enter

        # Lista visual
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Evento opcional: doble clic para completar tarea
        self.listbox.bind("<Double-Button-1>", self.complete_task_event)

    def add_task_event(self, event):
        """Evento para añadir tarea con Enter"""
        self.add_task()

    def add_task(self):
        """Añade una nueva tarea"""
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")

    def complete_task_event(self, event):
        """Evento de doble clic para completar tarea"""
        self.complete_task()

    def complete_task(self):
        """Marca una tarea como completada"""
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero")

    def delete_task(self):
        """Elimina una tarea"""
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero")

    def update_listbox(self):
        """Actualiza la lista visual"""
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["completed"]:
                text = "✔ " + text
            self.listbox.insert(tk.END, text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
