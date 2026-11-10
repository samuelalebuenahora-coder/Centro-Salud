from tkinter import *


ventana = Tk()
ventana.title("Formulario de Cita")
ventana.geometry("500x500")
ventana.configure(bg="#f2f2f2")


def guardar_cita():
    id_paciente = dato_entrada1.get()
    id_medico = dato_entrada2.get()
    dia = dato_entrada3.get()
    hora = dato_entrada4.get()

    mensaje = (
        f"ID paciente: {id_paciente}\n"
        f"ID médico: {id_medico}\n"
        f"Día: {dia}\n"
        f"Hora: {hora}"
    )
    resultado.config(text=mensaje, fg="white", bg="green")


titulo = Label(ventana, text="Formulario de Cita", fg="white", bg="black", font=("Verdana", 22))
titulo.pack(pady=15)

label_paciente = Label(ventana, text="Ingrese el ID del paciente", fg="blue", font=("Verdana", 12))
label_paciente.pack()
dato_entrada1 = StringVar()
Entry(ventana, text=dato_entrada1, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_medico = Label(ventana, text="Ingrese el ID del médico", fg="blue", font=("Verdana", 12))
label_medico.pack()
dato_entrada2 = StringVar()
Entry(ventana, text=dato_entrada2, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_dia = Label(ventana, text="Ingrese el día", fg="blue", font=("Verdana", 12))
label_dia.pack()
dato_entrada3 = StringVar()
Entry(ventana, text=dato_entrada3, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_hora = Label(ventana, text="Ingrese la hora", fg="blue", font=("Verdana", 12))
label_hora.pack()
dato_entrada4 = StringVar()
Entry(ventana, text=dato_entrada4, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

boton = Button(ventana, text="Guardar Cita", command=guardar_cita, font=("Verdana", 12))
boton.pack(pady=12)

resultado = Label(ventana, text="", fg="white", bg="green", font=("Verdana", 12), justify="left")
resultado.pack(padx=12, pady=8, fill="x")

ventana.mainloop()
