from string import ascii_uppercase
import graphic as G 
import utils
import data_storage
import MC
from copy import deepcopy
import test as T


def entry_weight (weights):
    weights = weights.split(',')
    weights = [item.strip() for item in weights]
    weights.sort(key=int)
    return weights 

def proces_vars (weights):
    last_weight = int(weights[-1])
    quantity_vars = len(bin(last_weight)) - 2
    vars = list(ascii_uppercase[:quantity_vars])
    return vars

def binary (weights , count_vars):
    return [utils.convert_number_binary(w, count_vars) for w in weights]

def create_binary_matrix ( binary_weights , weights ):
    return {w: list(b_w) for w, b_w in zip(weights, binary_weights)}

def mc_challenge (g_m):
    simplified_terms = []
    nosex = {}
    final_result = []
    while True:
        simplified_terms, no_sex_vector = MC.sex(g_m)
        if len(simplified_terms) == 0:
            break
        final_result = deepcopy(simplified_terms)
        data_storage.sex.append(final_result.copy())
        nosex.update(no_sex_vector)
        g_m = MC.group(simplified_terms)
        data_storage.grouping.append(g_m)
    return final_result, nosex


    







if __name__ == "__main__" :
    numeros = G.obtener_entrada_usuario()
    inputs = G.procesar_numeros(numeros)
    weight = entry_weight(inputs)
    #print(weight)#
    vars = proces_vars(weight)
    #print(vars)#
    count_vars = len(vars)
    binary_weights = binary(weight , count_vars)
    #print(binary_weights)#
    binary_matrix = create_binary_matrix(binary_weights,weight)
    #print(binary_matrix)#
    data_storage.first_binary.append(binary_matrix)
    matrix_grouping = MC.group(binary_matrix)
    #print(matrix_grouping)#
    simplified_terms,nosex = mc_challenge(matrix_grouping)
    #print(nosex)#
    data_storage.no_sex = utils.no_sex_data(nosex)
    santi = MC.buscar_santi(nosex,simplified_terms)
    data_storage.santi = santi
    final_result = T.comprobacion(santi,binary_weights,weight)
    print(final_result)
    results = MC.simplificar_expresion(final_result,vars)
    print(results)
    G.mostrar_resultados(final_result,results)



























































































































































































































































































































































