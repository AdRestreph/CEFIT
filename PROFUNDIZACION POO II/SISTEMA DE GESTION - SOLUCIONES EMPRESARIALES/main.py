import sys
from PyQt6.QtWidgets import QApplication

from database.connection import DatabaseConnection
from repositories.cliente_repository           import ClienteRepository
from repositories.consultor_repository         import ConsultorRepository
from repositories.servicio_repository          import ServicioRepository
from repositories.proyecto_repository          import ProyectoRepository
from repositories.propuesta_repository         import PropuestaRepository
from repositories.fase_repository             import FaseRepository
from repositories.entregable_repository        import EntregableRepository
from repositories.hora_trabajada_repository    import HoraTrabajadaRepository
from repositories.factura_repository           import FacturaRepository
from repositories.conocimiento_repository      import ConocimientoRepository
from repositories.proyecto_consultor_repository import ProyectoConsultorRepository

from views.ventana_principal import VentanaPrincipal


def main():
    # 1. QApplication primero
    app = QApplication(sys.argv)

    # 2. Conexion a base de datos
    db = DatabaseConnection()
    if not db.connect():
        print("No se pudo conectar a la base de datos.")
        return

    # 3. Repositorios (solo acceso a datos, sin logica de negocio)
    repos = {
        "clientes":         ClienteRepository(db),
        "consultores":      ConsultorRepository(db),
        "servicios":        ServicioRepository(db),
        "proyectos":        ProyectoRepository(db),
        "propuestas":       PropuestaRepository(db),
        "fases":            FaseRepository(db),
        "entregables":      EntregableRepository(db),
        "horas":            HoraTrabajadaRepository(db),
        "facturas":         FacturaRepository(db),
        "conocimiento":     ConocimientoRepository(db),
        "proy_consultores": ProyectoConsultorRepository(db),
    }

    # 4. VentanaPrincipal recibe repos y ella misma crea los Controllers
    #    y se los pasa a cada View  →  main.py no sabe nada de Views ni Controllers
    ventana = VentanaPrincipal(repos)
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
