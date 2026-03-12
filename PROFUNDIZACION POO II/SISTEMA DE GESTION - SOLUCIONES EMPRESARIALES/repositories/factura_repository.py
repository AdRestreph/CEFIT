from models.factura import Factura

class FacturaRepository:
    def __init__(self, db_connection):
        self.conn = db_connection.get_connection()

    def select_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM facturas")
        filas = cursor.fetchall()
        cursor.close()
        return [Factura(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11],f[12]) for f in filas]

    def select_WHERE_numero_factura(self, numero_factura):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM facturas WHERE numero_factura = %s", (numero_factura,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Factura(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12])
        return None

    def select_WHERE_cliente(self, cliente_codigo):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM facturas WHERE cliente_codigo = %s", (cliente_codigo,))
        filas = cursor.fetchall()
        cursor.close()
        return [Factura(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8],f[9],f[10],f[11],f[12]) for f in filas]

    def insert(self, factura):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO facturas VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (factura.numero_factura, factura.fecha, factura.cliente_codigo,
             factura.proyecto_numero, factura.periodo_inicio, factura.periodo_fin,
             factura.servicios_prestados, factura.honorarios, factura.gastos_reembolsables,
             factura.descuentos, factura.impuestos, factura.condiciones_pago, factura.estado)
        )
        self.conn.commit()
        cursor.close()

    def update(self, factura):
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE facturas SET fecha=%s, cliente_codigo=%s, proyecto_numero=%s,
               periodo_inicio=%s, periodo_fin=%s, servicios_prestados=%s, honorarios=%s,
               gastos_reembolsables=%s, descuentos=%s, impuestos=%s,
               condiciones_pago=%s, estado=%s WHERE numero_factura=%s""",
            (factura.fecha, factura.cliente_codigo, factura.proyecto_numero,
             factura.periodo_inicio, factura.periodo_fin, factura.servicios_prestados,
             factura.honorarios, factura.gastos_reembolsables, factura.descuentos,
             factura.impuestos, factura.condiciones_pago, factura.estado,
             factura.numero_factura)
        )
        self.conn.commit()
        cursor.close()

    def delete_factura(self, numero_factura):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM facturas WHERE numero_factura = %s", (numero_factura,))
        self.conn.commit()
        cursor.close()
