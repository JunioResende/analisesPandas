import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']

numeric_labels = [1, 2, 3]

minha_lista = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a': 10, 'b': 20, 'c': 30}

print('# indices automaticos')
indice = pd.Series(labels)
print('# imprime o conjunto de dados com indices iniciando de 0... de forma crescente')
print(indice)

print('# indices atribuidos')
indiceA = pd.Series(data=labels, index=minha_lista)
print('# imprime o conjunto de dados com indices atribuidos manualmente')
print(indiceA)

dictionaryIndice = pd.Series(d)
print('# dicionarios sao compostos por chave:valor nesse caso a chave se tornam indices automaticos')
print(dictionaryIndice)

paises = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai']
indexPais = [1, 2, 3, 4]
populacao = [564654881.3, 1688465.5, 1685321.16, 4549884.12]

ser1 = pd.Series(index=indexPais, data=paises)

print(ser1)
