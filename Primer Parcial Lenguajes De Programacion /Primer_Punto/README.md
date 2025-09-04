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



