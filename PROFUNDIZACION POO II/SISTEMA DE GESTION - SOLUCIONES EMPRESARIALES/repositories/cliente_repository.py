from models.cliente import Cliente


class ClienteRepository:

    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.callproc("sp_GetAllClientes")
        filas = next(cursor.stored_results()).fetchall()
        cursor.close()
        return [
            Cliente(
                codigo=f[0], tipo=f[1], razon_social=f[2],
                sector_actividad=f[3], ruc=f[4], direccion=f[5],
                telefono=f[6], sitio_web=f[7], contacto_principal=f[8],
                cargo_contacto=f[9], correo_electronico=f[10],
                telefono_directo=f[11], fecha_primera_relacion=f[12],
                origen_contacto=f[13], clasificacion_potencial=f[14]
            )
            for f in filas
        ]

    def select_WHERE_codigo(self, codigo):
        cursor = self.conn.cursor()
        cursor.callproc("sp_GetCliente", [codigo])
        fila = next(cursor.stored_results()).fetchone()
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

    def search(self, termino):
        cursor = self.conn.cursor()
        cursor.callproc("sp_SearchClientes", [termino])
        filas = next(cursor.stored_results()).fetchall()
        cursor.close()
        return [
            Cliente(
                codigo=f[0], tipo=f[1], razon_social=f[2],
                sector_actividad=f[3], contacto_principal=f[4],
                correo_electronico=f[5], clasificacion_potencial=f[6]
            )
            for f in filas
        ]

    def insert(self, cliente):
        cursor = self.conn.cursor()
        cursor.callproc("sp_InsertCliente", [
            cliente.codigo, cliente.tipo, cliente.razon_social,
            cliente.sector_actividad, cliente.ruc, cliente.direccion,
            cliente.telefono, cliente.sitio_web, cliente.contacto_principal,
            cliente.cargo_contacto, cliente.correo_electronico,
            cliente.telefono_directo, cliente.fecha_primera_relacion,
            cliente.origen_contacto, cliente.clasificacion_potencial
        ])
        self.conn.commit()
        cursor.close()

    def update(self, cliente):
        cursor = self.conn.cursor()
        cursor.callproc("sp_UpdateCliente", [
            cliente.codigo, cliente.tipo, cliente.razon_social,
            cliente.sector_actividad, cliente.ruc, cliente.direccion,
            cliente.telefono, cliente.sitio_web, cliente.contacto_principal,
            cliente.cargo_contacto, cliente.correo_electronico,
            cliente.telefono_directo, cliente.clasificacion_potencial
        ])
        self.conn.commit()
        cursor.close()

    def delete_cliente(self, codigo):
        cursor = self.conn.cursor()
        try:
            cursor.callproc("sp_DeleteCliente", [codigo])
            self.conn.commit()
        except Exception as e:
            # El SP lanza error si el cliente tiene proyectos o facturas asociadas
            raise Exception(str(e))
        finally:
            cursor.close()