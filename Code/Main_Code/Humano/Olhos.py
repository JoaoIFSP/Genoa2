import random
from Form import Zigoto_Olho_Mae, Zigoto_Olho_Pai
from Genero import Genero, escolha_X_Y

# Dicionário para mapear genes às cores
Olho = {
    8: "Castanho",  # Dominante
    4: "Preto",     # Dominante
    2: "Verde",     # Recessivo
    1: "Azul"       # Recessivo
}

# Função para gerar os olhos do filho
def gerar_olhos_filho(Zigoto_Olho_Mae, Zigoto_Olho_Pai):
    # Seleção aleatória de genes da mãe e do pai
    Zigoto_Olho_Filho = [0, 0]
    Zigoto_Olho_Filho[0] = random.choice(Zigoto_Olho_Mae)
    Zigoto_Olho_Filho[1] = random.choice(Zigoto_Olho_Pai)

    # Soma dos genes para determinar a cor
    soma_olhos = Zigoto_Olho_Filho[0] + Zigoto_Olho_Filho[1]

    # Lógica de determinação da cor dos olhos com base na soma
    if soma_olhos == 12:  # Castanho e Preto juntos
        cor = random.choice(["Preto", "Castanho"]) 
    elif soma_olhos in [16, 10, 9]:  # Predominância de Castanho
        cor = "Castanho"
    elif soma_olhos in [8, 6, 5]:  # Predominância de Preto
        cor = "Preto"
    elif soma_olhos == 4:
        cor = "Verde"
    elif soma_olhos == 2:
        cor = "Azul"
    elif soma_olhos == 3:  # Recessivos (Azul e Verde)
        cor = random.choice(["Verde", "Azul"])
    else:
        print(f"Erro: Soma inesperada ({soma_olhos}).")
        cor = "Indefinido"

    return Zigoto_Olho_Filho, cor

