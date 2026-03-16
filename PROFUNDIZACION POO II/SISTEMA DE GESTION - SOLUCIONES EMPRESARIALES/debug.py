print("1 - inicio")
import sys
print("2 - sys ok")
from PyQt6.QtWidgets import QApplication
print("3 - QApplication ok")
app = QApplication(sys.argv)
print("4 - app creada")
import mysql.connector
print("5 - mysql ok")
from database.connection import DatabaseConnection
print("6 - DatabaseConnection ok")
db = DatabaseConnection()
print("7 - db instanciada")
db.connect()
print("8 - conectado")
from ui.ventana_principal import VentanaPrincipal
print("9 - VentanaPrincipal ok")
ventana = VentanaPrincipal({})
print("10 - ventana creada")
ventana.show()
print("11 - ventana mostrada")