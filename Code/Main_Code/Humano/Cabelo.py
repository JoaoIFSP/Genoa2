import random
from Form import Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai
from Genero import Genero, escolha_X_Y

# Dicionário para mapear genes às cores
Cabelo = {
    8: "Moreno",  # Dominante
    4: "Preto",     # Dominante
    2: "Loiro",     # Recessivo
    1: "Ruivo"       # Recessivo
}

# Função para gerar os Cabelo do filho
def gerar_Cabelo_filho(Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai):
    # Seleção aleatória de genes da mãe e do pai
    Zigoto_Cabelo_Filho = [0, 0]
    Zigoto_Cabelo_Filho[0] = random.choice(Zigoto_Cabelo_Mae)
    Zigoto_Cabelo_Filho[1] = random.choice(Zigoto_Cabelo_Pai)

    # Soma dos genes para determinar a cor
    soma_Cabelo = Zigoto_Cabelo_Filho[0] + Zigoto_Cabelo_Filho[1]

    # Lógica de determinação da cor dos Cabelo com base na soma
    if soma_Cabelo == 12:  # Castanho e Preto juntos
        cor = random.choice(["Moreno", "Preto"]) 
    elif soma_Cabelo in [16, 10, 9]:  # Predominância de Castanho
        cor = "Moreno"
    elif soma_Cabelo in [8, 6, 5]:  # Predominância de Preto
        cor = "Preto"
    elif soma_Cabelo == 4:
        cor = "Loiro"
    elif soma_Cabelo == 2:
        cor = "Ruivo"
    elif soma_Cabelo == 3:  # Recessivos (Azul e Verde)
        cor = random.choice(["Loiro", "Ruivo"])
    else:
        print(f"Erro: Soma inesperada ({soma_Cabelo}).")
        cor = "Indefinido"

    return Zigoto_Cabelo_Filho, cor
