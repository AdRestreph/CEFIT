from Database.connection import DatabaseConnection
from repositories.cliente_repository import ClienteRepository
from repositories.consultor_repository import ConsultorRepository
from repositories.servicio_repository import ServicioRepository
from repositories.proyecto_repository import ProyectoRepository
from repositories.propuesta_repository import PropuestaRepository
from repositories.fase_repository import FaseRepository
from repositories.entregable_repository import EntregableRepository
from repositories.hora_trabajada_repository import HoraTrabajadaRepository
from repositories.factura_repository import FacturaRepository
from repositories.conocimiento_repository import ConocimientoRepository
from repositories.proyecto_consultor_repository import ProyectoConsultorRepository


def main():
    db = DatabaseConnection()
    if not db.connect():
        return

    clientes   = ClienteRepository(db)
    consultores = ConsultorRepository(db)
    servicios  = ServicioRepository(db)
    proyectos  = ProyectoRepository(db)
    propuestas = PropuestaRepository(db)
    fases      = FaseRepository(db)
    entregables = EntregableRepository(db)
    horas      = HoraTrabajadaRepository(db)
    facturas   = FacturaRepository(db)
    conocimiento = ConocimientoRepository(db)
    proy_consultores = ProyectoConsultorRepository(db)

    print("\n── CLIENTES ──────────────────────────")
    for c in clientes.select_all():
        print(c)

    print("\n── CONSULTORES ───────────────────────")
    for c in consultores.select_all():
        print(c)

    print("\n── SERVICIOS ─────────────────────────")
    for s in servicios.select_all():
        print(s)

    print("\n── PROYECTOS ─────────────────────────")
    for p in proyectos.select_all():
        print(p)

    print("\n── PROPUESTAS ────────────────────────")
    for p in propuestas.select_all():
        print(p)

    print("\n── FASES ─────────────────────────────")
    for f in fases.select_all():
        print(f)

    print("\n── ENTREGABLES ───────────────────────")
    for e in entregables.select_all():
        print(e)

    print("\n── HORAS TRABAJADAS ──────────────────")
    for h in horas.select_all():
        print(h)

    print("\n── FACTURAS ──────────────────────────")
    for f in facturas.select_all():
        print(f)

    print("\n── CONOCIMIENTO ──────────────────────")
    for c in conocimiento.select_all():
        print(c)

    print("\n── CONSULTORES POR PROYECTO ──────────")
    for pc in proy_consultores.select_WHERE_proyecto("PRY-2024-001"):
        print(pc)

    db.disconnect()


if __name__ == "__main__":
    main()