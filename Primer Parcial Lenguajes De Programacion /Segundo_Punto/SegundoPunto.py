def AutomataID(input_str):
    if not input_str:
        return "no pasa"
    first = input_str[0]
    if not ((first >= 'a' and first <= 'z') or (first >= 'A' and first <= 'Z')):
        return "no pasa"
    for c in input_str[1:]:
        if not ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')):
            return "no pasa"
    return "si pasa"
pruebas = ['Martha21', 'g2python', 'CoreX', '123inicio', 'alg-uno']
print([(s, AutomataID(s)) for s in pruebas])
