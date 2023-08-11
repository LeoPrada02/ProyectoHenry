# Proyecto individual Henry
## Contexto
  En este proyecto se simula un entorno laboral en el cual nuestra tarea es disponibilizar una api con funciones especificas para obtener informacion valiosa, todo esto a partir de unos archivos csv los cuales vienen sucios, asi que tendremos que limpiar estos datasets en un proceso de ETL, luego explorar las variables y las columnas en un proceso de EDA, y finalmente con la ayuda de la libreria Fastapi y render disponibilizaremos un servicio web para el consumo de la informacion extraída.

## Orden cronologico
  Primero empezamos con el ETL (Archivo del mismo nombre), en el cual hacemos los cambios pertinentes para una mejor extraccion de los datos, esto significa principalmente desanidar las columnas necesarias para poder crear columnas solicitadas por el cliente (recordar que simulamos un entorno laboral), me quedo solo con los registros que tienen status 'Released'
