# A = (Q,Al,F,Q0,Qf)
# Q es el conjunto de estados 
# Al es el alfabeto de entrada 
# F lo definimos como Q * Al ---> Q   . F en si es la Funcion Total de transicion 
# Q0 Es el estado Inicial xd
# Qf Es el conjunto de estados Finales  


Al = {'a', 'b', 'c'}
Q = {'q0', 'q1', 'q2'}
Q0 = 'q0'
Qf = {'q0', 'q1', 'q2'}

def FuncionTranscicion(Estado, Simbolo):
    if Estado == 'q0':
        if Simbolo == 'a':
            return 'q0'
        elif Simbolo == 'b':
            return 'q1'
        elif Simbolo == 'c':
            return 'q2'
    elif Estado == 'q1':
        if Simbolo == 'b':
            return 'q1'
        elif Simbolo == 'c':
            return 'q2'
    elif Estado == 'q2':
        if Simbolo == 'c':
            return 'q2'
    return None

def AutomataIdCadenas(Cadena):
    Estado = Q0
    for Simbolo in Cadena:
        if Simbolo not in Al:
            return False
        SeguirLeyendo = FuncionTranscicion(Estado, Simbolo)
        if SeguirLeyendo is None:
            return False
        Estado = SeguirLeyendo  
    return Estado in Qf

CadenasExperimento = [
]

for Cadena in CadenasExperimento:
    print(f"{Cadena!r}: {'Se acepta la cadena' if AutomataIdCadenas(Cadena) else 'Compadre eso no va'}")
