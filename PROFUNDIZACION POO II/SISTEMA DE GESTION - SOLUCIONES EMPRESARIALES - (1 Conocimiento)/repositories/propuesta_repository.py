from models.propuesta import Propuesta

class PropuestaRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM propuestas")
        filas = cursor.fetchall()
        cursor.close()
        return [Propuesta(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11]) for f in filas]

    def select_WHERE_numero(self, numero):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM propuestas WHERE numero = %s", (numero,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Propuesta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11])
        return None

    def select_WHERE_cliente(self, cliente_codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM propuestas WHERE cliente_codigo = %s", (cliente_codigo,))
        filas = cursor.fetchall()
        cursor.close()
        return [Propuesta(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11]) for f in filas]

    def insert(self, propuesta):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO propuestas VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (propuesta.numero, propuesta.fecha_presentacion, propuesta.cliente_codigo,
             propuesta.titulo, propuesta.servicios_incluidos, propuesta.enfoque_metodologico,
             propuesta.equipo_propuesto, propuesta.cronograma_tentativo,
             propuesta.inversion_requerida, propuesta.condiciones_comerciales,
             propuesta.validez_dias, propuesta.estado)
        )
        self.conn.commit()
        cursor.close()

    def update(self, propuesta):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE propuestas SET fecha_presentacion=%s, cliente_codigo=%s, titulo=%s,
               servicios_incluidos=%s, enfoque_metodologico=%s, equipo_propuesto=%s,
               cronograma_tentativo=%s, inversion_requerida=%s, condiciones_comerciales=%s,
               validez_dias=%s, estado=%s WHERE numero=%s""",
            (propuesta.fecha_presentacion, propuesta.cliente_codigo, propuesta.titulo,
             propuesta.servicios_incluidos, propuesta.enfoque_metodologico,
             propuesta.equipo_propuesto, propuesta.cronograma_tentativo,
             propuesta.inversion_requerida, propuesta.condiciones_comerciales,
             propuesta.validez_dias, propuesta.estado, propuesta.numero)
        )
        self.conn.commit()
        cursor.close()

    def delete_propuesta(self, numero):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM propuestas WHERE numero = %s", (numero,))
        self.conn.commit()
        cursor.close()
