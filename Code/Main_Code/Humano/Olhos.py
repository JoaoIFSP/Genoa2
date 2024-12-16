import random
from Form import Zigoto_Olho_Mae, Zigoto_Olho_Pai

# Dicionário para mapear genes às cores
Olho = {
    8: "Castanho",  # Dominante
    4: "Preto",     # Dominante
    2: "Verde",     # Recessivo
    1: "Azul"       # Recessivo
}

# Função para determinar a cor dos olhos do filho com base nos genes dos pais
def gerar_olhos_filho(Zigoto_Olho_Mae, Zigoto_Olho_Pai):
    # Seleção aleatória de genes da mãe e do pai
    gene_mae = random.choice(Zigoto_Olho_Mae)
    gene_pai = random.choice(Zigoto_Olho_Pai)

    # Soma dos genes para determinar a cor
    soma_olhos = gene_mae + gene_pai

    # Lógica de determinação da cor dos olhos com base na soma
    if soma_olhos == 12:  # Castanho e Preto juntos
        return random.choice(["Preto", "Castanho"]) 
    elif soma_olhos in [10, 9]:  # Predominância de Castanho
        return "Castanho"
    elif soma_olhos in [6, 5]:  # Predominância de Preto
        return "Preto"
    elif soma_olhos == 3:  # Recessivos (Azul e Verde)
        return random.choice(["Verde", "Azul"])
    else:
        print(f"Erro: Soma inesperada ({soma_olhos}).")
        return "Indefinido"

# Gerar a cor dos olhos do filho

