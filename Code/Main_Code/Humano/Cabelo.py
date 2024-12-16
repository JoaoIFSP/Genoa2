import random
from Form import Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai

# Dicionário para mapear genes às cores
Cabelo = {
    8: "Moreno",    # Dominante
    4: "Preto",     # Dominante
    2: "Loiro",     # Recessivo
    1: "Ruivo"      # Recessivo
}

# Função para determinar a cor dos Cabelo do filho com base nos genes dos pais
def gerar_Cabelo_filho(Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai):
    # Seleção aleatória de genes da mãe e do pai
    gene_mae = random.choice(Zigoto_Cabelo_Mae)
    gene_pai = random.choice(Zigoto_Cabelo_Pai)

    # Soma dos genes para determinar a cor
    soma_Cabelo = gene_mae + gene_pai

    # Lógica de determinação da cor dos Cabelo com base na soma
    if soma_Cabelo == 12:  # Castanho e Preto juntos
        return random.choice(["Moreno", "Preto"]) 
    elif soma_Cabelo in [10, 9]:  # Predominância de Castanho
        return "Moreno"
    elif soma_Cabelo in [6, 5]:  # Predominância de Preto
        return "Preto"
    elif soma_Cabelo == 3:  # Recessivos (Azul e Verde)
        return random.choice(["Loiro", "Ruivo"])
    else:
        print(f"Erro: Soma inesperada ({soma_Cabelo}).")
        return "Indefinido"

