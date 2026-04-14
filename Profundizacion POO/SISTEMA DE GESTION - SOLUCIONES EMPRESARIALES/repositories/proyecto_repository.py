from models.proyecto import Proyecto

class ProyectoRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proyectos")
        filas = cursor.fetchall()
        cursor.close()
        return [Proyecto(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11]) for f in filas]

    def select_WHERE_numero(self, numero):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proyectos WHERE numero = %s", (numero,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Proyecto(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11])
        return None

    def select_WHERE_cliente(self, cliente_codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proyectos WHERE cliente_codigo = %s", (cliente_codigo,))
        filas = cursor.fetchall()
        cursor.close()
        return [Proyecto(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11]) for f in filas]

    def insert(self, proyecto):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO proyectos VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (proyecto.numero, proyecto.titulo, proyecto.cliente_codigo,
             proyecto.servicio_codigo, proyecto.alcance, proyecto.objetivos,
             proyecto.fecha_inicio, proyecto.duracion_prevista_dias,
             proyecto.presupuesto_aprobado, proyecto.fases_principales,
             proyecto.estado, proyecto.nivel_confidencialidad)
        )
        self.conn.commit()
        cursor.close()

    def update(self, proyecto):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE proyectos SET titulo=%s, cliente_codigo=%s, servicio_codigo=%s,
               alcance=%s, objetivos=%s, fecha_inicio=%s, duracion_prevista_dias=%s,
               presupuesto_aprobado=%s, fases_principales=%s, estado=%s,
               nivel_confidencialidad=%s WHERE numero=%s""",
            (proyecto.titulo, proyecto.cliente_codigo, proyecto.servicio_codigo,
             proyecto.alcance, proyecto.objetivos, proyecto.fecha_inicio,
             proyecto.duracion_prevista_dias, proyecto.presupuesto_aprobado,
             proyecto.fases_principales, proyecto.estado,
             proyecto.nivel_confidencialidad, proyecto.numero)
        )
        self.conn.commit()
        cursor.close()

    def delete_proyecto(self, numero):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM proyectos WHERE numero = %s", (numero,))
        self.conn.commit()
        cursor.close()
