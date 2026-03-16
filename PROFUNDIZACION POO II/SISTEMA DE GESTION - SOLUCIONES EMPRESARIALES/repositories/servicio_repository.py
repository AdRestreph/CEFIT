from models.servicio import Servicio


class ServicioRepository:

    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.callproc("sp_GetAllServicios")
        filas = next(cursor.stored_results()).fetchall()
        cursor.close()
        # codigo, nombre_comercial, categoria, duracion_estimada, tarifario_referencial
        return [
            Servicio(
                codigo=f[0], nombre_comercial=f[1], categoria=f[2],
                duracion_estimada=f[3], tarifario_referencial=f[4]
            )
            for f in filas
        ]

    def select_WHERE_codigo(self, codigo):
        cursor = self.conn.cursor()
        cursor.callproc("sp_GetServicio", [codigo])
        fila = next(cursor.stored_results()).fetchone()
        cursor.close()
        if fila:
            return Servicio(
                codigo=fila[0], nombre_comercial=fila[1], categoria=fila[2],
                descripcion=fila[3], entregables_tipicos=fila[4],
                duracion_estimada=fila[5], metodologia=fila[6],
                beneficios_cliente=fila[7], equipo_minimo=fila[8],
                tarifario_referencial=fila[9], casos_exito=fila[10]
            )
        return None

    def search(self, termino):
        cursor = self.conn.cursor()
        cursor.callproc("sp_SearchServicios", [termino])
        filas = next(cursor.stored_results()).fetchall()
        cursor.close()
        return [
            Servicio(
                codigo=f[0], nombre_comercial=f[1], categoria=f[2],
                duracion_estimada=f[3], tarifario_referencial=f[4]
            )
            for f in filas
        ]

    def insert(self, servicio):
        cursor = self.conn.cursor()
        cursor.callproc("sp_InsertServicio", [
            servicio.codigo, servicio.nombre_comercial, servicio.categoria,
            servicio.descripcion, servicio.entregables_tipicos,
            servicio.duracion_estimada, servicio.metodologia,
            servicio.beneficios_cliente, servicio.equipo_minimo,
            servicio.tarifario_referencial, servicio.casos_exito
        ])
        self.conn.commit()
        cursor.close()

    def update(self, servicio):
        cursor = self.conn.cursor()
        cursor.callproc("sp_UpdateServicio", [
            servicio.codigo, servicio.nombre_comercial, servicio.categoria,
            servicio.descripcion, servicio.duracion_estimada,
            servicio.metodologia, servicio.tarifario_referencial
        ])
        self.conn.commit()
        cursor.close()

    def delete_servicio(self, codigo):
        cursor = self.conn.cursor()
        try:
            cursor.callproc("sp_DeleteServicio", [codigo])
            self.conn.commit()
        except Exception as e:
            raise Exception(str(e))
        finally:
            cursor.close()