from models.proyecto_consultor import ProyectoConsultor

class ProyectoConsultorRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proyecto_consultores")
        filas = cursor.fetchall()
        cursor.close()
        return [ProyectoConsultor(proyecto_numero=f[1], consultor_codigo=f[2], rol=f[3], dedicacion_porcentaje=f[4], id=f[0]) for f in filas]

    def select_WHERE_proyecto(self, proyecto_numero):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proyecto_consultores WHERE proyecto_numero = %s", (proyecto_numero,))
        filas = cursor.fetchall()
        cursor.close()
        return [ProyectoConsultor(proyecto_numero=f[1], consultor_codigo=f[2], rol=f[3], dedicacion_porcentaje=f[4], id=f[0]) for f in filas]

    def select_WHERE_consultor(self, consultor_codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proyecto_consultores WHERE consultor_codigo = %s", (consultor_codigo,))
        filas = cursor.fetchall()
        cursor.close()
        return [ProyectoConsultor(proyecto_numero=f[1], consultor_codigo=f[2], rol=f[3], dedicacion_porcentaje=f[4], id=f[0]) for f in filas]

    def insert(self, pc):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO proyecto_consultores (proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje) VALUES (%s,%s,%s,%s)",
            (pc.proyecto_numero, pc.consultor_codigo, pc.rol, pc.dedicacion_porcentaje)
        )
        self.conn.commit()
        cursor.close()

    def update(self, pc):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE proyecto_consultores SET rol=%s, dedicacion_porcentaje=%s WHERE id=%s",
            (pc.rol, pc.dedicacion_porcentaje, pc.id)
        )
        self.conn.commit()
        cursor.close()

    def delete_proyecto_consultor(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM proyecto_consultores WHERE id = %s", (id,))
        self.conn.commit()
        cursor.close()
