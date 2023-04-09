DW_DDL_QUERY = """
USE [dw-23000478];

CREATE TABLE [dw-23000478].[dbo].[dim_profesor] (
    id INT PRIMARY KEY IDENTITY (1, 1),
    idProfesor CHAR (5) NOT NULL,
    NIF CHAR (9) NOT NULL,
    email VARCHAR(50),
    direccion varchar(100),
	codigoPostal numeric(5,0),
	municipio text,
	provincia text,
	categoria varchar(150),
	telefono numeric(9,0),
	nombre_profesor VARCHAR(150)
);

CREATE TABLE [dw-23000478].[dbo].[dim_alumno] (
    id INT PRIMARY KEY IDENTITY (1, 1),
    idAlumno CHAR (5) NOT NULL,
    NIF CHAR (9) NOT NULL,
    email VARCHAR(50),
    direccion varchar(100),
	codigoPostal numeric(5,0),
	municipio text,
	provincia text,
	beca char(2),
	nota real,
	nombre_alumno VARCHAR(150),
	nombre_curso varchar(500)
);

CREATE TABLE [dw-23000478].[dbo].[dim_curso] (
    id INT PRIMARY KEY IDENTITY (1, 1),
    idAsignatura CHAR (5) NOT NULL,
    nombre VARCHAR (300) NOT NULL,
    cuatrimestre char(1),
	creditos real,
	caracter varchar(300),
	nombre_profesor VARCHAR(150),
	nombreDescriptivo varchar(150)
);

CREATE TABLE [dw-23000478].[dbo].[fact_table] (
    id INT PRIMARY KEY IDENTITY (1, 1),
	idAlumno CHAR (5) NOT NULL,	
    idAsignatura CHAR (5) NOT NULL,
	idProfesor CHAR (5) NOT NULL,
    nota real,
    idCurso numeric(1,0)
);

"""