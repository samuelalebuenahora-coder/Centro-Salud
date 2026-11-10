class Cita:
    def __init__(self, paciente, medico, horario):
        if paciente is None or medico is None or horario is None:
            raise ValueError(
                "La cita requiere paciente, médico y horario."
            )

        self.__paciente = paciente
        self.__medico = medico
        self.__horario = horario
        self.__estado = "Pendiente"

    def get_paciente(self):
        return self.__paciente

    def get_medico(self):
        return self.__medico

    def get_horario(self):
        return self.__horario

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        estados = ("Pendiente", "Programada", "Cancelada")
        if estado not in estados:
            raise ValueError("Estado de cita no válido.")
        self.__estado = estado

    def programar_cita(self):
        # BLOQUE 1: comprobar que el horario
        # pertenece al médico asignado.
        if self.__horario.get_medico() is not self.__medico:
            return False

        # Evitar programar dos veces la misma cita.
        if self.__estado != "Pendiente":
            return False

        # BLOQUE 2: comprobar disponibilidad.
        if not self.__horario.get_disp():
            return False

        # BLOQUE 3: actualizar horario y relaciones.
        self.__horario.set_disp(False)
        self.__paciente.agregar_cita(self)
        self.__medico.agregar_cita(self)

        # BLOQUE 4: establecer el estado.
        self.__estado = "Programada"
        return True

    def cancelar_cita(self):
        # BLOQUE 1: validar el estado.
        if self.__estado != "Programada":
            return False

        # BLOQUE 2: cancelar y liberar horario.
        self.__estado = "Cancelada"
        self.__horario.set_disp(True)

        # BLOQUE 3: actualizar las listas.
        self.__paciente.eliminar_cita(self)
        self.__medico.eliminar_cita(self)

        # BLOQUE 4: confirmar operación.
        return True

    def mostrar_cita(self):
        horario = self.__horario
        return (
            f"Paciente: {self.__paciente.get_nombres()} | "
            f"Médico: {self.__medico.get_nombres()} | "
            f"{horario.get_dia()} {horario.get_hora()} | "
            f"Estado: {self.__estado}"
        )