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
        printf("[REC] factorial(%d) = %d en %.6lfs\n", valores[i], resultado, fin-inicio);
    }
    printf("\nBatch (todos seguidos):\n");
    double inicio = tiempo_actual();
    for(int i=0; i<N; i++) {
        int resultado = factorial(valores[i]);
        printf("[BATCH] factorial(%d) = %d\n", valores[i], resultado);
    }
    double fin = tiempo_actual();
    printf("Todos (batch) calculados en %.6lf segundos\n", fin-inicio);
    return 0;
}
