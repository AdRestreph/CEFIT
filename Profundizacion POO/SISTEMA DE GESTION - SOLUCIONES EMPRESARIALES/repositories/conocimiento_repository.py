from models.conocimiento import Conocimiento

class ConocimientoRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM conocimiento")
        filas = cursor.fetchall()
        cursor.close()
        return [Conocimiento(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10]) for f in filas]

    def select_WHERE_codigo(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM conocimiento WHERE codigo = %s", (codigo,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Conocimiento(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10])
        return None

    def select_WHERE_autor(self, autor_codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM conocimiento WHERE autor_codigo = %s", (autor_codigo,))
        filas = cursor.fetchall()
        cursor.close()
        return [Conocimiento(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10]) for f in filas]

    def insert(self, conocimiento):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO conocimiento VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (conocimiento.codigo, conocimiento.titulo, conocimiento.tipo,
             conocimiento.industria, conocimiento.autor_codigo, conocimiento.fecha_creacion,
             conocimiento.descripcion, conocimiento.palabras_clave,
             conocimiento.archivo_adjunto, conocimiento.nivel_acceso,
             conocimiento.potencial_reutilizacion)
        )
        self.conn.commit()
        cursor.close()

    def update(self, conocimiento):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE conocimiento SET titulo=%s, tipo=%s, industria=%s, autor_codigo=%s,
               fecha_creacion=%s, descripcion=%s, palabras_clave=%s, archivo_adjunto=%s,
               nivel_acceso=%s, potencial_reutilizacion=%s WHERE codigo=%s""",
            (conocimiento.titulo, conocimiento.tipo, conocimiento.industria,
             conocimiento.autor_codigo, conocimiento.fecha_creacion, conocimiento.descripcion,
             conocimiento.palabras_clave, conocimiento.archivo_adjunto,
             conocimiento.nivel_acceso, conocimiento.potencial_reutilizacion,
             conocimiento.codigo)
        )
        self.conn.commit()
        cursor.close()

    def delete_conocimiento(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM conocimiento WHERE codigo = %s", (codigo,))
        self.conn.commit()
        cursor.close()
