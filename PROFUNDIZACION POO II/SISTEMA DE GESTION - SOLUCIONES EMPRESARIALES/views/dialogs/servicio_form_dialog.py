from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout,
    QLineEdit, QComboBox, QMessageBox, QDoubleSpinBox, QTextEdit
)
from ui.themes import obtener_tema, estilo_boton, estilo_input
from ui.iconos.iconos import iconos_formulario, favicon


class FormularioServicio(QDialog):
    """
    Dialogo para crear o editar un Servicio.
    Delega validacion y persistencia al ServicioController.
    """

    def __init__(self, controller, servicio=None):
        super().__init__()
        self.controller = controller
        self.servicio   = servicio
        self.editando   = servicio is not None
        t = obtener_tema()

        self.setWindowTitle("Editar Servicio" if self.editando else "Nuevo Servicio")
        self.setWindowIcon(favicon("app"))
        self.setMinimumWidth(440)
        self.setStyleSheet(f"background-color: {t['fondo_panel']}; color: {t['texto']};")

        layout = QVBoxLayout()
        self.setLayout(layout)

        form = QFormLayout()
        form.setSpacing(10)
        estilo = estilo_input(t)

        self.campo_codigo      = QLineEdit()
        self.campo_nombre      = QLineEdit()
        self.campo_tipo        = QComboBox()
        self.campo_tipo.addItems(["", "consultoria", "implementacion", "soporte", "capacitacion"])
        self.campo_descripcion = QTextEdit()
        self.campo_descripcion.setFixedHeight(80)
        self.campo_precio      = QDoubleSpinBox()
        self.campo_precio.setRange(0, 9999999)
        self.campo_precio.setDecimals(2)
        self.campo_precio.setPrefix("$ ")
        self.campo_unidad      = QLineEdit()
        self.campo_estado      = QComboBox()
        self.campo_estado.addItems(["activo", "inactivo"])

        for w in [self.campo_codigo, self.campo_nombre, self.campo_tipo,
                  self.campo_precio, self.campo_unidad, self.campo_estado,
                  self.campo_descripcion]:
            w.setStyleSheet(estilo)

        form.addRow("Codigo *:",     self.campo_codigo)
        form.addRow("Nombre *:",     self.campo_nombre)
        form.addRow("Tipo:",         self.campo_tipo)
        form.addRow("Descripcion:",  self.campo_descripcion)
        form.addRow("Precio base:",  self.campo_precio)
        form.addRow("Unidad cobro:", self.campo_unidad)
        form.addRow("Estado:",       self.campo_estado)
        layout.addLayout(form)

        barra = QHBoxLayout()
        self.btn_guardar  = QPushButton("  Guardar")
        self.btn_cancelar = QPushButton("  Cancelar")
        self.btn_guardar.setMinimumHeight(34)
        self.btn_cancelar.setMinimumHeight(34)
        self.btn_guardar.setStyleSheet(estilo_boton(t["btn_primario"],  t["btn_primario_txt"]))
        self.btn_cancelar.setStyleSheet(estilo_boton(t["btn_limpiar"],  t["btn_limpiar_txt"]))
        barra.addStretch()
        barra.addWidget(self.btn_guardar)
        barra.addWidget(self.btn_cancelar)
        layout.addLayout(barra)

        self.btn_guardar.clicked.connect(self._guardar)
        self.btn_cancelar.clicked.connect(self.reject)
        iconos_formulario(self.btn_guardar, self.btn_cancelar)

        if self.editando:
            self.campo_codigo.setText(servicio.codigo)
            self.campo_codigo.setEnabled(False)
            self.campo_nombre.setText(servicio.nombre or "")
            self.campo_tipo.setCurrentText(servicio.tipo or "")
            self.campo_descripcion.setPlainText(servicio.descripcion or "")
            self.campo_precio.setValue(float(servicio.precio_base or 0))
            self.campo_unidad.setText(servicio.unidad_cobro or "")
            self.campo_estado.setCurrentText(servicio.estado or "activo")

    def _recolectar_datos(self) -> dict:
        return {
            "codigo":       self.campo_codigo.text().strip(),
            "nombre":       self.campo_nombre.text().strip(),
            "tipo":         self.campo_tipo.currentText() or None,
            "descripcion":  self.campo_descripcion.toPlainText().strip() or None,
            "precio_base":  self.campo_precio.value() or None,
            "unidad_cobro": self.campo_unidad.text().strip() or None,
            "estado":       self.campo_estado.currentText() or None,
        }

    def _guardar(self):
        datos = self._recolectar_datos()
        valido, mensaje = self.controller.validar(datos)
        if not valido:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Error", mensaje)
            return
        from PyQt6.QtWidgets import QMessageBox
        accion = "actualizar" if self.editando else "guardar"
        respuesta = QMessageBox.question(
            self, "Confirmar", f"Deseas {accion} este servicio?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta != QMessageBox.StandardButton.Yes:
            return
        try:
            if self.editando:
                self.controller.actualizar(datos)
            else:
                self.controller.crear(datos)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error al guardar", str(e))
