def AutomataID(input_str):
    if not input_str:
        return False
    first = input_str[0]
    if not ((first >= 'a' and first <= 'z') or (first >= 'A' and first <= 'Z')):
        return False
    for c in input_str[1:]:
        if not ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')):
            return False
    return True
pruebas = ['a123', 'Zalgo', 'juan99', '9inicio', 'a-b']
print([(s, AutomataID(s)) for s in pruebas])
