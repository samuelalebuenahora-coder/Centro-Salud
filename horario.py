class Horario:
    def __init__(self, medico, hora, dia, disp=True):
        self.__medico = medico
        self.set_hora(hora)
        self.set_dia(dia)
        self.set_disp(disp)

        self.__medico.agregar_horario(self)

    def get_medico(self):
        return self.__medico

    def set_medico(self, medico):
        if medico is None:
            raise ValueError("Debe asignarse un médico.")
        if self.__medico is not medico:
            raise ValueError(
                "No se puede cambiar el médico de un horario creado."
            )

    def get_hora(self):
        return self.__hora

    def set_hora(self, hora):
        if not str(hora).strip():
            raise ValueError("La hora es obligatoria.")
        self.__hora = str(hora).strip()

    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        if not str(dia).strip():
            raise ValueError("El día es obligatorio.")
        self.__dia = str(dia).strip()

    def get_disp(self):
        return self.__disp

    def set_disp(self, disp):
        if not isinstance(disp, bool):
            raise ValueError("La disponibilidad debe ser True o False.")
        self.__disp = disp

    def verificar_disponibilidad(self):
        return self.__disp

    def mostrar_horario(self):
        estado = "Disponible" if self.__disp else "Ocupado"
        return (
            f"{self.__dia} - {self.__hora} "
            f"- Médico: {self.__medico.get_nombres()} "
            f"- {estado}"
        )
