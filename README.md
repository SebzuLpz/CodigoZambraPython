Este código de Python es un programa que simula una encuesta sobre la población, donde se generan registros aleatorios de personas con sus respectivos datos (sexo, trabaja o no, sueldo). Luego, se pueden mostrar estadísticas sobre la población, como porcentajes de hombres y mujeres, porcentajes de hombres y mujeres que trabajan, y sueldos promedio de hombres y mujeres que trabajan.

Explicacion por partes:

*Importación de la biblioteca random*

La biblioteca random se utiliza para generar números aleatorios.

*Variables globales*

Se definen varias variables globales para almacenar los resultados de la encuesta:

- encuestas: una lista vacía que almacenará los registros generados aleatoriamente.
- hombre_total, mujer_total, hombre_trabaja_total, mujer_trabaja_total, hombre_sueldo_total, mujer_sueldo_total: variables que almacenarán los resultados de la encuesta.

*Función generar_registros()*

Esta función genera 10 registros aleatorios de personas, cada uno con un sexo (1 para hombre, 2 para mujer), un valor que indica si trabaja o no (1 para sí, 2 para no), y un sueldo aleatorio entre 600 y 2000 si trabaja, o 0 si no trabaja. Los registros se almacenan en la lista encuestas.

*Función calcular_estadisticas()*

Esta función calcula las estadísticas de la encuesta, como el número total de hombres y mujeres, el número de hombres y mujeres que trabajan, y el sueldo promedio de hombres y mujeres que trabajan.

*Funciones mostrar_estadisticas()*

Estas funciones muestran diferentes estadísticas de la encuesta, como porcentajes de hombres y mujeres, porcentajes de hombres y mujeres que trabajan, y sueldos promedio de hombres y mujeres que trabajan. Cada función muestra una estadística específica.

*Función main()*

Esta función es el punto de entrada del programa. Muestra un menú con opciones para generar registros aleatorios, mostrar estadísticas específicas, o salir del programa. Según la opción seleccionada, se llama a la función correspondiente.
