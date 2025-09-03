## Comparación de rendimiento: recursión, paralelismo y estilos en Python vs C

### Enunciado

Se pide comparar el rendimiento de un lenguaje compilado (C) y un lenguaje interpretado (Python) utilizando la función recursiva factorial, demostrando estilos variados de programación y midiendo los tiempos de resolución.

---

### Desarrollo en Python (interpretado)

Se implementan dos enfoques para el cálculo recursivo del factorial:

1. **Paralelismo con hilos:**  
   Se utiliza el módulo estándar `threading` para lanzar un hilo por cada número a calcular, midiendo el tiempo individual necesario para cada cómputo factorial con la función `tiempostomados`. Esto ilustra cómo el paralelismo puede modelarse con Python, aunque por la estructura interna del intérprete CPython (y el Global Interpreter Lock, GIL) la ganancia es limitada para cálculos puramente computacionales.

2. **Programación funcional (`map`):**  
   Se calcula el factorial de todos los valores de entrada en estilo funcional, midiendo el tiempo total requerido para el lote de operaciones usando la función `map` y la medición `time.time()`.

**Código fuente Python:**


- **Observaciones:**  
  - El cálculo paralelo no es necesariamente más rápido en Python, pero sirve para observar tiempos individuales y la concurrencia de tareas.
  - El estilo funcional es práctico y compacto, útil para comparar el tiempo de procesamiento contínuo.
  - Python es sencillo para prototipado, pero su rendimiento desciende con algoritmos recursivos profundos.

---

### Desarrollo en C (compilado)

En C se implementa la función factorial recursiva y se mide el tiempo de cómputo de dos formas:

1. **Cálculo secuencial:**  
   Se mide y muestra el tiempo que toma cada llamada recursiva individualmente usando funciones de medición a nivel de sistema (`gettimeofday`).

2. **Modo batch (lote):**  
   Se calcula el tiempo total en el que se procesan todos los valores de entrada en un ciclo.

**Código fuente C:**

