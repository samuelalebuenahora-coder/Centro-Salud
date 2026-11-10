from persona import persona
from pathlib import Path


class Paciente(persona):
    def __init__(
        self, ide, nombres, edad, sexo,
        estado_salud, tipo_cita
    ):
        super().__init__(ide, nombres)

        self.__edad = 0
        self.set_edad(edad)
        self.set_sexo(sexo)
        self.set_estado_salud(estado_salud)
        self.set_tipo_cita(tipo_cita)
        self.__citas = []

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        edad = int(edad)
        if edad <= 0:
            raise ValueError("La edad debe ser mayor que cero.")
        self.__edad = edad

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        if not str(sexo).strip():
            raise ValueError("El sexo es obligatorio.")
        self.__sexo = str(sexo).strip()

    def get_estado_salud(self):
        return self.__estado_salud

    def set_estado_salud(self, estado_salud):
        if not str(estado_salud).strip():
            raise ValueError("El estado de salud es obligatorio.")
        self.__estado_salud = str(estado_salud).strip()

    def get_tipo_cita(self):
        return self.__tipo_cita

    def set_tipo_cita(self, tipo_cita):
        if not str(tipo_cita).strip():
            raise ValueError("El tipo de cita es obligatorio.")
        self.__tipo_cita = str(tipo_cita).strip()

    def get_citas(self):
        return self.__citas.copy()

    def agregar_cita(self, cita):
        if cita not in self.__citas:
            self.__citas.append(cita)

    def eliminar_cita(self, cita):
        if cita in self.__citas:
            self.__citas.remove(cita)

    def consultar_estado_salud(self):
        return self.__estado_salud

    # Guarda los datos del paciente en un archivo de texto
    def guardar_en_archivo(self):
        archivo = Path(__file__).resolve().parent / "Paciente.txt"

        with open(archivo, "a", encoding="utf-8") as documento:
            documento.write(
                f"ID: {self.get_ide()}\n"
                f"Nombre: {self.get_nombres()}\n"
                f"Edad: {self.__edad}\n"
                f"Sexo: {self.__sexo}\n"
                f"Estado de salud: {self.__estado_salud}\n"
                f"Tipo de cita: {self.__tipo_cita}\n"
                "-----------------------------\n"
            )

    # Consulta los registros almacenados
    @staticmethod
    def consultar_archivo():
        archivo = Path(__file__).resolve().parent / "Paciente.txt"

        if not archivo.exists():
            return "Todavía no existen pacientes registrados."

        with open(archivo, "r", encoding="utf-8") as documento:
            return documento.read()