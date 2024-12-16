import random
from Form import Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai

# Dicionário para mapear genes às cores
Tipo_Cabelo = {
    8: "Crespo",       # Dominante
    4: "Liso",         # Dominante
    2: "Cacheado",     # Recessivo
    1: "Ondulado"      # Recessivo
}

# Função para determinar a cor dos Tipo_Cabelo do filho com base nos genes dos pais
def gerar_Tipo_Cabelo_filho(Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai):
    # Seleção aleatória de genes da mãe e do pai
    gene_mae = random.choice(Zigoto_Tipo_Cabelo_Mae)
    gene_pai = random.choice(Zigoto_Tipo_Cabelo_Pai)

    # Soma dos genes para determinar a cor
    soma_Tipo_Cabelo = gene_mae + gene_pai

    # Lógica de determinação da cor dos Tipo_Cabelo com base na soma
    if soma_Tipo_Cabelo == 12:  # Castanho e Preto juntos
        return random.choice(["Crespo", "Liso"]) 
    elif soma_Tipo_Cabelo in [10, 9]:  # Predominância de Castanho
        return "Crespo"
    elif soma_Tipo_Cabelo in [6, 5]:  # Predominância de Preto
        return "Liso"
    elif soma_Tipo_Cabelo == 3:  # Recessivos (Azul e Verde)
        return random.choice(["Cacheado", "Ondulado"])
    else:
        print(f"Erro: Soma inesperada ({soma_Tipo_Cabelo}).")
        return "Indefinido"

# Gerar a cor dos Tipo_Cabelo do filho
