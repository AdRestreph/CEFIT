<h1 align="center"><b>Restaurante Gourmet - Sabor exquisito </b></h1>

Este repositorio tiene adjunto tambien el **archivo de Excel(xlsx)** con sus respectivas divisiones para su calificacion, o contiene un markdown que facilita la visualizacion de todo el contenido

## Enunciado

11: Restaurante Gourmet

"El restaurante 'Sabor Exquisito' gestiona reservas y pedidos. Cada mesa tiene un número único, capacidad y ubicación (interior, terraza). Los clientes se registran con su DNI, nombre completo, teléfono y correo electrónico. Las reservas incluyen la fecha, hora, número de personas y mesa asignada. Los pedidos se registran con un número único, fecha, hora, platos solicitados (cada uno con su código, nombre y precio), bebidas y el total a pagar. Además, el restaurante lleva un inventario de ingredientes, registrando el nombre, cantidad disponible y proveedor."

## DER (Diagrama Entidad Relacion)
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Der.png)

## Diccionario de datos

### Tabla cliente
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Tabla_cliente.png)

### Tabla mesa
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Tabla_mesa.png)

### Tabla reserva
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Reserva.png)

### Tabla pedido
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Pedido.png)

### Tabla detalle pedido
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Detalle_pedido.png)

### Tabla plato
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Plato.png)

### Tabla bebida
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Bebida.png)

### Tabla ingrediente inventario
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Ingrediente_inventario.png)

### Tabla proveedor
![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Proveedor.png)

## Normalizacion

![alt text](/Fundamentos%20y%20Herramientas%20en%20Bases%20de%20datos%20I%20PM/Taller%20de%20Identificación%20de%20Tipos%20de%20Datos%20en%20SQL/Imagenes/Normalizacion.png)

## Script

Hay un script adjunto en el SQL con el nombre de la base de datos el cual se puede ejecutar con 


CREATE DATABASE IF NOT EXISTS sabor_exquisito;

USE sabor_exquisito;

CREATE TABLE CLIENTE (
    ID_cliente INT(10) NOT NULL AUTO_INCREMENT,
    Numero_identificacion VARCHAR(20) NOT NULL UNIQUE,
    Tipo_documento VARCHAR(10) NOT NULL,
    Nombre_completo VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) NOT NULL UNIQUE,
    Telefono VARCHAR(20) NOT NULL,
    PRIMARY KEY (ID_cliente)
);

CREATE TABLE MESA (
    ID_mesa INT(10) NOT NULL AUTO_INCREMENT,
    Capacidad INT(3) NOT NULL,
    Ubicacion VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID_mesa)
);

CREATE TABLE RESERVA (
    ID_reserva INT(10) NOT NULL AUTO_INCREMENT,
    ID_cliente INT(10) NOT NULL,
    ID_mesa INT(10) NOT NULL,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Numero_personas INT(3) NOT NULL,
    PRIMARY KEY (ID_reserva),
    FOREIGN KEY (ID_cliente) REFERENCES CLIENTE(ID_cliente),
    FOREIGN KEY (ID_mesa) REFERENCES MESA(ID_mesa)
);

CREATE TABLE PEDIDO (
    ID_pedido INT(10) NOT NULL AUTO_INCREMENT,
    ID_reserva INT(10) NOT NULL,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Total_pagar DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (ID_pedido),
    FOREIGN KEY (ID_reserva) REFERENCES RESERVA(ID_reserva)
);

CREATE TABLE PLATO (
    ID_plato INT(10) NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Precio DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (ID_plato)
);

CREATE TABLE BEBIDA (
    ID_bebida INT(10) NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Precio DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (ID_bebida)
);

CREATE TABLE PROVEEDOR (
    ID_proveedor INT(10) NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Contacto VARCHAR(50) NOT NULL,
    Direccion VARCHAR(150) NOT NULL,
    PRIMARY KEY (ID_proveedor)
);

CREATE TABLE INGREDIENTE_INVENTARIO (
    ID_ingrediente INT(10) NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL,
    Cantidad INT(5) NOT NULL DEFAULT 0,
    ID_proveedor INT(10) NOT NULL,
    PRIMARY KEY (ID_ingrediente),
    FOREIGN KEY (ID_proveedor) REFERENCES PROVEEDOR(ID_proveedor)
);

CREATE TABLE DETALLE_PEDIDO (
    ID_detalle INT(10) NOT NULL AUTO_INCREMENT,
    ID_pedido INT(10) NOT NULL,
    ID_plato INT(10) NULL,
    ID_bebida INT(10) NULL,
    Cantidad INT(3) NOT NULL DEFAULT 1,
    PRIMARY KEY (ID_detalle),
    FOREIGN KEY (ID_pedido) REFERENCES PEDIDO(ID_pedido),
    FOREIGN KEY (ID_plato) REFERENCES PLATO(ID_plato),
    FOREIGN KEY (ID_bebida) REFERENCES BEBIDA(ID_bebida)
);