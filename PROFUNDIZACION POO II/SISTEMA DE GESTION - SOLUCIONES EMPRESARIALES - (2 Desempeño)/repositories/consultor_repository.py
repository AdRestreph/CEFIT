from models.consultor import Consultor

class ConsultorRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM consultores")
        filas = cursor.fetchall()
        cursor.close()
        return [Consultor(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11]) for f in filas]

    def select_WHERE_codigo_empleado(self, codigo_empleado):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM consultores WHERE codigo_empleado = %s", (codigo_empleado,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Consultor(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11])
        return None

    def insert(self, consultor):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO consultores VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (consultor.codigo_empleado, consultor.nombres, consultor.apellidos,
             consultor.documento_identidad, consultor.formacion_academica,
             consultor.certificaciones, consultor.especialidades,
             consultor.anios_experiencia, consultor.nivel, consultor.tarifa_horaria,
             consultor.idiomas, consultor.disponibilidad)
        )
        self.conn.commit()
        cursor.close()

    def update(self, consultor):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE consultores SET nombres=%s, apellidos=%s, documento_identidad=%s,
               formacion_academica=%s, certificaciones=%s, especialidades=%s,
               anios_experiencia=%s, nivel=%s, tarifa_horaria=%s, idiomas=%s,
               disponibilidad=%s WHERE codigo_empleado=%s""",
            (consultor.nombres, consultor.apellidos, consultor.documento_identidad,
             consultor.formacion_academica, consultor.certificaciones,
             consultor.especialidades, consultor.anios_experiencia, consultor.nivel,
             consultor.tarifa_horaria, consultor.idiomas, consultor.disponibilidad,
             consultor.codigo_empleado)
        )
        self.conn.commit()
        cursor.close()

    def delete_consultor(self, codigo_empleado):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM consultores WHERE codigo_empleado = %s", (codigo_empleado,))
        self.conn.commit()
        cursor.close()
