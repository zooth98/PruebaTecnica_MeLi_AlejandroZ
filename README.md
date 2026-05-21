DOCUMENTACIÓN PRUEBA TÉCNICA


EJERCICIOS BAJO ESTE REPOSITORIO:

1. Minesweeper Number of Neighbouring Mines (solutio)
2. REST API: Best TV Shows in Genre
3. SQL: Advertising System Failures Report

ESTRUCTURA PRINCIPAL:

├─ applicant_query.sql/
├─ requirements.txt/
├─ solution_best_in_genre.py
├─ solution_minesweeper.py
└─ README.md

DB_FILES: _Carpeta donde se almacena los comandos para la resolución del ejercicio 3_
├─ sample_data.sql/
├─ schema.sql/

*Requisitos para ejecución*
- Python 3.12.10
- Requests
- Para el ejercicio no.3 , utilizar las consultas SQL dentro del archivo db_files y luego ejecutar la consulta que está dentro del archivo applicant_query.sql
- MySQL 9.7.0

DECISIONES TÉCNICAS IMPORTANTES:
 - Para el ejercicio No.2 : Guardar las series filtradas por el genero en un nuevo arreglo para lograr organizar ascendentemente por rating y descendentemente por nombre.

INSTRUCCIONES DE USO:

Ejercicio 1:
 En la línea 49, en la variable _Board_ , anexar la matriz tablero y ejecutar.
 
Ejercicio 2: 
En la consola, luego de la pregunta "Ingresa un género: ", escribes el género de acuerdo a lo géneros existentes en la API del reto.

Ejercicio 3:
Ejecutar consultas SQL de los diferentes archivos en MySQL. El orden de ejecución debe ser:
 - schema.sql
 - sample_data.sql
 - aplicant.sql
