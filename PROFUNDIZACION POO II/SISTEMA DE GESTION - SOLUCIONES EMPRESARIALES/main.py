import sys
from PyQt6.QtWidgets import QApplication

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
from ui.ventana_principal import VentanaPrincipal


def main():
    db = DatabaseConnection()
    if not db.connect():
        print("No se pudo conectar a la base de datos.")
        return

    # Empaquetamos todos los repositorios en un diccionario
    # así los pasamos todos juntos a la ventana con una sola variable
    repos = {
        "clientes":           ClienteRepository(db),
        "consultores":        ConsultorRepository(db),
        "servicios":          ServicioRepository(db),
        "proyectos":          ProyectoRepository(db),
        "propuestas":         PropuestaRepository(db),
        "fases":              FaseRepository(db),
        "entregables":        EntregableRepository(db),
        "horas":              HoraTrabajadaRepository(db),
        "facturas":           FacturaRepository(db),
        "conocimiento":       ConocimientoRepository(db),
        "proy_consultores":   ProyectoConsultorRepository(db),
    }

    app = QApplication(sys.argv)
    ventana = VentanaPrincipal(repos)
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()