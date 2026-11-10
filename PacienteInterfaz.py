from tkinter import *


ventana = Tk()
ventana.title("Formulario de Paciente")
ventana.geometry("500x650")
ventana.configure(bg="#f2f2f2")


def guardar_paciente():
    ide = dato_entrada1.get()
    nombre = dato_entrada2.get()
    edad = dato_entrada3.get()
    sexo = dato_entrada4.get()
    estado = dato_entrada5.get()
    tipo_cita = dato_entrada6.get()

    mensaje = (
        f"ID: {ide}\n"
        f"Nombre: {nombre}\n"
        f"Edad: {edad}\n"
        f"Sexo: {sexo}\n"
        f"Estado de salud: {estado}\n"
        f"Tipo de cita: {tipo_cita}"
    )
    resultado.config(text=mensaje, fg="white", bg="green")


titulo = Label(ventana, text="Formulario de Paciente", fg="white", bg="black", font=("Verdana", 22))
titulo.pack(pady=15)

label_id = Label(ventana, text="Ingrese el ID del paciente", fg="blue", font=("Verdana", 12))
label_id.pack()
dato_entrada1 = StringVar()
Entry(ventana, text=dato_entrada1, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_nom = Label(ventana, text="Ingrese el nombre", fg="blue", font=("Verdana", 12))
label_nom.pack()
dato_entrada2 = StringVar()
Entry(ventana, text=dato_entrada2, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_edad = Label(ventana, text="Ingrese la edad", fg="blue", font=("Verdana", 12))
label_edad.pack()
dato_entrada3 = StringVar()
Entry(ventana, text=dato_entrada3, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_sexo = Label(ventana, text="Ingrese el sexo", fg="blue", font=("Verdana", 12))
label_sexo.pack()
dato_entrada4 = StringVar()
Entry(ventana, text=dato_entrada4, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_estado = Label(ventana, text="Ingrese el estado de salud", fg="blue", font=("Verdana", 12))
label_estado.pack()
dato_entrada5 = StringVar()
Entry(ventana, text=dato_entrada5, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_tipo = Label(ventana, text="Ingrese el tipo de cita", fg="blue", font=("Verdana", 12))
label_tipo.pack()
dato_entrada6 = StringVar()
Entry(ventana, text=dato_entrada6, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

boton = Button(ventana, text="Guardar Paciente", command=guardar_paciente, font=("Verdana", 12))
boton.pack(pady=12)

resultado = Label(ventana, text="", fg="white", bg="green", font=("Verdana", 12), justify="left")
resultado.pack(padx=12, pady=8, fill="x")

ventana.mainloop()
