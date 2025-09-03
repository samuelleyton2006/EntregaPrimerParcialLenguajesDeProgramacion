def afd_id(input_str):
    if not input_str:
        return False
    if not ((input_str >= 'a' and input_str <= 'z') or (input_str >= 'A' and input_str <= 'Z')):
        return False
    for c in input_str[1:]:
        if not ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')):
            return False
    return True

# Pruebas
pruebas = ['a123', 'Zalgo', 'juan99', '9inicio', 'a-b']
print([(s, afd_id(s)) for s in pruebas])
