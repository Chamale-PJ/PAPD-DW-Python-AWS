# PAPD-DW-Python-AWS
Proyecto#2 Usando 2 instancias de RDS (MySQL-SQLServer) en Amazon y cargando la información usando pandas

VIDEO PROYECTO

https://drive.google.com/file/d/1_P8e4Mnc0nKYsQRRGIbc-gjrzfL9N5NU/view?usp=sharing

INTRODUCCION

Se realiza la creación de 2 instancias RDS en AWS, la primera instancia se crea en MySQL y la segunda en SQLServer, la estructura DDL para ambas bases de datos se enuentra en el repositorio del proyecto con los siguientes nombres (sql_queries.py y dw_23000478.py)

La información que se utiliza para el llenado de cada una de las tablas se encuentra en los archivos de texto que se adjuntan al repositorio, solo para la tabla curso se crea un arreglo de diccionarios que se suben directamente del notebook de jupyter hacia la base de datos de MySQL

Posterior al llenado de datos de las tablas, se realiza la transformacion de los datos en dataframes para poder manipular y configurar los datos de la manera en que se cargaran al DW o 2da instancia que se crea en SQLServer.
