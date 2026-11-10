from persona import persona


class medico(persona):
    def __init__(self, ide, nombres, esp, tipo, sueldo):
        super().__init__(ide, nombres)
        self.__esp = esp
        self.__tipo = tipo
        self.__sueldo = 0
        self.set_sueldo(sueldo)
        self.__horarios = []
        self.__citas = []

    def get_esp(self):
        return self.__esp

    def set_esp(self, esp):
        if not str(esp).strip():
            raise ValueError("La especialidad es obligatoria.")
        self.__esp = str(esp).strip()

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        if not str(tipo).strip():
            raise ValueError("El tipo de médico es obligatorio.")
        self.__tipo = str(tipo).strip()

    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, sueldo):
        sueldo = float(sueldo)
        if sueldo < 0:
            raise ValueError("El sueldo no puede ser negativo.")
        self.__sueldo = sueldo

    def get_horarios(self):
        return self.__horarios.copy()

    def get_citas(self):
        return self.__citas.copy()

    def agregar_horario(self, horario):
        if horario not in self.__horarios:
            self.__horarios.append(horario)

    def agregar_cita(self, cita):
        if cita not in self.__citas:
            self.__citas.append(cita)

    def eliminar_cita(self, cita):
        if cita in self.__citas:
            self.__citas.remove(cita)

    def ver_horarios(self):
        return [
            horario.mostrar_horario()
            for horario in self.__horarios
        ]

    def atender_paciente(self, paciente):
        return (
            f"El médico {self.get_nombres()} "
            f"está atendiendo al paciente "
            f"{paciente.get_nombres()}."
        )

    def calcularsueldoannio(self):
        return self.__sueldo * 12

    def verificardisponbilidad(self, hora, dia):
        for horario in self.__horarios:
            if horario.get_hora() == hora and horario.get_dia() == dia:
                return horario.get_disp()
        return False
