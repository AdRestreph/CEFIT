from models.consultor import Consultor


class ConsultorRepository:

    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.callproc("sp_GetAllConsultores")
        filas = next(cursor.stored_results()).fetchall()
        cursor.close()
        # codigo_empleado, nombres, apellidos, nivel, especialidades, tarifa_horaria, disponibilidad
        return [
            Consultor(
                codigo_empleado=f[0], nombres=f[1], apellidos=f[2],
                nivel=f[3], especialidades=f[4], tarifa_horaria=f[5],
                disponibilidad=f[6]
            )
            for f in filas
        ]

    def select_WHERE_codigo_empleado(self, codigo_empleado):
        cursor = self.conn.cursor()
        cursor.callproc("sp_GetConsultor", [codigo_empleado])
        fila = next(cursor.stored_results()).fetchone()
        cursor.close()
        if fila:
            return Consultor(
                codigo_empleado=fila[0], nombres=fila[1], apellidos=fila[2],
                documento_identidad=fila[3], formacion_academica=fila[4],
                certificaciones=fila[5], especialidades=fila[6],
                anios_experiencia=fila[7], nivel=fila[8], tarifa_horaria=fila[9],
                idiomas=fila[10], disponibilidad=fila[11]
            )
        return None

    def search(self, termino):
        cursor = self.conn.cursor()
        cursor.callproc("sp_SearchConsultores", [termino])
        filas = next(cursor.stored_results()).fetchall()
        cursor.close()
        return [
            Consultor(
                codigo_empleado=f[0], nombres=f[1], apellidos=f[2],
                nivel=f[3], especialidades=f[4], tarifa_horaria=f[5],
                disponibilidad=f[6]
            )
            for f in filas
        ]

    def select_disponibles(self):
        cursor = self.conn.cursor()
        cursor.callproc("sp_GetConsultoresDisponibles")
        filas = next(cursor.stored_results()).fetchall()
        cursor.close()
        return [
            Consultor(
                codigo_empleado=f[0], nombres=f[1],
                nivel=f[2], especialidades=f[3], tarifa_horaria=f[4]
            )
            for f in filas
        ]

    def insert(self, consultor):
        cursor = self.conn.cursor()
        cursor.callproc("sp_InsertConsultor", [
            consultor.codigo_empleado, consultor.nombres, consultor.apellidos,
            consultor.documento_identidad, consultor.formacion_academica,
            consultor.certificaciones, consultor.especialidades,
            consultor.anios_experiencia, consultor.nivel, consultor.tarifa_horaria,
            consultor.idiomas, consultor.disponibilidad
        ])
        self.conn.commit()
        cursor.close()

    def update(self, consultor):
        cursor = self.conn.cursor()
        cursor.callproc("sp_UpdateConsultor", [
            consultor.codigo_empleado, consultor.nombres, consultor.apellidos,
            consultor.formacion_academica, consultor.certificaciones,
            consultor.especialidades, consultor.anios_experiencia,
            consultor.nivel, consultor.tarifa_horaria,
            consultor.idiomas, consultor.disponibilidad
        ])
        self.conn.commit()
        cursor.close()

    def delete_consultor(self, codigo_empleado):
        cursor = self.conn.cursor()
        try:
            cursor.callproc("sp_DeleteConsultor", [codigo_empleado])
            self.conn.commit()
        except Exception as e:
            raise Exception(str(e))
        finally:
            cursor.close()