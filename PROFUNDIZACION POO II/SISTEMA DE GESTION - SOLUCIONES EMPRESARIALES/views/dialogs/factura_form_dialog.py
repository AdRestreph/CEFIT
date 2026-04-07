from datetime import date

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout,
    QLineEdit, QComboBox, QMessageBox, QDoubleSpinBox, QTextEdit, QDateEdit
)
from PyQt6.QtCore import QDate
from ui.themes import obtener_tema, estilo_boton, estilo_input
from ui.iconos.iconos import iconos_formulario, favicon


class FormularioFactura(QDialog):
    """
    Dialogo para crear o editar una Factura.
    Delega validacion y persistencia al FacturaController.
    """

    def __init__(self, controller, factura=None):
        super().__init__()
        self.controller = controller
        self.factura    = factura
        self.editando   = factura is not None
        t = obtener_tema()

        self.setWindowTitle("Editar Factura" if self.editando else "Nueva Factura")
        self.setWindowIcon(favicon("app"))
        self.setMinimumWidth(440)
        self.setStyleSheet(f"background-color: {t['fondo_panel']}; color: {t['texto']};")

        layout = QVBoxLayout()
        self.setLayout(layout)

        form = QFormLayout()
        form.setSpacing(10)
        estilo = estilo_input(t)

        self.campo_codigo    = QLineEdit()
        self.campo_cliente   = QLineEdit()
        self.campo_proyecto  = QLineEdit()
        self.campo_emision   = QDateEdit()
        self.campo_emision.setCalendarPopup(True)
        self.campo_emision.setDate(QDate.currentDate())
        self.campo_emision.setDisplayFormat("dd/MM/yyyy")
        self.campo_vence     = QDateEdit()
        self.campo_vence.setCalendarPopup(True)
        self.campo_vence.setDate(QDate.currentDate())
        self.campo_vence.setDisplayFormat("dd/MM/yyyy")
        self.campo_monto     = QDoubleSpinBox()
        self.campo_monto.setRange(0, 999999999)
        self.campo_monto.setDecimals(2)
        self.campo_monto.setPrefix("$ ")
        self.campo_estado    = QComboBox()
        self.campo_estado.addItems(["pendiente", "pagada", "vencida", "anulada"])
        self.campo_notas     = QTextEdit()
        self.campo_notas.setFixedHeight(70)

        for w in [self.campo_codigo, self.campo_cliente, self.campo_proyecto,
                  self.campo_emision, self.campo_vence, self.campo_monto,
                  self.campo_estado, self.campo_notas]:
            w.setStyleSheet(estilo)

        form.addRow("Codigo *:",          self.campo_codigo)
        form.addRow("Cliente *:",         self.campo_cliente)
        form.addRow("Proyecto:",          self.campo_proyecto)
        form.addRow("Fecha emision:",     self.campo_emision)
        form.addRow("Fecha vencimiento:", self.campo_vence)
        form.addRow("Monto total:",       self.campo_monto)
        form.addRow("Estado:",            self.campo_estado)
        form.addRow("Notas:",             self.campo_notas)
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
            self.campo_codigo.setText(factura.codigo)
            self.campo_codigo.setEnabled(False)
            self.campo_cliente.setText(factura.codigo_cliente or "")
            self.campo_proyecto.setText(factura.codigo_proyecto or "")
            if factura.fecha_emision:
                f = factura.fecha_emision
                self.campo_emision.setDate(QDate(f.year, f.month, f.day))
            if factura.fecha_vencimiento:
                f = factura.fecha_vencimiento
                self.campo_vence.setDate(QDate(f.year, f.month, f.day))
            self.campo_monto.setValue(float(factura.monto_total or 0))
            self.campo_estado.setCurrentText(factura.estado or "pendiente")
            self.campo_notas.setPlainText(factura.notas or "")

    def _recolectar_datos(self) -> dict:
        def qdate_a_py(qd):
            return date(qd.year(), qd.month(), qd.day())
        return {
            "codigo":            self.campo_codigo.text().strip(),
            "codigo_cliente":    self.campo_cliente.text().strip(),
            "codigo_proyecto":   self.campo_proyecto.text().strip() or None,
            "fecha_emision":     qdate_a_py(self.campo_emision.date()),
            "fecha_vencimiento": qdate_a_py(self.campo_vence.date()),
            "monto_total":       self.campo_monto.value() or None,
            "estado":            self.campo_estado.currentText() or None,
            "notas":             self.campo_notas.toPlainText().strip() or None,
        }

    def _guardar(self):
        datos = self._recolectar_datos()
        valido, mensaje = self.controller.validar(datos)
        if not valido:
            QMessageBox.warning(self, "Error", mensaje)
            return
        accion = "actualizar" if self.editando else "guardar"
        respuesta = QMessageBox.question(
            self, "Confirmar", f"Deseas {accion} esta factura?",
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
