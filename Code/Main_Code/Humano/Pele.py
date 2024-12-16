import random
from Form import Zigoto_Pele_Mae, Zigoto_Pele_Pai

# Dicionário para mapear genes às cores
Pele = {
    8: "Negro",     # Dominante
    4: "Branco",    # Dominante
    2: "Amarelo",   # Recessivo
    1: "Pardo"      # Recessivo
}

# Função para determinar a cor dos Pele do filho com base nos genes dos pais
def gerar_Pele_filho(Zigoto_Pele_Mae, Zigoto_Pele_Pai):
    # Seleção aleatória de genes da mãe e do pai
    gene_mae = random.choice(Zigoto_Pele_Mae)
    gene_pai = random.choice(Zigoto_Pele_Pai)

    # Soma dos genes para determinar a cor
    soma_Pele = gene_mae + gene_pai

    # Lógica de determinação da cor dos Pele com base na soma
    if soma_Pele == 12:  # Castanho e Preto juntos
        return random.choice(["Negro", "Branco"]) 
    elif soma_Pele in [10, 9]:  # Predominância de Castanho
        return "Negro"
    elif soma_Pele in [6, 5]:  # Predominância de Preto
        return "Branco"
    elif soma_Pele == 3:  # Recessivos (Azul e Verde)
        return random.choice(["Amarelo", "Pardo"])
    else:
        print(f"Erro: Soma inesperada ({soma_Pele}).")
        return "Indefinido"

# Gerar a cor dos Pele do filho
