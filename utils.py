def convert_number_binary(number: int | str, length=4):
    if isinstance(number, str):
        if "0x" in number:
            number = int(number, 16)
    binary = int(number).to_bytes(length=4, signed=True)
    normal_binary = ''.join(format(byte, '08b') for byte in binary)
    return normal_binary[-length:]

def no_sex_data(no_apareados: dict[tuple:list]):
    lista_no_apareados = []
    for no_apareado in no_apareados.keys():
        aux = []
        if len(no_apareado) == 0:
            continue
        for minterminos in no_apareado:
            if isinstance(minterminos, tuple):
                aux.append(minterminos)
        if aux:
            lista_no_apareados.append(aux)

    return lista_no_apareados