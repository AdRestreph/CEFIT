from models.fase import Fase

class FaseRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM fases")
        filas = cursor.fetchall()
        cursor.close()
        return [Fase(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11],f[12],f[13]) for f in filas]

    def select_WHERE_codigo(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM fases WHERE codigo = %s", (codigo,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Fase(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12],fila[13])
        return None

    def select_WHERE_proyecto(self, proyecto_numero):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM fases WHERE proyecto_numero = %s", (proyecto_numero,))
        filas = cursor.fetchall()
        cursor.close()
        return [Fase(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11],f[12],f[13]) for f in filas]

    def insert(self, fase):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO fases VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (fase.codigo, fase.proyecto_numero, fase.nombre, fase.descripcion,
             fase.fecha_inicio_planificada, fase.fecha_inicio_real,
             fase.fecha_fin_planificada, fase.fecha_fin_real, fase.responsable_codigo,
             fase.entregables_asociados, fase.esfuerzo_estimado_horas,
             fase.recursos_necesarios, fase.dependencias, fase.porcentaje_avance)
        )
        self.conn.commit()
        cursor.close()

    def update(self, fase):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE fases SET proyecto_numero=%s, nombre=%s, descripcion=%s,
               fecha_inicio_planificada=%s, fecha_inicio_real=%s, fecha_fin_planificada=%s,
               fecha_fin_real=%s, responsable_codigo=%s, entregables_asociados=%s,
               esfuerzo_estimado_horas=%s, recursos_necesarios=%s, dependencias=%s,
               porcentaje_avance=%s WHERE codigo=%s""",
            (fase.proyecto_numero, fase.nombre, fase.descripcion,
             fase.fecha_inicio_planificada, fase.fecha_inicio_real,
             fase.fecha_fin_planificada, fase.fecha_fin_real, fase.responsable_codigo,
             fase.entregables_asociados, fase.esfuerzo_estimado_horas,
             fase.recursos_necesarios, fase.dependencias,
             fase.porcentaje_avance, fase.codigo)
        )
        self.conn.commit()
        cursor.close()

    def delete_fase(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM fases WHERE codigo = %s", (codigo,))
        self.conn.commit()
        cursor.close()
