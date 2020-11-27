import numpy as np

# Definindo os vertices
# Obs: Os nomes entre aspas são usados para identificar o vertives,
# podem ser substituidos por letra ou nomes de cidades
vertices = {
  "1": 0,
  "2": 1,
  "3": 2,
  "4": 3,
  "5": 4,
  "6": 5,
  "7": 6,
  "8": 7,
  "9": 8,
  "10": 9,
  "11": 10,
  "12": 11,
  "13": 12,
  "14": 13,
  "15": 14,
  "16": 15,
}

# Criando uma matriz de adjacência
arestas = np.zeros([len(vertices), len(vertices)], dtype=int)

# Definindo a distância entre os vertices
arestas[vertices['1'], [vertices['2']]] = 15
arestas[vertices['1'], [vertices['3']]] = 10
arestas[vertices['1'], [vertices['4']]] = 17
arestas[vertices['2'], [vertices['3']]] = 4
arestas[vertices['2'], [vertices['5']]] = 10
arestas[vertices['2'], [vertices['13']]] = 16
arestas[vertices['3'], [vertices['5']]] = 15
arestas[vertices['3'], [vertices['4']]] = 5
arestas[vertices['4'], [vertices['6']]] = 21
arestas[vertices['4'], [vertices['7']]] = 10
arestas[vertices['5'], [vertices['12']]] = 20
arestas[vertices['5'], [vertices['6']]] = 10
arestas[vertices['6'], [vertices['11']]] = 22,
arestas[vertices['6'], [vertices['7']]] = 8
arestas[vertices['6'], [vertices['8']]] = 9
arestas[vertices['6'], [vertices['9']]] = 17
arestas[vertices['7'], [vertices['8']]] = 12
arestas[vertices['8'], [vertices['9']]] = 14
arestas[vertices['9'], [vertices['10']]] = 23
arestas[vertices['10'], [vertices['11']]] = 8
arestas[vertices['10'], [vertices['16']]] = 12
arestas[vertices['11'], [vertices['12']]] = 12
arestas[vertices['11'], [vertices['15']]] = 13
arestas[vertices['12'], [vertices['13']]] = 19
arestas[vertices['12'], [vertices['15']]] = 38
arestas[vertices['13'], [vertices['14']]] = 26
arestas[vertices['14'], [vertices['15']]] = 28
arestas[vertices['15'], [vertices['16']]] = 9


import sys

# Criando o algoritmo.
class Algoritmo:
  # Definindo atributos
  def __init__(self, vertices, arestas, inicio):
    self.tamanho = len(vertices)
    self.vertices = vertices
    self.grafo = arestas
    self.inicio = inicio

  # Método para mostrar o resultado.
  def mostra_solucao(self, distancias):
    print('Menores distâncias de {} até todos os outros'.format(self.vertices[self.inicio]))
    for vertice in range(self.tamanho):
      print(self.vertices[vertice], distancias[vertice])  

  # Método para calcular as distâncias minimas entre os vertices
  def distancia_minima(self, distancia, visitados):
    minimo = sys.maxsize
    for vertice in range(self.tamanho):
      if distancia[vertice] < minimo and visitados[vertice] == False:
        minimo = distancia[vertice]
        indice_minimo = vertice
    return indice_minimo

  # Algoritmo para o calcular a distância de um ponto até os demais.
  def calcular(self):
    distancia = [sys.maxsize] * self.tamanho
    distancia[self.inicio] = 0
    visitados = [False] * self.tamanho

    for _ in range(self.tamanho):
      indice_minimo = self.distancia_minima(distancia, visitados)
      visitados[indice_minimo] = True
      for vertice in range(self.tamanho):
        if self.grafo[indice_minimo][vertice] > 0 and visitados[vertice] == False \
            and distancia[vertice] > distancia[indice_minimo] + self.grafo[indice_minimo][vertice]:
          distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]

    self.mostra_solucao(distancia)


nomevertice = {
  0: '1',
  1: '2',
  2: '3',
  3: '4',
  4: '5',
  5: '6',
  6: '7',
  7: '8',
  8: '9',
  9: "10",
  10: "11",
  11: "12",
  12: "13",
  13: "14",
  14: "15",
  15: "16",
}

# Mostrar a distância de 1 a todos os outros pontos
umtodos = Algoritmo(nomevertice, arestas, vertices['1'])
umtodos.calcular() 

# Saida esperada:
# 1 0
# 2 15
# 3 10
# 4 15
# 5 25
# 6 35
# 7 25
# 8 37
# 9 51
# 10 74
# 11 57
# 12 45
# 13 31
# 14 57
# 15 70
# 16 79

# A distância minima entre 1 e 16 é 79