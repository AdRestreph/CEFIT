from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QStackedWidget, QComboBox
)
from PyQt6.QtCore import Qt

from ui.themes import obtener_tema, cambiar_tema, estilo_ventana
from ui.iconos.iconos import favicon
from ui.modulos.clientes_widget     import ClientesWidget
from ui.modulos.consultores_widget  import ConsultoresWidget
from ui.modulos.servicios_widget    import ServiciosWidget
from ui.modulos.facturas_widget     import FacturasWidget


class VentanaPrincipal(QMainWindow):

    def __init__(self, repos):
        super().__init__()
        self.repos           = repos
        self.botones_sidebar = []
        self.setWindowTitle("Sistema de Gestion — Soluciones Empresariales")
        self.setWindowIcon(favicon("app"))
        self.setMinimumSize(1100, 650)
        self._construir_ui()
        self._aplicar_tema()

    def _construir_ui(self):
        raiz = QWidget()
        self.setCentralWidget(raiz)
        layout_raiz = QHBoxLayout()
        layout_raiz.setSpacing(0)
        layout_raiz.setContentsMargins(0, 0, 0, 0)
        raiz.setLayout(layout_raiz)

        self.sidebar = QWidget()
        self.sidebar.setFixedWidth(210)
        layout_sidebar = QVBoxLayout()
        layout_sidebar.setSpacing(2)
        layout_sidebar.setContentsMargins(10, 16, 10, 16)
        self.sidebar.setLayout(layout_sidebar)

        self.lbl_titulo = QLabel("Soluciones\nEmpresariales")
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_sidebar.addWidget(self.lbl_titulo)

        self.stack = QStackedWidget()

        modulos = [
            ("Clientes",         ClientesWidget(self.repos["clientes"])),
            ("Consultores",      ConsultoresWidget(self.repos["consultores"])),
            ("Servicios",        ServiciosWidget(self.repos["servicios"])),
            ("Proyectos",        self._placeholder("Proyectos")),
            ("Propuestas",       self._placeholder("Propuestas")),
            ("Fases",            self._placeholder("Fases")),
            ("Entregables",      self._placeholder("Entregables")),
            ("Horas Trabajadas", self._placeholder("Horas Trabajadas")),
            ("Facturas",         FacturasWidget(self.repos["facturas"])),
            ("Conocimiento",     self._placeholder("Conocimiento")),
        ]

        for texto, pagina in modulos:
            boton = QPushButton(texto)
            boton.setCheckable(True)
            indice = self.stack.addWidget(pagina)
            boton.clicked.connect(lambda checked, i=indice: self._cambiar_modulo(i))
            layout_sidebar.addWidget(boton)
            self.botones_sidebar.append(boton)

        self.botones_sidebar[0].setChecked(True)
        layout_sidebar.addStretch()

        self.lbl_tema = QLabel("Tema:")
        layout_sidebar.addWidget(self.lbl_tema)
        self.combo_tema = QComboBox()
        self.combo_tema.addItems(["Charcoal Pro", "Ivory Gold"])
        self.combo_tema.setCurrentText("Charcoal Pro")
        self.combo_tema.currentTextChanged.connect(self._on_cambiar_tema)
        layout_sidebar.addWidget(self.combo_tema)

        layout_raiz.addWidget(self.sidebar)
        layout_raiz.addWidget(self.stack)

    def _cambiar_modulo(self, indice):
        self.stack.setCurrentIndex(indice)
        for i, btn in enumerate(self.botones_sidebar):
            btn.setChecked(i == indice)

    def _on_cambiar_tema(self, nombre):
        mapa = {"Charcoal Pro": "charcoal", "Ivory Gold": "ivory"}
        cambiar_tema(mapa[nombre])
        self._aplicar_tema()
        widget_actual = self.stack.currentWidget()
        if hasattr(widget_actual, "_aplicar_tema"):
            widget_actual._aplicar_tema()

    def _aplicar_tema(self):
        t = obtener_tema()
        self.setStyleSheet(estilo_ventana(t))
        self.sidebar.setStyleSheet(f"""
            QWidget {{ background-color: {t['sidebar']}; }}
            QPushButton {{
                background-color: transparent;
                color: {t['sidebar_texto']};
                border: none;
                padding: 10px 14px;
                text-align: left;
                font-size: 13px;
                border-radius: 6px;
            }}
            QPushButton:hover {{
                background-color: {t['sidebar_hover']};
                color: {t['sidebar_activo_txt']};
            }}
            QPushButton:checked {{
                background-color: {t['sidebar_activo']};
                color: {t['sidebar_activo_txt']};
                font-weight: bold;
            }}
        """)
        self.lbl_titulo.setStyleSheet(
            f"font-size: 13px; font-weight: bold; color: {t['sidebar_activo_txt']}; padding: 8px 4px 16px 4px;"
        )
        self.lbl_tema.setStyleSheet(f"font-size: 11px; padding: 0 4px; color: {t['sidebar_texto']};")
        self.combo_tema.setStyleSheet(f"""
            QComboBox {{
                background-color: {t['sidebar_hover']};
                color: {t['sidebar_texto']};
                border: 1px solid {t['borde']};
                border-radius: 4px;
                padding: 4px 8px;
                font-size: 11px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {t['sidebar']};
                color: {t['sidebar_texto']};
                selection-background-color: {t['sidebar_activo']};
            }}
        """)

    def _placeholder(self, nombre):
        t = obtener_tema()
        pagina = QWidget()
        layout = QVBoxLayout()
        pagina.setLayout(layout)
        etiqueta = QLabel(nombre)
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta.setStyleSheet(f"font-size: 26px; color: {t['texto_suave']};")
        layout.addWidget(etiqueta)
        sub = QLabel("Modulo en construccion")
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub.setStyleSheet(f"font-size: 13px; color: {t['texto_suave']};")
        layout.addWidget(sub)
        return pagina
