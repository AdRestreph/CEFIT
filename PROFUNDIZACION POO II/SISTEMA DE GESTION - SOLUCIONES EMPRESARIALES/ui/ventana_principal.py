from PyQt6.QtWidgets import (
    QMainWindow,   # ventana principal con soporte para barra de menú y status bar
    QWidget,       # contenedor genérico, base de todos los widgets
    QHBoxLayout,   # organiza elementos horizontalmente (sidebar | contenido)
    QVBoxLayout,   # organiza elementos verticalmente (botones apilados)
    QPushButton,   # botón clickeable
    QLabel,        # texto estático
    QStackedWidget # contenedor que muestra UN solo widget a la vez (como pestañas)
)
from PyQt6.QtCore import Qt  # contiene constantes como alineación, tamaños, etc.


class VentanaPrincipal(QMainWindow):

    def __init__(self, repos):
        super().__init__()

        # repos es un diccionario con todos los repositorios
        # lo guardamos para pasárselo a cada sección cuando la creemos
        self.repos = repos

        self.setWindowTitle("Sistema de Gestión — Soluciones Empresariales")
        self.setMinimumSize(1000, 600)

        # ── Contenedor raíz ───────────────────────────────────────
        # QMainWindow exige un widget central, todo lo demás va adentro
        raiz = QWidget()
        self.setCentralWidget(raiz)

        # Layout horizontal: sidebar a la izquierda, contenido a la derecha
        layout_raiz = QHBoxLayout()
        layout_raiz.setSpacing(0)       # sin espacio entre sidebar y contenido
        layout_raiz.setContentsMargins(0, 0, 0, 0)  # sin márgenes en los bordes
        raiz.setLayout(layout_raiz)

        # ── Sidebar ───────────────────────────────────────────────
        sidebar = QWidget()
        sidebar.setFixedWidth(200)       # ancho fijo de 200px, no se estira
        sidebar.setStyleSheet("background-color: #2c3e50;")  # color oscuro
        layout_sidebar = QVBoxLayout()
        layout_sidebar.setSpacing(4)
        layout_sidebar.setContentsMargins(8, 16, 8, 16)
        sidebar.setLayout(layout_sidebar)

        # Título del sidebar
        titulo = QLabel("📊 Gestión")
        titulo.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)  # centrar el texto
        layout_sidebar.addWidget(titulo)

        # Espaciador pequeño debajo del título
        layout_sidebar.addSpacing(12)

        # ── Área de contenido ─────────────────────────────────────
        # QStackedWidget muestra un solo "panel" a la vez
        # cuando el usuario hace clic en un botón del sidebar, cambiamos cuál panel se ve
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: #f5f6fa;")

        # ── Crear botones del sidebar y sus páginas ───────────────
        # Cada módulo tiene un botón en el sidebar y una página en el stack
        modulos = [
            ("👥  Clientes",      self._pagina_placeholder("Clientes")),
            ("🧑‍💼  Consultores",   self._pagina_placeholder("Consultores")),
            ("📋  Servicios",     self._pagina_placeholder("Servicios")),
            ("🗂️  Proyectos",     self._pagina_placeholder("Proyectos")),
            ("📝  Propuestas",    self._pagina_placeholder("Propuestas")),
            ("🔀  Fases",         self._pagina_placeholder("Fases")),
            ("📦  Entregables",   self._pagina_placeholder("Entregables")),
            ("⏱️  Horas",         self._pagina_placeholder("Horas Trabajadas")),
            ("🧾  Facturas",      self._pagina_placeholder("Facturas")),
            ("📚  Conocimiento",  self._pagina_placeholder("Conocimiento")),
        ]

        for texto, pagina in modulos:
            # Crear botón
            boton = QPushButton(texto)
            boton.setStyleSheet("""
                QPushButton {
                    color: white;
                    background-color: transparent;
                    border: none;
                    padding: 10px;
                    text-align: left;
                    font-size: 13px;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #3d5166;
                }
                QPushButton:pressed {
                    background-color: #1a252f;
                }
            """)

            # Agregar la página al stack y guardar su índice
            indice = self.stack.addWidget(pagina)

            # Conectar el botón al stack
            # lambda captura el índice actual del for para cada botón
            boton.clicked.connect(lambda checked, i=indice: self.stack.setCurrentIndex(i))

            layout_sidebar.addWidget(boton)

        # Empuja todo hacia arriba, dejando espacio vacío abajo
        layout_sidebar.addStretch()

        # ── Ensamblar sidebar + contenido ─────────────────────────
        layout_raiz.addWidget(sidebar)
        layout_raiz.addWidget(self.stack)

    def _pagina_placeholder(self, nombre):
        """
        Crea una página temporal con solo un título centrado.
        Cada módulo va a reemplazar esto con su tabla real.
        """
        pagina = QWidget()
        layout = QVBoxLayout()
        pagina.setLayout(layout)

        etiqueta = QLabel(f"Módulo: {nombre}")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta.setStyleSheet("font-size: 24px; color: #95a5a6;")

        layout.addWidget(etiqueta)
        return pagina