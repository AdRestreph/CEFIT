TEMAS = {
    "charcoal": {
        "fondo":              "#1C1C1E",
        "fondo_panel":        "#2C2C2E",
        "fondo_tabla":        "#1C1C1E",
        "fondo_input":        "#3A3A3C",
        "texto":              "#F5F5F7",
        "texto_suave":        "#AEAEB2",
        "borde":              "#3A3A3C",
        "sidebar":            "#111111",
        "sidebar_hover":      "#2C2C2E",
        "sidebar_texto":      "#AEAEB2",
        "sidebar_activo":     "#2C2C2E",
        "sidebar_activo_txt": "#D4B483",
        "btn_primario":       "#D4B483",
        "btn_primario_txt":   "#1C1C1E",
        "btn_peligro":        "#3A1A1A",
        "btn_peligro_txt":    "#FF6B6B",
        "btn_editar":         "#3A3A3C",
        "btn_editar_txt":     "#D4B483",
        "btn_excel":          "#1A3A2A",
        "btn_excel_txt":      "#63C98A",
        "btn_pdf":            "#3A2A1A",
        "btn_pdf_txt":        "#D4B483",
        "btn_buscar":         "#2C2C2E",
        "btn_buscar_txt":     "#AEAEB2",
        "btn_limpiar":        "#2C2C2E",
        "btn_limpiar_txt":    "#AEAEB2",
        "encabezado":         "#2C2C2E",
        "encabezado_txt":     "#D4B483",
        "seleccion":          "#3A3A3C",
        "titulo":             "#F5F5F7",
    },
    "ivory": {
        "fondo":              "#FAFAF8",
        "fondo_panel":        "#FFFFFF",
        "fondo_tabla":        "#FFFFFF",
        "fondo_input":        "#F0EDE4",
        "texto":              "#1A1A1A",
        "texto_suave":        "#6B7280",
        "borde":              "#E5E3DC",
        "sidebar":            "#1A1A1A",
        "sidebar_hover":      "#292929",
        "sidebar_texto":      "#6B6B6B",
        "sidebar_activo":     "#292929",
        "sidebar_activo_txt": "#C9A84C",
        "btn_primario":       "#C9A84C",
        "btn_primario_txt":   "#1A1A1A",
        "btn_peligro":        "#7F1D1D",
        "btn_peligro_txt":    "#FEE2E2",
        "btn_editar":         "#292929",
        "btn_editar_txt":     "#C9A84C",
        "btn_excel":          "#14532D",
        "btn_excel_txt":      "#DCFCE7",
        "btn_pdf":            "#78350F",
        "btn_pdf_txt":        "#FEF3C7",
        "btn_buscar":         "#1A1A1A",
        "btn_buscar_txt":     "#C9A84C",
        "btn_limpiar":        "#F0EDE4",
        "btn_limpiar_txt":    "#6B7280",
        "encabezado":         "#F0EDE4",
        "encabezado_txt":     "#1A1A1A",
        "seleccion":          "#FFF9EC",
        "titulo":             "#1A1A1A",
    }
}

_tema_actual = "charcoal"


def obtener_tema():
    return TEMAS[_tema_actual]


def cambiar_tema(nombre):
    global _tema_actual
    if nombre in TEMAS:
        _tema_actual = nombre


def tema_actual():
    return _tema_actual


def estilo_boton(color_fondo, color_texto):
    return f"""
        QPushButton {{
            background-color: {color_fondo};
            color: {color_texto};
            padding: 6px 14px;
            border-radius: 5px;
            font-weight: bold;
            border: none;
            font-size: 12px;
        }}
        QPushButton:hover {{ background-color: {color_fondo}CC; }}
        QPushButton:pressed {{ background-color: {color_fondo}99; }}
    """


def estilo_input(t):
    return f"""
        QLineEdit, QComboBox, QDateEdit, QSpinBox, QDoubleSpinBox, QTextEdit {{
            background-color: {t['fondo_input']};
            color: {t['texto']};
            border: 1px solid {t['borde']};
            border-radius: 4px;
            padding: 5px 8px;
            font-size: 12px;
        }}
        QComboBox::drop-down {{ border: none; }}
        QComboBox QAbstractItemView {{
            background-color: {t['fondo_panel']};
            color: {t['texto']};
            selection-background-color: {t['seleccion']};
            border: 1px solid {t['borde']};
        }}
        QDateEdit::drop-down {{ border: none; }}
        QCalendarWidget {{
            background-color: {t['fondo_panel']};
            color: {t['texto']};
        }}
    """


def estilo_tabla(t):
    return f"""
        QTableWidget {{
            background-color: {t['fondo_tabla']};
            color: {t['texto']};
            gridline-color: {t['borde']};
            border: 1px solid {t['borde']};
            border-radius: 6px;
            font-size: 12px;
        }}
        QTableWidget::item {{ padding: 6px 8px; }}
        QTableWidget::item:selected {{
            background-color: {t['seleccion']};
            color: {t['texto']};
        }}
        QTableWidget::item:alternate {{ background-color: {t['fondo_panel']}; }}
        QHeaderView::section {{
            background-color: {t['encabezado']};
            color: {t['encabezado_txt']};
            padding: 8px;
            border: none;
            border-right: 1px solid {t['borde']};
            border-bottom: 1px solid {t['borde']};
            font-weight: bold;
            font-size: 12px;
        }}
        QScrollBar:vertical {{
            background: {t['fondo']};
            width: 8px;
            border-radius: 4px;
        }}
        QScrollBar::handle:vertical {{
            background: {t['borde']};
            border-radius: 4px;
            min-height: 20px;
        }}
    """


def estilo_sidebar(t):
    return f"""
        QWidget#sidebar {{
            background-color: {t['sidebar']};
        }}
        QPushButton#sidebar_btn {{
            background-color: transparent;
            color: {t['sidebar_texto']};
            border: none;
            padding: 10px 14px;
            text-align: left;
            font-size: 13px;
            border-radius: 6px;
        }}
        QPushButton#sidebar_btn:hover {{
            background-color: {t['sidebar_hover']};
            color: {t['sidebar_activo_txt']};
        }}
        QPushButton#sidebar_btn:checked {{
            background-color: {t['sidebar_activo']};
            color: {t['sidebar_activo_txt']};
            font-weight: bold;
        }}
    """


def estilo_ventana(t):
    return f"""
        QMainWindow, QWidget {{
            background-color: {t['fondo']};
            color: {t['texto']};
            font-family: 'Segoe UI', Arial, sans-serif;
        }}
        QLabel {{ color: {t['texto']}; }}
        QDialog {{ background-color: {t['fondo_panel']}; color: {t['texto']}; }}
        QMessageBox {{ background-color: {t['fondo_panel']}; color: {t['texto']}; }}
        QScrollArea {{ border: none; background-color: transparent; }}
    """