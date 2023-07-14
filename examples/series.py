import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']

numeric_labels = [1, 2, 3]

minha_lista = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a': 10, 'b': 20, 'c': 30}

# indices automaticos
indice = pd.Series(labels)
# imprime o conjunto de dados com indices iniciando de 0... de forma crescente
print(indice)

# indices atribuidos
indiceA = pd.Series(data=labels, index=minha_lista)
# imprime o conjunto de dados com indices atribuidos manualmente
print(indiceA)

dictionaryIndice = pd.Series(d)
# dicionarios sao compostos por chave:valor nesse caso a chave se tornam indices automaticos
print(dictionaryIndice)
