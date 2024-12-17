import random
from Form import Zigoto_Pele_Mae, Zigoto_Pele_Pai
from Genero import Genero, escolha_X_Y

# Dicionário para mapear genes às cores
Pele = {
    8: "Negro",  # Dominante
    4: "Branco",     # Dominante
    2: "Amarelo",     # Recessivo
    1: "Pardo"       # Recessivo
}

# Função para gerar os Pele do filho
def gerar_Pele_filho(Zigoto_Pele_Mae, Zigoto_Pele_Pai):
    # Seleção aleatória de genes da mãe e do pai
    Zigoto_Pele_Filho = [0, 0]
    Zigoto_Pele_Filho[0] = random.choice(Zigoto_Pele_Mae)
    Zigoto_Pele_Filho[1] = random.choice(Zigoto_Pele_Pai)

    # Soma dos genes para determinar a cor
    soma_Pele = Zigoto_Pele_Filho[0] + Zigoto_Pele_Filho[1]

    # Lógica de determinação da cor dos Pele com base na soma
    if soma_Pele == 12:  # Castanho e Preto juntos
        cor = random.choice(["Negro", "Branco"]) 
    elif soma_Pele in [16, 10, 9]:  # Predominância de Castanho
        cor = "Negro"
    elif soma_Pele in [8, 6, 5]:  # Predominância de Preto
        cor = "Branco"
    elif soma_Pele == 4:
        cor = "Amarelo"
    elif soma_Pele == 2:
        cor = "Pardo"
    elif soma_Pele == 3:  # Recessivos (Azul e Verde)
        cor = random.choice(["Amarelo", "Pardo"])
    else:
        print(f"Erro: Soma inesperada ({soma_Pele}).")
        cor = "Indefinido"

    return Zigoto_Pele_Filho, cor
