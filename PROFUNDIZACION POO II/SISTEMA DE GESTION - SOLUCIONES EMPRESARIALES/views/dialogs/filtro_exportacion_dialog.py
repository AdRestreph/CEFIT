from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox
)
from ui.themes import obtener_tema, estilo_boton, estilo_input
from ui.iconos.iconos import favicon


class DialogoFiltroExportacion(QDialog):
    """
    Dialogo generico para elegir filtros antes de exportar.
    Reutilizable por cualquier modulo que tenga filtros de tipo y clasificacion.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Filtros de exportacion")
        self.setWindowIcon(favicon("clientes"))
        self.setMinimumWidth(320)
        t = obtener_tema()
        self.setStyleSheet(f"background-color: {t['fondo_panel']}; color: {t['texto']};")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Filtrar por tipo:"))
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Todos", "PYME", "corporativo", "gobierno"])
        self.combo_tipo.setStyleSheet(estilo_input(t))
        layout.addWidget(self.combo_tipo)

        layout.addWidget(QLabel("Filtrar por clasificacion:"))
        self.combo_clasif = QComboBox()
        self.combo_clasif.addItems(["Todos", "alto", "medio", "bajo"])
        self.combo_clasif.setStyleSheet(estilo_input(t))
        layout.addWidget(self.combo_clasif)

        barra      = QHBoxLayout()
        btn_ok     = QPushButton("  Exportar")
        btn_cancel = QPushButton("  Cancelar")
        btn_ok.setStyleSheet(estilo_boton(t["btn_primario"], t["btn_primario_txt"]))
        btn_cancel.setStyleSheet(estilo_boton(t["btn_limpiar"], t["btn_limpiar_txt"]))
        barra.addStretch()
        barra.addWidget(btn_ok)
        barra.addWidget(btn_cancel)
        layout.addLayout(barra)

        btn_ok.clicked.connect(self.accept)
        btn_cancel.clicked.connect(self.reject)

    def obtener_filtros(self):
        tipo   = self.combo_tipo.currentText()
        clasif = self.combo_clasif.currentText()
        return {
            "tipo":          None if tipo   == "Todos" else tipo,
            "clasificacion": None if clasif == "Todos" else clasif,
        }
