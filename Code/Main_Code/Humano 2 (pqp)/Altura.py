import random
from Form import Zigoto_Altura_Mae, Zigoto_Altura_Pai

# Dicionário para mapear genes às cores
Altura = {
    8: "1,70 m",    # Dominante
    4: "1,60 m",     # Dominante
    2: "1,90 m",     # Recessivo
    1: "1,40 m"      # Recessivo
}

# Função para determinar a cor dos Altura do filho com base nos genes dos pais
def gerar_Altura_filho(Zigoto_Altura_Mae, Zigoto_Altura_Pai):
    # Seleção aleatória de genes da mãe e do pai
    gene_mae = random.choice(Zigoto_Altura_Mae)
    gene_pai = random.choice(Zigoto_Altura_Pai)

    # Soma dos genes para determinar a cor
    soma_Altura = gene_mae + gene_pai

    # Lógica de determinação da cor dos Altura com base na soma
    if soma_Altura == 12:  # Castanho e Preto juntos
        return random.choice(["1,70 m", "1,60 m"]) 
    elif soma_Altura in [10, 9]:  # Predominância de Castanho
        return "1,70 m"
    elif soma_Altura in [6, 5]:  # Predominância de Preto
        return "1,60 m"
    elif soma_Altura == 3:  # Recessivos (Azul e Verde)
        return random.choice(["1,90 m", "1,40 m"])
    else:
        print(f"Erro: Soma inesperada ({soma_Altura}).")
        return "Indefinido"

# Gerar a cor dos Altura do filho
for i in range (100):
    cor_Altura_filho = gerar_Altura_filho(Zigoto_Altura_Mae, Zigoto_Altura_Pai)
    print(f"Altura do filho: {cor_Altura_filho}")
