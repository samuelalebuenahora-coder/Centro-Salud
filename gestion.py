import re

from persona import persona
from medico import medico
from paciente import Paciente
from horario import Horario
from cita import Cita


class CentroSalud:
    def __init__(self):
        self.personas = []
        self.medicos = []
        self.pacientes = []
        self.horarios = []
        self.citas = []

    def agregar_persona(self, ide, nombre):
        p = persona(ide, nombre)
        if any(x.get_ide() == p.get_ide() for x in self.personas):
            raise ValueError("La identificación ya existe.")
        self.personas.append(p)
        return p

    def agregar_medico(self, ide, nombre, especialidad, tipo, sueldo):
        m = medico(ide, nombre, especialidad, tipo, sueldo)
        if any(x.get_ide() == m.get_ide() for x in self.medicos):
            raise ValueError("El médico ya existe.")
        self.medicos.append(m)
        return m

    def agregar_paciente(self, ide, nombre, edad, sexo, estado_salud, tipo_cita):
        p = Paciente(ide, nombre, edad, sexo, estado_salud, tipo_cita)

        if any(x.get_ide() == p.get_ide() for x in self.pacientes):
            raise ValueError("El paciente ya existe.")

        self.pacientes.append(p)
        p.guardar_en_archivo()

        return p

    def agregar_horario(self, id_medico, dia, hora):
        medico_actual = next(
            (x for x in self.medicos if x.get_ide() == id_medico),
            None,
        )
        if medico_actual is None:
            raise ValueError("No existe ese médico.")

        if not re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", hora):
            raise ValueError("Usa la hora HH:MM, por ejemplo 11:00.")

        if any(
            h.get_medico() is medico_actual and h.get_dia() == dia and h.get_hora() == hora
            for h in self.horarios
        ):
            raise ValueError("Ese horario ya existe.")

        horario = Horario(medico_actual, hora, dia, True)
        self.horarios.append(horario)
        return horario

    def agregar_cita(self, id_paciente, id_medico, dia, hora):
        paciente = next((x for x in self.pacientes if x.get_ide() == id_paciente), None)
        medico_actual = next((x for x in self.medicos if x.get_ide() == id_medico), None)

        if paciente is None or medico_actual is None:
            raise ValueError("Verifica el ID del paciente y del médico.")

        horario = next(
            (
                x
                for x in self.horarios
                if x.get_medico() is medico_actual and x.get_dia() == dia and x.get_hora() == hora
            ),
            None,
        )

        if horario is None:
            raise ValueError("No existe ese horario para el médico.")
        cita = Cita(paciente, medico_actual, horario)
        if not cita.programar_cita():
            raise ValueError("El horario está ocupado o no es válido.")

        self.citas.append(cita)
        return cita

    def cancelar_cita(self, indice):
        if indice < 0 or indice >= len(self.citas):
            raise ValueError("Selecciona una cita válida.")

        cita = self.citas[indice]
        if cita.cancelar_cita():
            return cita
        raise ValueError("La cita no está programada.")

    def datos_para_listas(self):
        return {
            "personas": [p.mostrarinformacion() for p in self.personas],
            "medicos": [
                f"{m.get_ide()} | {m.get_nombres()} | {m.get_esp()} | {m.get_tipo()}"
                for m in self.medicos
            ],
            "pacientes": [
                f"{p.get_ide()} | {p.get_nombres()} | Edad: {p.get_edad()} | Salud: {p.get_estado_salud()}"
                for p in self.pacientes
            ],
            "horarios": [h.mostrar_horario() for h in self.horarios],
            "citas": [c.mostrar_cita() for c in self.citas],
        }
