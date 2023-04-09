DDL_QUERY = '''

	-- Designamos 'Facultad' como base de datos actual, a la que se hará referencia en el resto del código
USE db_school_23000478;


-- CREACIÓN DE LAS TABLAS
	/* Borramos las tablas si existen. 
    Esto no es totalmente necesario ya que anteriormente se eliminó y creó de nuevo la base de datos. 
    Por lo tanto, las tablas también quedaron eliminadas*/
DROP TABLE IF EXISTS curso;
DROP TABLE IF EXISTS profesor;
DROP TABLE IF EXISTS tlfContactoProf;
DROP TABLE IF EXISTS asignatura;
DROP TABLE IF EXISTS alumno;
DROP TABLE IF EXISTS matricula;
DROP TABLE IF EXISTS impartir;
	-- Creación de tablas
CREATE TABLE curso(
	idCurso numeric(2),
    nombreDescriptivo text(10) not null,
    nAsignaturas numeric(3) not null,
    PRIMARY KEY(idCurso)
);

CREATE TABLE profesor(
	idProfesor char(5),
    NIF char(9) unique,
    nombre varchar(50) not null,
    apellido1 varchar(50) not null,
    apellido2 varchar(50),
    email varchar (50) unique,
    direccion varchar(100) not null,
    codigoPostal numeric(5) not null,
    municipio text(50) not null,
    provincia text(50) not null,
    categoria enum('Catedráticos de Universidad', 'Titulares Universidad', 'Catedráticos de Escuela Universitaria',
    'Titulares de Escuela Universitaria', 'Eméritos', 'Contratados Doctores', 'Contratados Doctores Interinos',
    'Asociados', 'Asociado Interino', 'Ayudantes Doctores', 'Otros Investigadores Doctores', 'PDI predoctoral'),
    PRIMARY KEY(idProfesor)
    );
    
CREATE TABLE telProf(
	idProfesor char(5) not null,
    telefono numeric(9) not null,
    FOREIGN KEY(idProfesor) REFERENCES profesor(idProfesor) 
    ON DELETE cascade -- Eliminando un profesor se eliminarán automáticamente sus teléfonos de contacto
);

CREATE TABLE asignatura(
	curso numeric(2) not null,
    idAsignatura char(5) not null,
    nombre varchar(150) unique,
    cuatrimestre enum('1', '2'),
    creditos real not null,
    caracter enum('obligatoria', 'optativa') not null,
    coordinador char(5) not null,
    PRIMARY KEY(idAsignatura),
    FOREIGN KEY(curso) REFERENCES curso(idCurso),
    FOREIGN KEY(coordinador) REFERENCES profesor(idProfesor)
    );
    
CREATE TABLE alumno(
	idAlumno char(5) not null,
    NIF char(9)unique, -- NIF es una cadena de caracteres de longitud fija de 9 y un valor único
    nombre text(50) not null,
    apellido1 text(50) not null,
    apellido2 text(50),
    email varchar(50) unique,
    direccion varchar(100) not null,
    codigoPostal numeric(5) not null,
    municipio text(50) not null,
    provincia text(50) not null,
    PRIMARY KEY(idAlumno)
    );
    
CREATE TABLE matricula(
    idAlumno char(5) not null,
    idAsignatura char(5) not null,
    nota real not null,
    FOREIGN KEY(idAlumno) REFERENCES alumno(idAlumno),
	FOREIGN KEY(idAsignatura) REFERENCES asignatura(idAsignatura),
    CHECK (nota > 0)
    );

CREATE TABLE impartir(
    idProfesor char(5) not null,
    idAsignatura char(5) not null,
    FOREIGN KEY(idProfesor) REFERENCES profesor(idProfesor),
	FOREIGN KEY(idAsignatura) REFERENCES asignatura(idAsignatura)
);

	-- Olvidé incluir el campo beca en alumno. Lo incluiremos con alter table
ALTER TABLE alumno
ADD beca char(2) not null;

 '''