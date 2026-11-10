from tkinter import *


ventana = Tk()
ventana.title("Formulario de Médico")
ventana.geometry("500x600")
ventana.configure(bg="#f2f2f2")


def guardar_medico():
    ide = dato_entrada1.get()
    nombre = dato_entrada2.get()
    especialidad = dato_entrada3.get()
    tipo = dato_entrada4.get()
    sueldo = dato_entrada5.get()

    mensaje = (
        f"ID: {ide}\n"
        f"Nombre: {nombre}\n"
        f"Especialidad: {especialidad}\n"
        f"Tipo: {tipo}\n"
        f"Sueldo: {sueldo}"
    )
    resultado.config(text=mensaje, fg="white", bg="green")


titulo = Label(ventana, text="Formulario de Médico", fg="white", bg="black", font=("Verdana", 22))
titulo.pack(pady=15)

label_id = Label(ventana, text="Ingrese el ID del médico", fg="blue", font=("Verdana", 12))
label_id.pack()
dato_entrada1 = StringVar()
Entry(ventana, text=dato_entrada1, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_nom = Label(ventana, text="Ingrese el nombre", fg="blue", font=("Verdana", 12))
label_nom.pack()
dato_entrada2 = StringVar()
Entry(ventana, text=dato_entrada2, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_esp = Label(ventana, text="Ingrese la especialidad", fg="blue", font=("Verdana", 12))
label_esp.pack()
dato_entrada3 = StringVar()
Entry(ventana, text=dato_entrada3, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_tipo = Label(ventana, text="Ingrese el tipo", fg="blue", font=("Verdana", 12))
label_tipo.pack()
dato_entrada4 = StringVar()
Entry(ventana, text=dato_entrada4, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

label_sueldo = Label(ventana, text="Ingrese el sueldo", fg="blue", font=("Verdana", 12))
label_sueldo.pack()
dato_entrada5 = StringVar()
Entry(ventana, text=dato_entrada5, width=40, font=("Arial", 11)).pack(padx=10, pady=8)

boton = Button(ventana, text="Guardar Médico", command=guardar_medico, font=("Verdana", 12))
boton.pack(pady=12)

resultado = Label(ventana, text="", fg="white", bg="green", font=("Verdana", 12), justify="left")
resultado.pack(padx=12, pady=8, fill="x")

ventana.mainloop()
