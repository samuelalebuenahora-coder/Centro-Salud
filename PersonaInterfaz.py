from tkinter import *


ventana = Tk()
ventana.title("Formulario de Persona")
ventana.geometry("500x700")
ventana.configure(bg="#f2f2f2")


def guardar_persona():
    ide = dato_entrada1.get()
    nombre = dato_entrada2.get()
    anio = dato_entrada3.get()
    mes = dato_entrada4.get()
    dia = dato_entrada5.get()
    genero = dato_entrada6.get()
    direccion = dato_entrada7.get()
    codigo = dato_entrada8.get()

    mensaje = (
        f"ID: {ide}\n"
        f"Nombre: {nombre}\n"
        f"Fecha: {anio}-{mes}-{dia}\n"
        f"Género: {genero}\n"
        f"Dirección: {direccion}\n"
        f"Código postal: {codigo}"
    )
    resultado.config(text=mensaje, fg="white", bg="green")


titulo = Label(
    ventana,
    text="Formulario de Persona",
    fg="white",
    bg="black",
    font=("Verdana", 22),
)
titulo.pack(pady=15)

label_id = Label(ventana, text="Ingrese su identificación", fg="blue", font=("Verdana", 12))
label_id.pack()
dato_entrada1 = StringVar()
entrada1 = Entry(ventana, text=dato_entrada1, width=40, font=("Arial", 11))
entrada1.pack(padx=10, pady=8)

label_nom = Label(ventana, text="Ingrese su nombre", fg="blue", font=("Verdana", 12))
label_nom.pack()
dato_entrada2 = StringVar()
entrada2 = Entry(ventana, text=dato_entrada2, width=40, font=("Arial", 11))
entrada2.pack(padx=10, pady=8)

label_an = Label(ventana, text="Ingrese su año de nacimiento", fg="blue", font=("Verdana", 12))
label_an.pack()
dato_entrada3 = StringVar()
entrada3 = Entry(ventana, text=dato_entrada3, width=40, font=("Arial", 11))
entrada3.pack(padx=10, pady=8)

label_mes = Label(ventana, text="Ingrese su mes de nacimiento", fg="blue", font=("Verdana", 12))
label_mes.pack()
dato_entrada4 = StringVar()
entrada4 = Entry(ventana, text=dato_entrada4, width=40, font=("Arial", 11))
entrada4.pack(padx=10, pady=8)

label_dia = Label(ventana, text="Ingrese su día de nacimiento", fg="blue", font=("Verdana", 12))
label_dia.pack()
dato_entrada5 = StringVar()
entrada5 = Entry(ventana, text=dato_entrada5, width=40, font=("Arial", 11))
entrada5.pack(padx=10, pady=8)

label_gen = Label(ventana, text="Ingrese su género", fg="blue", font=("Verdana", 12))
label_gen.pack()
dato_entrada6 = StringVar()
entrada6 = Entry(ventana, text=dato_entrada6, width=40, font=("Arial", 11))
entrada6.pack(padx=10, pady=8)

label_dir = Label(ventana, text="Ingrese su dirección", fg="blue", font=("Verdana", 12))
label_dir.pack()
dato_entrada7 = StringVar()
entrada7 = Entry(ventana, text=dato_entrada7, width=40, font=("Arial", 11))
entrada7.pack(padx=10, pady=8)

label_cod = Label(ventana, text="Ingrese su código postal", fg="blue", font=("Verdana", 12))
label_cod.pack()
dato_entrada8 = StringVar()
entrada8 = Entry(ventana, text=dato_entrada8, width=40, font=("Arial", 11))
entrada8.pack(padx=10, pady=8)

boton = Button(ventana, text="Guardar Persona", command=guardar_persona, font=("Verdana", 12))
boton.pack(pady=12)

resultado = Label(ventana, text="", fg="white", bg="green", font=("Verdana", 12), justify="left")
resultado.pack(padx=12, pady=8, fill="x")

ventana.mainloop()
