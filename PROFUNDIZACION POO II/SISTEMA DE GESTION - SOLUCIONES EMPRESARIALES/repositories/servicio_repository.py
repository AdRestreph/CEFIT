from models.servicio import Servicio

class ServicioRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM servicios")
        filas = cursor.fetchall()
        cursor.close()
        return [Servicio(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10]) for f in filas]

    def select_WHERE_codigo(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM servicios WHERE codigo = %s", (codigo,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Servicio(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10])
        return None

    def insert(self, servicio):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO servicios VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (servicio.codigo, servicio.nombre_comercial, servicio.categoria,
             servicio.descripcion, servicio.entregables_tipicos, servicio.duracion_estimada,
             servicio.metodologia, servicio.beneficios_cliente, servicio.equipo_minimo,
             servicio.tarifario_referencial, servicio.casos_exito)
        )
        self.conn.commit()
        cursor.close()

    def update(self, servicio):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE servicios SET nombre_comercial=%s, categoria=%s, descripcion=%s,
               entregables_tipicos=%s, duracion_estimada=%s, metodologia=%s,
               beneficios_cliente=%s, equipo_minimo=%s, tarifario_referencial=%s,
               casos_exito=%s WHERE codigo=%s""",
            (servicio.nombre_comercial, servicio.categoria, servicio.descripcion,
             servicio.entregables_tipicos, servicio.duracion_estimada, servicio.metodologia,
             servicio.beneficios_cliente, servicio.equipo_minimo, servicio.tarifario_referencial,
             servicio.casos_exito, servicio.codigo)
        )
        self.conn.commit()
        cursor.close()

    def delete_servicio(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM servicios WHERE codigo = %s", (codigo,))
        self.conn.commit()
        cursor.close()
