class persona:
    def __init__(self, ide, nombres):
        self.__ide = ide
        self.__nombres = nombres

    def get_ide(self):
        return self.__ide

    def set_ide(self, ide):
        if not str(ide).strip():
            raise ValueError("El ID no puede estar vacío.")
        self.__ide = str(ide).strip()

    def get_nombres(self):
        return self.__nombres

    def set_nombres(self, nombres):
        if not str(nombres).strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombres = str(nombres).strip()

    def mostrarinformacion(self):
        return f"Nombre: {self.__nombres} | ID: {self.__ide}"
