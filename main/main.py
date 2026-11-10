import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from gestion import CentroSalud


class AppCentroSalud(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centro de Salud")
        self.geometry("920x620")
        self.minsize(820, 520)
        self.configure(bg="#f2f2f2")
        self.gestor = CentroSalud()

        titulo = tk.Label(
            self,
            text="Centro de Salud",
            fg="white",
            bg="black",
            font=("Verdana", 24),
            pady=12,
        )
        titulo.pack(fill="x")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(fill="both", expand=True, padx=12, pady=12)

        self.persona_form = self.crear_tab(
            "Persona",
            ["ID", "Nombre", "Año", "Mes", "Día", "Género", "Dirección", "Código postal"],
            self.guardar_persona,
        )
        self.medico_form = self.crear_tab(
            "Médico",
            ["ID", "Nombre", "Especialidad", "Tipo", "Sueldo"],
            self.guardar_medico,
        )
        self.paciente_form = self.crear_tab(
            "Paciente",
            ["ID", "Nombre", "Edad", "Sexo", "Estado de salud", "Tipo de cita"],
            self.guardar_paciente,
        )
        self.horario_form = self.crear_tab(
            "Horario",
            ["ID médico", "Día", "Hora"],
            self.guardar_horario,
        )
        self.cita_form = self.crear_tab(
            "Cita",
            ["ID paciente", "ID médico", "Día", "Hora"],
            self.guardar_cita,
        )

        self.crear_panel_resumen()

    def crear_tab(self, titulo, campos, accion):
        frame = ttk.Frame(self.tabs, padding=12)
        frame.configure(style="TFrame")
        self.tabs.add(frame, text=titulo)

        entradas = {}
        for i, campo in enumerate(campos):
            ttk.Label(frame, text=f"{campo}", foreground="blue", font=("Verdana", 11)).grid(
                row=i, column=0, sticky="w", padx=(0, 10), pady=6
            )
            entrada = ttk.Entry(frame, width=35, font=("Arial", 11))
            entrada.grid(row=i, column=1, sticky="ew", pady=6)
            entradas[campo] = entrada

        ttk.Button(frame, text="Guardar", command=lambda: self.seguro(accion, entradas), width=20).grid(
            row=len(campos), column=1, sticky="w", pady=(12, 0)
        )

        frame.columnconfigure(1, weight=1)
        return entradas

    def crear_panel_resumen(self):
        ttk.Label(self, text="Resumen de registros", foreground="blue", font=("Verdana", 12, "bold")).pack(
            padx=12, pady=(0, 6), anchor="w"
        )
        self.listado = tk.Listbox(self, width=120, height=14, font=("Arial", 10), bg="#ffffff")
        self.listado.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.actualizar_resumen()

    def valor(self, formulario, campo):
        return formulario[campo].get().strip()

    def seguro(self, accion, formulario):
        try:
            accion(formulario)
        except (ValueError, TypeError) as error:
            messagebox.showerror("Error", str(error))

    def limpiar(self, formulario):
        for entrada in formulario.values():
            entrada.delete(0, tk.END)

    def guardar_persona(self, formulario):
        self.gestor.agregar_persona(self.valor(formulario, "ID"), self.valor(formulario, "Nombre"))
        self.limpiar(formulario)
        self.actualizar_resumen()
        messagebox.showinfo("Correcto", "Persona registrada.")

    def guardar_medico(self, formulario):
        self.gestor.agregar_medico(
            self.valor(formulario, "ID"),
            self.valor(formulario, "Nombre"),
            self.valor(formulario, "Especialidad"),
            self.valor(formulario, "Tipo"),
            self.valor(formulario, "Sueldo"),
        )
        self.limpiar(formulario)
        self.actualizar_resumen()
        messagebox.showinfo("Correcto", "Médico registrado.")

    def guardar_paciente(self, formulario):
        self.gestor.agregar_paciente(
            self.valor(formulario, "ID"),
            self.valor(formulario, "Nombre"),
            self.valor(formulario, "Edad"),
            self.valor(formulario, "Sexo"),
            self.valor(formulario, "Estado de salud"),
            self.valor(formulario, "Tipo de cita"),
        )
        self.limpiar(formulario)
        self.actualizar_resumen()
        messagebox.showinfo("Correcto", "Paciente registrado.")

    def guardar_horario(self, formulario):
        self.gestor.agregar_horario(
            self.valor(formulario, "ID médico"),
            self.valor(formulario, "Día"),
            self.valor(formulario, "Hora"),
        )
        self.limpiar(formulario)
        self.actualizar_resumen()
        messagebox.showinfo("Correcto", "Horario registrado.")

    def guardar_cita(self, formulario):
        self.gestor.agregar_cita(
            self.valor(formulario, "ID paciente"),
            self.valor(formulario, "ID médico"),
            self.valor(formulario, "Día"),
            self.valor(formulario, "Hora"),
        )
        self.limpiar(formulario)
        self.actualizar_resumen()
        messagebox.showinfo("Correcto", "Cita programada.")

    def actualizar_resumen(self):
        datos = self.gestor.datos_para_listas()
        registros = []
        registros.extend([f"PERSONA: {d}" for d in datos["personas"]])
        registros.extend([f"MEDICO: {d}" for d in datos["medicos"]])
        registros.extend([f"PACIENTE: {d}" for d in datos["pacientes"]])
        registros.extend([f"HORARIO: {d}" for d in datos["horarios"]])
        registros.extend([f"CITA: {d}" for d in datos["citas"]])

        self.listado.delete(0, tk.END)
        for item in registros:
            self.listado.insert(tk.END, item)


if __name__ == "__main__":
    app = AppCentroSalud()
    app.mainloop()
