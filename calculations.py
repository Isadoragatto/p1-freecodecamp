import numpy as np

def calculate(numbers):
    # Verifica se a lista contém exatamente 9 elementos
    if len(numbers) != 9:
        raise ValueError("A lista deve conter nove números")
    
    # Converte a lista em um array Numpy 3x3
    matrix = np.array(numbers).reshape(3, 3)

    # Cálculo das estatísticas
    mean_axis1 = np.mean(matrix, axis=0).tolist()  # Média ao longo das colunas
    mean_axis2 = np.mean(matrix, axis=1).tolist()  # Média ao longo das linhas
    mean_flattened = np.mean(matrix).tolist()      # Média da matriz achatada
    
    variance_axis1 = np.var(matrix, axis=0).tolist()
    variance_axis2 = np.var(matrix, axis=1).tolist()
    variance_flattened = np.var(matrix).tolist()


    std_axis1 = np.std(matrix, axis=0).tolist()
    std_axis2 = np.std(matrix, axis=1).tolist()
    std_flattened = np.std(matrix).tolist()

    max_axis1 = np.max(matrix, axis=0).tolist()
    max_axis2 = np.max(matrix, axis=1).tolist()
    max_flattened = np.max(matrix).tolist()


    sum_axis1 = np.sum(matrix, axis=0).tolist()
    sum_axis2 = np.sum(matrix, axis=1).tolist()
    sum_flattened = np.sum(matrix).tolist()

    min_axis1 = np.min(matrix, axis=0).tolist()
    min_axis2 = np.min(matrix, axis=1).tolist()
    min_flattened = np.min(matrix).tolist()

# Cria o dicionário de resultados
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations

    from mean_var_std import calculate

# Teste a função com uma lista de 9 elementos
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
