from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout,
    QLineEdit, QComboBox, QLabel, QMessageBox, QSpinBox, QDoubleSpinBox
)
from ui.themes import obtener_tema, estilo_boton, estilo_input
from ui.iconos.iconos import iconos_formulario, favicon


class FormularioConsultor(QDialog):
    """
    Dialogo para crear o editar un Consultor.
    Delega validacion y persistencia al ConsultorController.
    """

    def __init__(self, controller, consultor=None):
        super().__init__()
        self.controller = controller
        self.consultor  = consultor
        self.editando   = consultor is not None
        t = obtener_tema()

        self.setWindowTitle("Editar Consultor" if self.editando else "Nuevo Consultor")
        self.setWindowIcon(favicon("consultores"))
        self.setMinimumWidth(480)
        self.setStyleSheet(f"background-color: {t['fondo_panel']}; color: {t['texto']};")

        layout = QVBoxLayout()
        self.setLayout(layout)

        form = QFormLayout()
        form.setSpacing(10)
        estilo = estilo_input(t)

        self.campo_codigo         = QLineEdit()
        self.campo_nombres        = QLineEdit()
        self.campo_apellidos      = QLineEdit()
        self.campo_documento      = QLineEdit()
        self.campo_formacion      = QLineEdit()
        self.campo_certificaciones= QLineEdit()
        self.campo_especialidades = QLineEdit()
        self.campo_experiencia    = QSpinBox()
        self.campo_experiencia.setRange(0, 60)
        self.campo_nivel          = QComboBox()
        self.campo_nivel.addItems(["", "junior", "senior", "gerente", "socio"])
        self.campo_tarifa         = QDoubleSpinBox()
        self.campo_tarifa.setRange(0, 9999999)
        self.campo_tarifa.setDecimals(2)
        self.campo_tarifa.setPrefix("$ ")
        self.campo_idiomas        = QLineEdit()
        self.campo_disponibilidad = QComboBox()
        self.campo_disponibilidad.addItems(["", "tiempo completo", "medio tiempo"])

        for w in [self.campo_codigo, self.campo_nombres, self.campo_apellidos,
                  self.campo_documento, self.campo_formacion, self.campo_certificaciones,
                  self.campo_especialidades, self.campo_experiencia,
                  self.campo_nivel, self.campo_tarifa, self.campo_idiomas,
                  self.campo_disponibilidad]:
            w.setStyleSheet(estilo)

        form.addRow("Codigo *:",          self.campo_codigo)
        form.addRow("Nombres *:",         self.campo_nombres)
        form.addRow("Apellidos *:",       self.campo_apellidos)
        form.addRow("Documento:",         self.campo_documento)
        form.addRow("Formacion:",         self.campo_formacion)
        form.addRow("Certificaciones:",   self.campo_certificaciones)
        form.addRow("Especialidades:",    self.campo_especialidades)
        form.addRow("Años experiencia:",  self.campo_experiencia)
        form.addRow("Nivel:",             self.campo_nivel)
        form.addRow("Tarifa/hora:",       self.campo_tarifa)
        form.addRow("Idiomas:",           self.campo_idiomas)
        form.addRow("Disponibilidad:",    self.campo_disponibilidad)
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
            self.campo_codigo.setText(consultor.codigo_empleado)
            self.campo_codigo.setEnabled(False)
            self.campo_nombres.setText(consultor.nombres or "")
            self.campo_apellidos.setText(consultor.apellidos or "")
            self.campo_documento.setText(consultor.documento_identidad or "")
            self.campo_formacion.setText(consultor.formacion_academica or "")
            self.campo_certificaciones.setText(consultor.certificaciones or "")
            self.campo_especialidades.setText(consultor.especialidades or "")
            self.campo_experiencia.setValue(int(consultor.anios_experiencia or 0))
            self.campo_nivel.setCurrentText(consultor.nivel or "")
            self.campo_tarifa.setValue(float(consultor.tarifa_horaria or 0))
            self.campo_idiomas.setText(consultor.idiomas or "")
            self.campo_disponibilidad.setCurrentText(consultor.disponibilidad or "")

    def _recolectar_datos(self) -> dict:
        return {
            "codigo_empleado":     self.campo_codigo.text().strip(),
            "nombres":             self.campo_nombres.text().strip(),
            "apellidos":           self.campo_apellidos.text().strip(),
            "documento_identidad": self.campo_documento.text().strip(),
            "formacion_academica": self.campo_formacion.text().strip(),
            "certificaciones":     self.campo_certificaciones.text().strip(),
            "especialidades":      self.campo_especialidades.text().strip(),
            "anios_experiencia":   self.campo_experiencia.value() or None,
            "nivel":               self.campo_nivel.currentText() or None,
            "tarifa_horaria":      self.campo_tarifa.value() or None,
            "idiomas":             self.campo_idiomas.text().strip() or None,
            "disponibilidad":      self.campo_disponibilidad.currentText() or None,
        }

    def _guardar(self):
        datos = self._recolectar_datos()
        valido, mensaje = self.controller.validar(datos)
        if not valido:
            QMessageBox.warning(self, "Error", mensaje)
            return
        accion = "actualizar" if self.editando else "guardar"
        respuesta = QMessageBox.question(
            self, "Confirmar", f"Deseas {accion} este consultor?",
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
