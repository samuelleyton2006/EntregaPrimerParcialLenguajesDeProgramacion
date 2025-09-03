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
