## Reconocimiento de cadenas con un Autómata Finito Determinista (AFD) en Python

### Problema

Dado el alfabeto \(\Sigma = \{a, b, c\}\), construir un AFD que reconozca el conjunto de cadenas donde todas las 'a' preceden a todas las 'b', y todas las 'b' preceden a todas las 'c'. Es posible que no haya 'a', 'b' o 'c'.

---

### Expresión Regular

La expresión regular que específica este lenguaje es:


Esto significa: cualquier cantidad de 'a' (incluso cero), seguida de cualquier cantidad de 'b', seguida de cualquier cantidad de 'c', y siempre en ese orden.

---

### Definición Formal del AFD

- **Alfabeto:**  
  \(\Sigma = \{a, b, c\}\)

- **Estados:**  
  \(Q = \{q_0, q_1, q_2\}\)

- **Estado inicial:**  
  \(q_0\)

- **Estados de aceptación:**  
  \(\{q_0, q_1, q_2\}\)

- **Función de transición \(\delta\):**

  | Estado | Entrada 'a' | Entrada 'b' | Entrada 'c' |
  |--------|:-----------:|:-----------:|:-----------:|
  | q0     | q0          | q1          | q2          |
  | q1     | —           | q1          | q2          |
  | q2     | —           | —           | q2          |

(—: transición no definida)

---

### Diagrama de Transiciones


