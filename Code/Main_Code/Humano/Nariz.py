import random
from Form import Zigoto_Nariz_Mae, Zigoto_Nariz_Pai
from Genero import Genero, escolha_X_Y

# Dicionário para mapear genes às cores
Nariz = {
    8: "Largo",  # Dominante
    4: "Fino",     # Dominante
    2: "Redondo",     # Recessivo
    1: "Adunco"       # Recessivo
}

# Função para gerar os Nariz do filho
def gerar_Nariz_filho(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai):
    # Seleção aleatória de genes da mãe e do pai
    Zigoto_Nariz_Filho = [0, 0]
    Zigoto_Nariz_Filho[0] = random.choice(Zigoto_Nariz_Mae)
    Zigoto_Nariz_Filho[1] = random.choice(Zigoto_Nariz_Pai)

    # Soma dos genes para determinar a cor
    soma_Nariz = Zigoto_Nariz_Filho[0] + Zigoto_Nariz_Filho[1]

    # Lógica de determinação da cor dos Nariz com base na soma
    if soma_Nariz == 12:  # Castanho e Preto juntos
        cor = random.choice(["Largo", "Fino"]) 
    elif soma_Nariz in [16, 10, 9]:  # Predominância de Castanho
        cor = "Largo"
    elif soma_Nariz in [8, 6, 5]:  # Predominância de Preto
        cor = "Fino"
    elif soma_Nariz == 4:
        cor = "Redondo"
    elif soma_Nariz == 2:
        cor = "Adunco"
    elif soma_Nariz == 3:  # Recessivos (Azul e Verde)
        cor = random.choice(["Redondo", "Adunco"])
    else:
        print(f"Erro: Soma inesperada ({soma_Nariz}).")
        cor = "Indefinido"

    return Zigoto_Nariz_Filho, cor
