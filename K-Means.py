import random
import math
import matplotlib.pyplot as plt

"""
@author: Fernanda P. Umberto
"""

def lerArquivo():
    dados=[]
    with open("r15.csv") as arquivo:
        for dado in arquivo.readlines():
            dado = list(map(float, dado.rstrip().split(',')))
            list.append(dados, dado)
    return dados

def selecionarCentroides(k: int, maximo: int):
    indices = []
    contador = 0
    while contador < k:
        numero = random.randint(0, maximo)
        if numero not in indices:
            indices.append(numero)
            contador+=1
    return indices

def distanciaEuclidiana(dado1, dado2):
    somatorio = 0
    for i in range(len(dado1)):
        somatorio+=math.pow((dado1[i]-dado2[i]), 2)
    return math.sqrt(somatorio)
    
def encontrarGrupoMaisProximo(dado, agrupamento):
    menorDistancia = distanciaEuclidiana(dado, agrupamento[0][0])
    grupoMaisProximo = agrupamento[0]
    tamanho = len(agrupamento)
    for indice in range(1, tamanho, 1):
        grupo = agrupamento[indice]
        distancia = distanciaEuclidiana(dado, grupo[0])
        if distancia < menorDistancia:
            menorDistancia = distancia
            grupoMaisProximo = grupo
    return grupoMaisProximo

def recalcularCentroide(grupo):
    colunas = len(grupo[0])
    linhas = len(grupo)
    centroide = [0 for i in range(colunas)]
    for i in range(1, linhas, 1):
        for j in range(colunas):
            centroide[j] += grupo[i][j]
    for i in range(colunas):
        centroide[i]/=(linhas-1)
    return centroide

def centroidesDiferentes(centroide, novoCentroide):
    colunas = len(centroide)
    for i in range(colunas):
        if centroide[i] != novoCentroide[i]:
            return True
    return False

def zerarGrupos(agrupamento):
    for grupo in agrupamento.values():
        centroide = grupo[0]
        grupo.clear()
        list.append(grupo, centroide)

def kMeans(k: int, dados):
    indices = selecionarCentroides(k, len(dados))
    agrupamento={}
    for i in range(k):
        grupo=[]
        centroide = dados[indices[i]]
        list.append(grupo, centroide)
        agrupamento[i] = grupo
    centroidesAlterados = True
    while centroidesAlterados:
        centroidesAlterados = False
        for dado in dados:
            grupoMaisProximo = encontrarGrupoMaisProximo(dado, agrupamento)
            list.append(grupoMaisProximo, dado)
        for grupo in agrupamento.values():
            novoCentroide = recalcularCentroide(grupo)
            if centroidesDiferentes(grupo[0], novoCentroide):
                centroidesAlterados = True
                grupo[0] = novoCentroide
        if centroidesAlterados:
            zerarGrupos(agrupamento)
    return agrupamento

def plotar(agrupamento):
    indice = 0
    for grupo in agrupamento.values():
        x = []
        y = []
        for dado in grupo:
            x.append(dado[0])
            y.append(dado[1])
        plt.scatter(x, y, label = 'Grupo ' + str(indice))
        indice += 1
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Agrupamento R15')
    plt.legend()
    plt.show()
        
dados = lerArquivo()
k = int(input('Digite o número de grupos:'))
agrupamento = kMeans(k, dados)
plotar(agrupamento)