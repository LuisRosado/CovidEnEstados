# CovidEnEstados
Programa que consulta casos de covad en los estados de la república mexicana (No esta actualizada es de una database vieja)


Este código es una aplicación de consulta de casos confirmados de COVID-19 en diferentes estados de México. A continuación, te explico cómo funciona:

La función NorOeste, NorEste, Occidente, Oriente, CentroNorte, CentroSur, SurOeste, y SurEste son funciones que muestran las opciones para seleccionar un estado de una región específica (por ejemplo, Noroeste, NorEste, etc.), y luego muestran la cantidad de casos confirmados en ese estado utilizando los datos almacenados en el diccionario pais.

La función Menu muestra las opciones de las regiones de la República y solicita al usuario que elija una opción. Luego, llama a la función correspondiente de acuerdo con la opción seleccionada.

La variable pais es un diccionario que contiene la información de casos confirmados de COVID-19 en diferentes estados de México. Cada clave del diccionario es el nombre del estado y su valor es el número de casos confirmados.

Después de definir todas las funciones y el diccionario, se llama a la función Menu(pais), lo que inicia la consulta de casos confirmados. El programa se repite hasta que el usuario ingrese una opción inválida o elija salir.

En resumen, este código es una aplicación sencilla para consultar el número de casos confirmados de COVID-19 en diferentes estados de México, organizados por regiones. El usuario selecciona la región y luego el estado de interés, y el programa muestra el número de casos confirmados en ese estado. Cabe mencionar que los datos en el diccionario pais son ficticios y que para obtener datos reales y actualizados, sería necesario obtenerlos de fuentes oficiales y mantener el diccionario actualizado con la información más reciente.
