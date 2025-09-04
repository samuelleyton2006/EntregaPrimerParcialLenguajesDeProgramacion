## Comparación de rendimiento: recursión, paralelismo y estilos en Python vs C

---

### Desarrollo en Python (interpretado)

![Imagealt](https://github.com/samuelleyton2006/EntregaPrimerParcialLenguajesDeProgramacion/blob/07dcfd806c6b04fc8bbcbfcf184ef23fa7633290/Primer%20Parcial%20Lenguajes%20De%20Programacion%20/Cuarto_Punto/TerminPy.jpg)

**Código fuente Python:**
``` python
import time
import threading

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def tiempostomados(n):  
    inicio = time.time()
    resultado = factorial(n)
    fin = time.time()
    print(f"El factorial de {n} = {resultado} tomando un tiempo de resolucion de: {fin-inicio:.6f} segundos")

def main():
    valores = [10, 12, 15, 18]
    hilos = []
    print("Cálculo factorial en paralelo (con hilos):")
    for v in valores:
        hilo = threading.Thread(target=tiempostomados, args=(v,))  
        hilos.append(hilo)
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print("\nAhora factorial en estilo funcional usando map():")
    inicio = time.time()
    resultados = list(map(factorial, valores))
    fin = time.time()
    for v, r in zip(valores, resultados):
        print(f"El factorial de {v} = {r}")
    print(f"La función resolvió todos en: {fin-inicio:.6f} segundos")

main()
```
---

### Desarrollo en C (compilado)

![Imagealt](https://github.com/samuelleyton2006/EntregaPrimerParcialLenguajesDeProgramacion/blob/07dcfd806c6b04fc8bbcbfcf184ef23fa7633290/Primer%20Parcial%20Lenguajes%20De%20Programacion%20/Cuarto_Punto/TerminC.jpg)

**Código fuente C:**
``` C
#include <stdio.h>
#include <sys/time.h>

int factorial(int n) {
    if(n <= 1) return 1;
    return n * factorial(n-1);
}

double tiempo_actual() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + tv.tv_usec/1e6;
}
int main() {
    int valores[] = {10, 12, 15, 18};
    int N = sizeof(valores)/sizeof(valores);
    printf("Secuencial factorial:\n");
    for(int i=0; i<N; i++) {
        double inicio = tiempo_actual();
        int resultado = factorial(valores[i]);
        double fin = tiempo_actual();
        printf("El factorial de (%d) = %d en %.6lfs\n", valores[i], resultado, fin-inicio);
    }
    printf("\nBatch (todos seguidos):\n");
    double inicio = tiempo_actual();
    for(int i=0; i<N; i++) {
        int resultado = factorial(valores[i]);
        printf("[El factorial(%d) = %d\n", valores[i], resultado);
    }
    double fin = tiempo_actual();
    printf("Todos los factoriales calculados en %.6lf segundos\n", fin-inicio);
    return 0;
}
```
