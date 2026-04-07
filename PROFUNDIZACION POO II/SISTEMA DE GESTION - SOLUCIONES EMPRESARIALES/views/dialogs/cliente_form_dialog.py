import os
from datetime import date

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout,
    QLineEdit, QComboBox, QLabel, QMessageBox, QDateEdit,
    QFileDialog, QScrollArea, QWidget, QFrame
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QPixmap

from ui.themes import obtener_tema, estilo_boton, estilo_input
from ui.iconos.iconos import iconos_formulario, favicon


class FormularioCliente(QDialog):
    """
    Dialogo para crear o editar un Cliente.
    Delega validacion y persistencia al ClienteController.
    """

    def __init__(self, controller, cliente=None):
        super().__init__()
        self.controller  = controller
        self.cliente     = cliente
        self.editando    = cliente is not None
        self.ruta_imagen = None
        t = obtener_tema()

        self.setWindowTitle("Editar Cliente" if self.editando else "Nuevo Cliente")
        self.setWindowIcon(favicon("clientes"))
        self.setMinimumWidth(560)
        self.setStyleSheet(f"background-color: {t['fondo_panel']}; color: {t['texto']};")

        layout_principal = QHBoxLayout()
        self.setLayout(layout_principal)

        # -------- Panel formulario (scroll)
        scroll     = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        contenedor = QWidget()
        scroll.setWidget(contenedor)
        form_layout = QVBoxLayout()
        contenedor.setLayout(form_layout)

        form = QFormLayout()
        form.setSpacing(10)
        estilo = estilo_input(t)

        self.campo_codigo    = QLineEdit()
        self.campo_tipo      = QComboBox()
        self.campo_tipo.addItems(["PYME", "corporativo", "gobierno"])
        self.campo_razon     = QLineEdit()
        self.campo_sector    = QLineEdit()
        self.campo_ruc       = QLineEdit()
        self.campo_direccion = QLineEdit()
        self.campo_telefono  = QLineEdit()
        self.campo_sitio_web = QLineEdit()
        self.campo_contacto  = QLineEdit()
        self.campo_cargo     = QLineEdit()
        self.campo_correo    = QLineEdit()
        self.campo_tel_dir   = QLineEdit()
        self.campo_fecha     = QDateEdit()
        self.campo_fecha.setCalendarPopup(True)
        self.campo_fecha.setDate(QDate.currentDate())
        self.campo_fecha.setDisplayFormat("dd/MM/yyyy")
        self.campo_origen    = QLineEdit()
        self.campo_clasif    = QComboBox()
        self.campo_clasif.addItems(["", "alto", "medio", "bajo"])

        for w in [self.campo_codigo, self.campo_razon, self.campo_sector,
                  self.campo_ruc, self.campo_direccion, self.campo_telefono,
                  self.campo_sitio_web, self.campo_contacto, self.campo_cargo,
                  self.campo_correo, self.campo_tel_dir, self.campo_origen,
                  self.campo_tipo, self.campo_clasif, self.campo_fecha]:
            w.setStyleSheet(estilo)

        form.addRow("Codigo *:",           self.campo_codigo)
        form.addRow("Tipo *:",             self.campo_tipo)
        form.addRow("Razon Social *:",     self.campo_razon)
        form.addRow("Sector:",             self.campo_sector)
        form.addRow("RUC:",                self.campo_ruc)
        form.addRow("Direccion:",          self.campo_direccion)
        form.addRow("Telefono:",           self.campo_telefono)
        form.addRow("Sitio Web:",          self.campo_sitio_web)
        form.addRow("Contacto:",           self.campo_contacto)
        form.addRow("Cargo:",              self.campo_cargo)
        form.addRow("Correo:",             self.campo_correo)
        form.addRow("Tel. Directo:",       self.campo_tel_dir)
        form.addRow("Fecha 1ra Relacion:", self.campo_fecha)
        form.addRow("Origen:",             self.campo_origen)
        form.addRow("Clasificacion:",      self.campo_clasif)
        form_layout.addLayout(form)

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
        form_layout.addLayout(barra)

        self.btn_guardar.clicked.connect(self._guardar)
        self.btn_cancelar.clicked.connect(self.reject)
        layout_principal.addWidget(scroll, 2)

        # -------- Panel imagen
        panel_imagen = QFrame()
        panel_imagen.setFixedWidth(180)
        panel_imagen.setStyleSheet(
            f"background-color: {t['fondo_input']}; "
            f"border-radius: 8px; border: 1px solid {t['borde']};"
        )
        img_layout = QVBoxLayout()
        img_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        panel_imagen.setLayout(img_layout)

        lbl_img_titulo = QLabel("Imagen del Cliente")
        lbl_img_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_img_titulo.setStyleSheet(
            f"color: {t['texto_suave']}; font-size: 11px; font-weight: bold; border: none;"
        )
        img_layout.addWidget(lbl_img_titulo)

        self.lbl_imagen = QLabel()
        self.lbl_imagen.setFixedSize(150, 150)
        self.lbl_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_imagen.setStyleSheet(
            f"border: 2px dashed {t['borde']}; border-radius: 6px; color: {t['texto_suave']};"
        )
        self.lbl_imagen.setText("Sin imagen")
        img_layout.addWidget(self.lbl_imagen)

        self.btn_cargar       = QPushButton("  Cargar imagen")
        self.btn_eliminar_img = QPushButton("  Quitar imagen")
        self.btn_cargar.setStyleSheet(estilo_boton(t["btn_buscar"],  t["btn_buscar_txt"]))
        self.btn_eliminar_img.setStyleSheet(estilo_boton(t["btn_peligro"], t["btn_peligro_txt"]))
        img_layout.addWidget(self.btn_cargar)
        img_layout.addWidget(self.btn_eliminar_img)

        lbl_formatos = QLabel("JPG, PNG, GIF\nMax: 5MB")
        lbl_formatos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_formatos.setStyleSheet(f"color: {t['texto_suave']}; font-size: 10px; border: none;")
        img_layout.addWidget(lbl_formatos)
        img_layout.addStretch()

        self.btn_cargar.clicked.connect(self._cargar_imagen)
        self.btn_eliminar_img.clicked.connect(self._quitar_imagen)
        layout_principal.addWidget(panel_imagen, 1)

        iconos_formulario(self.btn_guardar, self.btn_cancelar, self.btn_cargar)

        # -------- Prellenar si es edicion
        if self.editando:
            self.campo_codigo.setText(cliente.codigo)
            self.campo_codigo.setEnabled(False)
            self.campo_tipo.setCurrentText(cliente.tipo or "")
            self.campo_razon.setText(cliente.razon_social or "")
            self.campo_sector.setText(cliente.sector_actividad or "")
            self.campo_ruc.setText(cliente.ruc or "")
            self.campo_direccion.setText(cliente.direccion or "")
            self.campo_telefono.setText(cliente.telefono or "")
            self.campo_sitio_web.setText(cliente.sitio_web or "")
            self.campo_contacto.setText(cliente.contacto_principal or "")
            self.campo_cargo.setText(cliente.cargo_contacto or "")
            self.campo_correo.setText(cliente.correo_electronico or "")
            self.campo_tel_dir.setText(cliente.telefono_directo or "")
            if cliente.fecha_primera_relacion:
                f = cliente.fecha_primera_relacion
                self.campo_fecha.setDate(QDate(f.year, f.month, f.day))
            self.campo_origen.setText(cliente.origen_contacto or "")
            self.campo_clasif.setCurrentText(cliente.clasificacion_potencial or "")
            ruta_img = self.controller.ruta_imagen(cliente.codigo)
            if ruta_img:
                self.ruta_imagen = ruta_img
                self._mostrar_imagen(ruta_img)

    # -------------------------------------------------------- Imagen helpers

    def _cargar_imagen(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar imagen", "",
            "Imagenes (*.jpg *.jpeg *.png *.gif)"
        )
        if not ruta:
            return
        if os.path.getsize(ruta) > 5 * 1024 * 1024:
            QMessageBox.warning(self, "Error", "La imagen supera el tamaño maximo de 5MB.")
            return
        try:
            from PIL import Image
            img = Image.open(ruta)
            if img.format not in ["JPEG", "PNG", "GIF"]:
                QMessageBox.warning(self, "Error", "Formato no soportado. Usa JPG, PNG o GIF.")
                return
        except Exception:
            QMessageBox.warning(self, "Error", "No se pudo leer la imagen.")
            return
        self.ruta_imagen = ruta
        self._mostrar_imagen(ruta)

    def _mostrar_imagen(self, ruta):
        pixmap = QPixmap(ruta).scaled(
            150, 150,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.lbl_imagen.setPixmap(pixmap)
        self.lbl_imagen.setText("")

    def _quitar_imagen(self):
        self.ruta_imagen = None
        self.lbl_imagen.setPixmap(QPixmap())
        self.lbl_imagen.setText("Sin imagen")

    # ------------------------------------------------------------ Guardar

    def _recolectar_datos(self) -> dict:
        fecha_q  = self.campo_fecha.date()
        fecha_py = date(fecha_q.year(), fecha_q.month(), fecha_q.day())
        return {
            "codigo":                   self.campo_codigo.text().strip(),
            "tipo":                     self.campo_tipo.currentText(),
            "razon_social":             self.campo_razon.text().strip(),
            "sector_actividad":         self.campo_sector.text().strip(),
            "ruc":                      self.campo_ruc.text().strip(),
            "direccion":                self.campo_direccion.text().strip(),
            "telefono":                 self.campo_telefono.text().strip(),
            "sitio_web":                self.campo_sitio_web.text().strip(),
            "contacto_principal":       self.campo_contacto.text().strip(),
            "cargo_contacto":           self.campo_cargo.text().strip(),
            "correo_electronico":       self.campo_correo.text().strip(),
            "telefono_directo":         self.campo_tel_dir.text().strip(),
            "fecha_primera_relacion":   fecha_py,
            "origen_contacto":          self.campo_origen.text().strip(),
            "clasificacion_potencial":  self.campo_clasif.currentText(),
        }

    def _guardar(self):
        datos = self._recolectar_datos()

        # Validacion via controller
        valido, mensaje = self.controller.validar(datos)
        if not valido:
            QMessageBox.warning(self, "Error", mensaje)
            return

        accion = "actualizar" if self.editando else "guardar"
        respuesta = QMessageBox.question(
            self, "Confirmar",
            f"Deseas {accion} este cliente?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta != QMessageBox.StandardButton.Yes:
            return

        try:
            if self.editando:
                self.controller.actualizar(datos, self.ruta_imagen)
            else:
                self.controller.crear(datos, self.ruta_imagen)
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error al guardar", str(e))
