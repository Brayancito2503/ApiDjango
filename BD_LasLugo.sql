CREATE TABLE Rol (
	IdRol SERIAL PRIMARY KEY,
	nombreRol VARCHAR(25),
	esActivo BOOLEAN DEFAULT True,
	fechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Menu (
	IdMenu SERIAL PRIMARY KEY,
	nombreMenu VARCHAR(30),
	icono TEXT,
	url TEXT
);

CREATE TABLE MenuRol(
	IdMenuRol SERIAL PRIMARY KEY,
	IdMenu INT REFERENCES Menu(IdMenu),
	IdRol INT REFERENCES Rol(IdRol)
);

CREATE TABLE Personal(
	IdPersonal SERIAL PRIMARY KEY,
	IdRol INT REFERENCES Rol(IdRol),
	nombre VARCHAR(30),
	apellido VARCHAR(30),
	telefono VARCHAR(15),
	correo TEXT,
	clave TEXT,
	esActivo BOOLEAN DEFAULT True,
	fechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-------------------------------------

CREATE TABLE CategoriaCompra(
	IdCatCompra SERIAL PRIMARY KEY,
	nombreCategoria VARCHAR(20),
	fechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	esActivo BOOLEAN DEFAULT True
);

CREATE TABLE Proveedor(
	IdProveedor SERIAL PRIMARY KEY,
	RUC TEXT,
	telefono VARCHAR(15),
	nombreProveedor VARCHAR(20),
	fechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	empresa VARCHAR(50)
);

CREATE TABLE Compras(
	IdCompra SERIAL PRIMARY KEY,
	IdProveedor INT REFERENCES Proveedor(IdProveedor),
	IdCatCompra INT REFERENCES CategoriaCompra(IdCatCompra),
	nombreCompra TEXT,
	total DECIMAL(8, 2),
	tipoPago BOOLEAN,
	fechaCompra TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE CategoriaProducto(
	IdCatProducto SERIAL PRIMARY KEY,
	nombreCatproducto VARCHAR(30),
	fechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Productos (
	IdProducto SERIAL PRIMARY KEY,
	IdCatProducto INT REFERENCES CategoriaProducto(IdCatProducto),
	nombreProducto TEXT,
	precioCompra DECIMAL(3,2),
	precioVenta DECIMAL(3,2),
	fechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE DetalleCompra(
	IdDetCompra SERIAl PRIMARY KEY,
	IdCompra INT REFERENCES Compras(IdCompra),
	IdProducto INT REFERENCES Productos (IdProducto),
	Cantidad DECIMAL (5,2),
	precio DECIMAL (3,2),
	fechaDetCompra TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---------------------------------------

CREATE TABLE Clientes (
	IdCliente SERIAL PRIMARY KEY,
	IdPersonal INT REFERENCES Personal(IdPersonal),
	nombreCompleto VARCHAR(50)
);

CREATE TABLE VENTA (
	IdVenta SERIAL PRIMARY KEY,
	IdCliente INT REFERENCES Clientes(IdCliente),
	cantidad DECIMAL(2,2),
	PrecioVenta DECIMAL(3,2),
	esActivo BOOLEAN DEFAULT True,
	fechaVenta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE DetalleVenta (
	IdDetVenta SERIAL PRIMARY KEY,
	IdProducto INT REFERENCES Productos(IdProducto),
	IdVenta INT REFERENCES Venta(IdVenta),
	cantidad DECIMAL (3,2),
	precio DECIMAL(3,2),
	fechaVenta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	esActivo BOOLEAN DEFAULT True
);

CREATE TABLE Mesas(
	IdMesa SERIAL PRIMARY KEY,
	IdCliente INT REFERENCES Clientes(IdCliente),
	IdPersonal INT REFERENCES Personal(IdPersonal),
	numeroMesa INT,
	esActivo BOOLEAN DEFAULT True
);

-----------------------------

-----------------------------




-- Iniciar una transacción en PostgreSQL
BEGIN;

-- Iniciar un bloque de manejo de errores
BEGIN
    -- Realizar las actualizaciones
    UPDATE "MisCuentas" SET "Monto" = "Monto" + 990
    WHERE "NumCuenta" = 12345;

    UPDATE "MisAhorros" SET "Monto" = "Monto" - 990
    WHERE "NumCuenta" = 12345;

    -- Confirmar la transacción
    COMMIT;
EXCEPTION
    -- Capturar errores y hacer el rollback en caso de error
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Transaction Aborted';
        ROLLBACK;
END;
