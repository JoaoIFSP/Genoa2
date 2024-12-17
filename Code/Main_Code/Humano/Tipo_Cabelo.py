import random
from Form import Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai
from Genero import Genero, escolha_X_Y

# Dicionário para mapear genes às cores
Tipo_Cabelo = {
    8: "Crespo",  # Dominante
    4: "Liso",     # Dominante
    2: "Cacheado",     # Recessivo
    1: "Ondulado"       # Recessivo
}

# Função para gerar os Tipo_Cabelo do filho
def gerar_Tipo_Cabelo_filho(Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai):
    Zigoto_Tipo_Cabelo_Filho = [random.choice(Zigoto_Tipo_Cabelo_Mae), random.choice(Zigoto_Tipo_Cabelo_Pai)]
    soma_Tipo_Cabelo = Zigoto_Tipo_Cabelo_Filho[0] + Zigoto_Tipo_Cabelo_Filho[1]
    
    if soma_Tipo_Cabelo == 12:
        cor = random.choice(["Crespo", "Liso"])
    elif soma_Tipo_Cabelo in [16, 10, 9]:
        cor = "Crespo"
    elif soma_Tipo_Cabelo in [8, 6, 5]:
        cor = "Liso"
    elif soma_Tipo_Cabelo == 4:
        cor = "Cacheado"
    elif soma_Tipo_Cabelo == 2:
        cor = "Ondulado"
    elif soma_Tipo_Cabelo == 3:
        cor = random.choice(["Cacheado", "Ondulado"])
    else:
        cor = "Indefinido"
    
    return Zigoto_Tipo_Cabelo_Filho, cor
