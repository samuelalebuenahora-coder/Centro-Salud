import tkinter as tk
from tkinter import ttk, messagebox

from gestion import CentroSalud


class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centro de Salud")
        self.geometry("800x550")
        self.gestor = CentroSalud()

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.fp, self.lp = self.pagina("Personas", ["ID", "Nombre"], self.agregar_persona)
        self.fm, self.lm = self.pagina(
            "Médicos",
            ["ID", "Nombre", "Especialidad", "Tipo", "Sueldo"],
            self.agregar_medico,
        )
        self.fpa, self.lpa = self.pagina(
            "Pacientes",
            ["ID", "Nombre", "Edad", "Sexo", "Estado de salud", "Tipo de cita"],
            self.agregar_paciente,
        )
        self.fh, self.lh = self.pagina("Horarios", ["ID médico", "Día", "Hora"], self.agregar_horario)
        self.fc, self.lc = self.pagina("Citas", ["ID paciente", "ID médico", "Día", "Hora"], self.agregar_cita)

        ttk.Button(
            self.fc["frame"],
            text="Cancelar cita seleccionada",
            command=self.cancelar_cita,
        ).pack(pady=5)

    def pagina(self, titulo, campos, accion):
        frame = ttk.Frame(self.tabs, padding=12)
        self.tabs.add(frame, text=titulo)

        entradas = {}
        for i, nombre in enumerate(campos):
            ttk.Label(frame, text=f"{nombre}:").grid(row=i, column=0, sticky="w", pady=4)
            entradas[nombre] = ttk.Entry(frame, width=30)
            entradas[nombre].grid(row=i, column=1, sticky="w", pady=4)

        ttk.Button(frame, text="Registrar / Ejecutar", command=lambda: self.seguro(accion)).grid(
            row=len(campos), column=1, pady=8, sticky="w"
        )

        lista = tk.Listbox(frame, width=90, height=10)
        lista.grid(row=len(campos) + 1, column=0, columnspan=2, sticky="nsew", pady=8)

        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(len(campos) + 1, weight=1)

        entradas["frame"] = frame
        return entradas, lista

    def valor(self, formulario, campo):
        return formulario[campo].get().strip()

    def seguro(self, funcion):
        try:
            funcion()
        except (ValueError, TypeError) as error:
            messagebox.showerror("Error", str(error))

    def limpiar(self, formulario):
        for campo, entrada in formulario.items():
            if campo != "frame" and isinstance(entrada, ttk.Entry):
                entrada.delete(0, tk.END)

    def agregar_persona(self):
        self.gestor.agregar_persona(self.valor(self.fp, "ID"), self.valor(self.fp, "Nombre"))
        self.limpiar(self.fp)
        self.actualizar()
        messagebox.showinfo("Correcto", "Persona registrada.")

    def agregar_medico(self):
        self.gestor.agregar_medico(
            self.valor(self.fm, "ID"),
            self.valor(self.fm, "Nombre"),
            self.valor(self.fm, "Especialidad"),
            self.valor(self.fm, "Tipo"),
            self.valor(self.fm, "Sueldo"),
        )
        self.limpiar(self.fm)
        self.actualizar()
        messagebox.showinfo("Correcto", "Médico registrado.")

    def agregar_paciente(self):
        self.gestor.agregar_paciente(
            self.valor(self.fpa, "ID"),
            self.valor(self.fpa, "Nombre"),
            self.valor(self.fpa, "Edad"),
            self.valor(self.fpa, "Sexo"),
            self.valor(self.fpa, "Estado de salud"),
            self.valor(self.fpa, "Tipo de cita"),
        )
        self.limpiar(self.fpa)
        self.actualizar()
        messagebox.showinfo("Correcto", "Paciente registrado.")

    def agregar_horario(self):
        self.gestor.agregar_horario(
            self.valor(self.fh, "ID médico"),
            self.valor(self.fh, "Día"),
            self.valor(self.fh, "Hora"),
        )
        self.limpiar(self.fh)
        self.actualizar()
        messagebox.showinfo("Correcto", "Horario registrado.")

    def agregar_cita(self):
        self.gestor.agregar_cita(
            self.valor(self.fc, "ID paciente"),
            self.valor(self.fc, "ID médico"),
            self.valor(self.fc, "Día"),
            self.valor(self.fc, "Hora"),
        )
        self.limpiar(self.fc)
        self.actualizar()
        messagebox.showinfo("Correcto", "Cita programada.")

    def cancelar_cita(self):
        seleccion = self.lc.curselection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona una cita en la lista.")
            return

        try:
            self.gestor.cancelar_cita(seleccion[0])
            self.actualizar()
            messagebox.showinfo("Correcto", "Cita cancelada.")
        except ValueError as error:
            messagebox.showwarning("Aviso", str(error))

    def actualizar(self):
        listas = {
            self.lp: self.gestor.datos_para_listas()["personas"],
            self.lm: self.gestor.datos_para_listas()["medicos"],
            self.lpa: self.gestor.datos_para_listas()["pacientes"],
            self.lh: self.gestor.datos_para_listas()["horarios"],
            self.lc: self.gestor.datos_para_listas()["citas"],
        }

        for lista, datos in listas.items():
            lista.delete(0, tk.END)
            for dato in datos:
                lista.insert(tk.END, dato)


if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
