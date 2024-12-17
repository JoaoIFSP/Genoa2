import random
from Form import Zigoto_Altura_Mae, Zigoto_Altura_Pai
from Genero import Genero, escolha_X_Y

# Dicionário para mapear genes às cores
Altura = {
    8: "1,70 m",  # Dominante
    4: "1,60 m",     # Dominante
    2: "1,90 m",     # Recessivo
    1: "1,40 m"       # Recessivo
}

# Função para gerar os Altura do filho
def gerar_Altura_filho(Zigoto_Altura_Mae, Zigoto_Altura_Pai):
    # Seleção aleatória de genes da mãe e do pai
    Zigoto_Altura_Filho = [0, 0]
    Zigoto_Altura_Filho[0] = random.choice(Zigoto_Altura_Mae)
    Zigoto_Altura_Filho[1] = random.choice(Zigoto_Altura_Pai)

    # Soma dos genes para determinar a cor
    soma_Altura = Zigoto_Altura_Filho[0] + Zigoto_Altura_Filho[1]

    # Lógica de determinação da cor dos Altura com base na soma
    if soma_Altura == 12:  # Castanho e Preto juntos
        cor = random.choice(["1,70 m", "1,60 m"]) 
    elif soma_Altura in [16, 10, 9]:  # Predominância de Castanho
        cor = "1,70 m"
    elif soma_Altura in [8, 6, 5]:  # Predominância de Preto
        cor = "1,60 m"
    elif soma_Altura == 4:
        cor = "1,90 m"
    elif soma_Altura == 2:
        cor = "1,40 m"
    elif soma_Altura == 3:  # Recessivos (Azul e Verde)
        cor = random.choice(["1,90 m", "1,40 m"])
    else:
        print(f"Erro: Soma inesperada ({soma_Altura}).")
        cor = "Indefinido"

    return Zigoto_Altura_Filho, cor
