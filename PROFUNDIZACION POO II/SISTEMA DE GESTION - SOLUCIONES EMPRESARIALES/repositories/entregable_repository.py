from models.entregable import Entregable

class EntregableRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entregables")
        filas = cursor.fetchall()
        cursor.close()
        return [Entregable(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11],f[12]) for f in filas]

    def select_WHERE_codigo(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entregables WHERE codigo = %s", (codigo,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Entregable(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12])
        return None

    def select_WHERE_proyecto(self, proyecto_numero):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entregables WHERE proyecto_numero = %s", (proyecto_numero,))
        filas = cursor.fetchall()
        cursor.close()
        return [Entregable(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11],f[12]) for f in filas]

    def insert(self, entregable):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO entregables VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (entregable.codigo, entregable.proyecto_numero, entregable.fase_codigo,
             entregable.titulo, entregable.tipo, entregable.descripcion,
             entregable.autor_principal_codigo, entregable.colaboradores,
             entregable.fecha_entrega_planificada, entregable.fecha_entrega_real,
             entregable.estado_revision, entregable.version_actual,
             entregable.aprobacion_cliente)
        )
        self.conn.commit()
        cursor.close()

    def update(self, entregable):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE entregables SET proyecto_numero=%s, fase_codigo=%s, titulo=%s,
               tipo=%s, descripcion=%s, autor_principal_codigo=%s, colaboradores=%s,
               fecha_entrega_planificada=%s, fecha_entrega_real=%s, estado_revision=%s,
               version_actual=%s, aprobacion_cliente=%s WHERE codigo=%s""",
            (entregable.proyecto_numero, entregable.fase_codigo, entregable.titulo,
             entregable.tipo, entregable.descripcion, entregable.autor_principal_codigo,
             entregable.colaboradores, entregable.fecha_entrega_planificada,
             entregable.fecha_entrega_real, entregable.estado_revision,
             entregable.version_actual, entregable.aprobacion_cliente, entregable.codigo)
        )
        self.conn.commit()
        cursor.close()

    def delete_entregable(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM entregables WHERE codigo = %s", (codigo,))
        self.conn.commit()
        cursor.close()
