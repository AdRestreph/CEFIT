from models.cliente import Cliente

class ClienteRepository:
    """Todas las consultas SQL de la tabla clientes van aqui."""

    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clientes")

        filas = cursor.fetchall()
        cursor.close()

        return [
            Cliente(
                codigo=f[0],
                tipo=f[1],
                razon_social=f[2],
                sector_actividad=f[3],
                ruc=f[4],
                direccion=f[5],
                telefono=f[6],
                sitio_web=f[7],
                contacto_principal=f[8],
                cargo_contacto=f[9],
                correo_electronico=f[10],
                telefono_directo=f[11],
                fecha_primera_relacion=f[12],
                origen_contacto=f[13],
                clasificacion_potencial=f[14]
            )
            for f in filas  # recorre cada fila y aplica lo de arriba
        ]

    def select_WHERE_codigo(self, codigo):
        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM clientes WHERE codigo = %s", (codigo,))

        fila = cursor.fetchone()
        cursor.close()

        if fila:
            return Cliente(
                codigo=fila[0], tipo=fila[1], razon_social=fila[2],
                sector_actividad=fila[3], ruc=fila[4], direccion=fila[5],
                telefono=fila[6], sitio_web=fila[7], contacto_principal=fila[8],
                cargo_contacto=fila[9], correo_electronico=fila[10],
                telefono_directo=fila[11], fecha_primera_relacion=fila[12],
                origen_contacto=fila[13], clasificacion_potencial=fila[14]
            )
        return None

    def insert(self, cliente):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO clientes (
                codigo, tipo, razon_social, sector_actividad, ruc,
                direccion, telefono, sitio_web, contacto_principal,
                cargo_contacto, correo_electronico, telefono_directo,
                fecha_primera_relacion, origen_contacto, clasificacion_potencial
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                cliente.codigo, cliente.tipo, cliente.razon_social,
                cliente.sector_actividad, cliente.ruc, cliente.direccion,
                cliente.telefono, cliente.sitio_web, cliente.contacto_principal,
                cliente.cargo_contacto, cliente.correo_electronico,
                cliente.telefono_directo, cliente.fecha_primera_relacion,
                cliente.origen_contacto, cliente.clasificacion_potencial
            )
        )
        self.conn.commit()  # confirma los cambios, sin esto no se guardan en la BD
        cursor.close()

    def update(self, cliente):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            UPDATE clientes SET
                tipo = %s, razon_social = %s, sector_actividad = %s,
                ruc = %s, direccion = %s, telefono = %s, sitio_web = %s,
                contacto_principal = %s, cargo_contacto = %s,
                correo_electronico = %s, telefono_directo = %s,
                fecha_primera_relacion = %s, origen_contacto = %s,
                clasificacion_potencial = %s
            WHERE codigo = %s
            """,
            (
                cliente.tipo, cliente.razon_social, cliente.sector_actividad,
                cliente.ruc, cliente.direccion, cliente.telefono,
                cliente.sitio_web, cliente.contacto_principal,
                cliente.cargo_contacto, cliente.correo_electronico,
                cliente.telefono_directo, cliente.fecha_primera_relacion,
                cliente.origen_contacto, cliente.clasificacion_potencial,
                cliente.codigo  # el WHERE va al final de la tupla
            )
        )
        self.conn.commit()
        cursor.close()

    # ─── ELIMINAR ─────────────────────────────────────────────
    def delete_cliente(self, codigo):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE codigo = %s", (codigo,))
        self.conn.commit()
        cursor.close()