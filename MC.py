from copy import deepcopy 

def simplificar_expresion(matriz, variables):
    expresiones_simplificadas = []

    # Función interna para simplificar un solo vector
    def simplificar_vector(vector):
        expresion = []
        for bit, variable in zip(vector, variables):
            if bit == '1':
                expresion.append(variable)
            elif bit == '0':
                expresion.append(variable + "'")
        return ''.join(expresion)

    # Procesar la matriz
    for vector in matriz:
        expresion = simplificar_vector(vector)
        expresiones_simplificadas.append(expresion)

    return expresiones_simplificadas

def count_1s(vector):
    return vector.count('1')

def group(binary_matrix: dict):
    groups = {}
    for w, vector in binary_matrix.items():
        quantity_1s = count_1s(vector)
        if quantity_1s not in groups:
            groups[quantity_1s] = {}
        groups[quantity_1s][w] = vector
    groups = dict(sorted(groups.items()))
    matrix_grouping = {tuple(value.keys()): list(value.values()) for value in groups.values()}
    return matrix_grouping

def v_d(v, dict_: dict):
    for values in dict_.values():
        for value in values:
            if value == v:
                return True
    return False

def one_bit_diference(vector_1, vector_2):
    return sum(b1 != b2 for b1, b2 in zip(vector_1, vector_2))

def sex(g_m: dict):
    s_t = {}
    sex_ready = set() 
    no_sex = deepcopy(g_m)
    length = len(g_m)
    c = [value.copy() for value in g_m.values()]
    weight = [numbers for numbers in g_m.keys()]
    weight_temp = deepcopy(weight)
    for i in range(length-1):
        for j in range(len(c[i])):
            vector1 = c[i][j]
            for k in range(len(c[i+1])):
                vector2 = c[i+1][k]
                if one_bit_diference(vector1, vector2) == 1:
                    vectors = set([tuple(vector1.copy()), tuple(vector2.copy())])
                    if not vectors in sex_ready:
                        new_vector = ['-' if b1 != b2 else b1 for b1, b2 in zip(vector1, vector2)]
                        if isinstance(weight[i][j], tuple):
                            numbers = weight[i][j] + weight[i+1][k]
                        else:
                            numbers = (weight[i][j], weight[i+1][k])
                        s_t.update({tuple(sorted(numbers, key=int)): new_vector})
                        sex_ready.update(vectors)
                        if v_d(vector1, no_sex):
                            no_sex[weight_temp[i]].remove(vector1)
                            n_p = list(weight_temp[i])
                            n_p.remove(weight[i][j])
                            no_sex[tuple(n_p)] = no_sex[weight_temp[i]].copy()
                            del no_sex[weight_temp[i]]
                            weight_temp[i] = tuple(n_p)
    return s_t, no_sex

def buscar_santi(implicantes: dict[tuple:list], apareamientos: dict):
    IPE = {}
    band = False
    for parejas, binarios in implicantes.items():
        for i in range(len(parejas)):
            pareja = parejas[i]
            if not isinstance(pareja, tuple):
                continue
            for pareja_ap in apareamientos.keys():
                if set(pareja).issubset(set(pareja_ap)):
                    band = False
                    break
                band = True
            if band: IPE[pareja] = binarios[i]
    IPE.update(apareamientos)
    return IPE