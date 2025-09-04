## Reconocimiento de cadenas con un Autómata Finito Determinista (AFD) en Python

### Problema

Dado el alfabeto \(Al = \{a, b, c\}\), construir un AFD que reconozca el conjunto de cadenas donde todas las 'a' preceden a todas las 'b', y todas las 'b' preceden a todas las 'c'. Es posible que no haya 'a', 'b' o 'c'.

---

### Expresión Regular

La expresión regular que específica este lenguaje es:


Esto significa: cualquier cantidad de 'a' (incluso cero), seguida de cualquier cantidad de 'b', seguida de cualquier cantidad de 'c', y siempre en ese orden.

---

### Definición Formal del AFD

- **Alfabeto:**  
  \(Al= \{a, b, c\}\)

- **Estados:**  
  \(Q = \{Q0, Q1, Q2\}\)

- **Estado inicial:**  
  \(Q0\)

- **Estados de aceptación:**  
  \(\{Q0, Q1, Q2\}\)

- **Función de transición \(\delta\):**

  | Estado | Entrada 'a' | Entrada 'b' | Entrada 'c' |
  |--------|:-----------:|:-----------:|:-----------:|
  | Q0     | Q0          | Q1          | Q2          |
  | Q1     | —           | Q1          | Q2          |
  | Q2     | —           | —           | Q2          |

---

![Image alt]https://github.com/samuelleyton2006/EntregaPrimerParcialLenguajesDeProgramacion/blob/46ba50e86d404475a1263e1593773bfc97fbc27c/Primer%20Parcial%20Lenguajes%20De%20Programacion%20/Primer_Punto/Terminal.jpg 


