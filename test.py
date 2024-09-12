import re
import data_storage

def crear_dict_implicantes(primeImplicants, minterms):
    primeImplicantChart = {}  # Diccionario vacío

    # Crear el gráfico vacío con los primeros implicantes como claves y cadenas vacías como valores
    for implicant in primeImplicants:
        primeImplicantChart["".join(implicant)] = ""

    # Rellenar el gráfico basado en coincidencias con minterms
    for primeImplicant in primeImplicantChart.keys():
        regularExpression = covertir_re(primeImplicant)
        for minterm in minterms:
            # Si la expresión regular coincide con el minterm, añadir '1', de lo contrario, '0'
            if re.match(regularExpression, "".join(minterm)):
                primeImplicantChart[primeImplicant] += "1"
            else:
                primeImplicantChart[primeImplicant] += "0"

    return primeImplicantChart


def covertir_re(primeImplicant):
    regularExpression = ""
    # Convertir "-" a "\d" que representa cualquier dígito
    for char in primeImplicant:
        if char == "-":
            regularExpression += r"\d"
        else:
            regularExpression += char
    return regularExpression

def encontrar_implicantes_esenciales(primeImplicantChart):
    minterm_count = len(next(iter(primeImplicantChart.values())))  # Número de minterms
    minterm_coverage = [0] * minterm_count  # Lista para contar cuántos implicantes cubren cada minterm

    # Contar cuántos implicantes cubren cada minterm
    for implicant, coverage in primeImplicantChart.items():
        for i, bit in enumerate(coverage):
            if bit == '1':
                minterm_coverage[i] += 1

    essential_prime_implicants = []
    remaining_minterms = set()

    # Buscar los implicantes esenciales (cubren un minterm que no está cubierto por otros)
    for implicant, coverage in primeImplicantChart.items():
        is_essential = False
        for i, bit in enumerate(coverage):
            if bit == "1":
                if minterm_coverage[i] == 1:
                    is_essential = True
                if is_essential:
                    remaining_minterms.add(i)  # Añadir el minterm cubierto por el implicante esencial
                    
        if is_essential:
            essential_prime_implicants.append(implicant)

    # Retorna los implicantes esenciales y los minterms restantes que no están cubiertos
    return essential_prime_implicants, remaining_minterms



def cover_remaining_minterms(tabla_implicantes, implicantes_esenciales, remaining: set, minterminos):
    length = len(minterminos)
    sin_cubir = list(set(range(length)) - remaining)
    
    if not sin_cubir:
        return {}
    
    seleccion = {}
        
    for expresion, cubre in tabla_implicantes.items():
        if expresion in implicantes_esenciales:
            continue
        bits = cubre[sin_cubir[0]:]
        for bit in bits:
            if bit == "1":
                if seleccion.get(expresion, False):
                    seleccion[expresion] += 1
                else:
                    seleccion[expresion] = 1
    
    return seleccion

def seleccionar_expresion(seleccion: dict):
    values = list(seleccion.values())
    max_ = max(values)
    llaves_con_max_valor = [llave for llave, valor in seleccion.items() if valor == max_]

    expresion = max(llaves_con_max_valor, key=lambda x: x.count('-'))
    return expresion

def comprobacion(implicantes, minterminos_bin, minterminos):
    tabla_implicantes = crear_dict_implicantes(implicantes.values(), minterminos_bin)
    implicantes_esenciales, remaining = encontrar_implicantes_esenciales(tabla_implicantes)
    seleccion = cover_remaining_minterms(tabla_implicantes, implicantes_esenciales, remaining, minterminos)

    implicantes_esenciales.append(seleccionar_expresion(seleccion))
    data_storage.santi = implicantes_esenciales
    return implicantes_esenciales