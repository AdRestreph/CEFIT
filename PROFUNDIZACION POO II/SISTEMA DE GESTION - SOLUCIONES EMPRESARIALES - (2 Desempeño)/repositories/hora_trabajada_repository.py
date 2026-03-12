from models.hora_trabajada import HoraTrabajada

class HoraTrabajadaRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM horas_trabajadas")
        filas = cursor.fetchall()
        cursor.close()
        return [HoraTrabajada(consultor_codigo=f[1], proyecto_numero=f[2], fecha=f[3], horas_dedicadas=f[5], actividad_realizada=f[4], lugar=f[6], descripcion_detallada=f[7], resultados_obtenidos=f[8], dificultades=f[9], horas_facturables=f[10], id=f[0]) for f in filas]

    def select_WHERE_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM horas_trabajadas WHERE id = %s", (id,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return HoraTrabajada(consultor_codigo=fila[1], proyecto_numero=fila[2], fecha=fila[3], horas_dedicadas=fila[5], actividad_realizada=fila[4], lugar=fila[6], descripcion_detallada=fila[7], resultados_obtenidos=fila[8], dificultades=fila[9], horas_facturables=fila[10], id=fila[0])
        return None

    def select_WHERE_consultor(self, consultor_codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM horas_trabajadas WHERE consultor_codigo = %s", (consultor_codigo,))
        filas = cursor.fetchall()
        cursor.close()
        return [HoraTrabajada(consultor_codigo=f[1], proyecto_numero=f[2], fecha=f[3], horas_dedicadas=f[5], actividad_realizada=f[4], lugar=f[6], descripcion_detallada=f[7], resultados_obtenidos=f[8], dificultades=f[9], horas_facturables=f[10], id=f[0]) for f in filas]

    def select_WHERE_proyecto(self, proyecto_numero):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM horas_trabajadas WHERE proyecto_numero = %s", (proyecto_numero,))
        filas = cursor.fetchall()
        cursor.close()
        return [HoraTrabajada(consultor_codigo=f[1], proyecto_numero=f[2], fecha=f[3], horas_dedicadas=f[5], actividad_realizada=f[4], lugar=f[6], descripcion_detallada=f[7], resultados_obtenidos=f[8], dificultades=f[9], horas_facturables=f[10], id=f[0]) for f in filas]

    def insert(self, hora):
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO horas_trabajadas (consultor_codigo, proyecto_numero, fecha,
               actividad_realizada, horas_dedicadas, lugar, descripcion_detallada,
               resultados_obtenidos, dificultades, horas_facturables)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (hora.consultor_codigo, hora.proyecto_numero, hora.fecha,
             hora.actividad_realizada, hora.horas_dedicadas, hora.lugar,
             hora.descripcion_detallada, hora.resultados_obtenidos,
             hora.dificultades, hora.horas_facturables)
        )
        self.conn.commit()
        cursor.close()

    def update(self, hora):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE horas_trabajadas SET consultor_codigo=%s, proyecto_numero=%s,
               fecha=%s, actividad_realizada=%s, horas_dedicadas=%s, lugar=%s,
               descripcion_detallada=%s, resultados_obtenidos=%s, dificultades=%s,
               horas_facturables=%s WHERE id=%s""",
            (hora.consultor_codigo, hora.proyecto_numero, hora.fecha,
             hora.actividad_realizada, hora.horas_dedicadas, hora.lugar,
             hora.descripcion_detallada, hora.resultados_obtenidos,
             hora.dificultades, hora.horas_facturables, hora.id)
        )
        self.conn.commit()
        cursor.close()

    def delete_hora_trabajada(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM horas_trabajadas WHERE id = %s", (id,))
        self.conn.commit()
        cursor.close()
