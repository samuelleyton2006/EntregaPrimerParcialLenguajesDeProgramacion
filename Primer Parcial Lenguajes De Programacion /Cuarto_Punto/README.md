Enunciado
Realizar una comparación del rendimiento entre un lenguaje compilado y un lenguaje interpretado utilizando la función recursiva factorial, con medición de tiempos y aplicación de diferentes estilos de programación.
Fundamentación teórica
	•	Lenguaje compilado: El código fuente se traduce directamente a lenguaje máquina antes de la ejecución, lo que garantiza mayor eficiencia y velocidad en la ejecución de tareas computacionalmente intensivas.
	•	Lenguaje interpretado: El código fuente se traduce y ejecuta línea a línea en tiempo real; esto ofrece mayor flexibilidad, pero a costa de un rendimiento menor, especialmente en tareas recursivas pesadas.
Descripción de la prueba
	•	Función empleada: Factorial recursivo clásico.
	•	Pruebas realizadas: Se calcula el factorial de varios números (10, 12, 15, 18), midiendo el tiempo de ejecución de cada llamada.
	•	En Python: Se prueba tanto el cálculo en paralelo por hilos (threading) como el estilo funcional (map).
	•	En C: Se mide el tiempo de cada cálculo secuencialmente y también el tiempo total de un lote de cálculos (“batch”).
