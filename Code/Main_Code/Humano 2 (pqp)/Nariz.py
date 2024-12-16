import random
from Form import Zigoto_Nariz_Mae, Zigoto_Nariz_Pai

# Dicionário para mapear genes às cores
Nariz = {
    8: "Largo",    # Dominante
    4: "Fino",     # Dominante
    2: "Redondo",     # Recessivo
    1: "Adunco"      # Recessivo
}

# Função para determinar a cor dos Nariz do filho com base nos genes dos pais
def gerar_Nariz_filho(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai):
    # Seleção aleatória de genes da mãe e do pai
    gene_mae = random.choice(Zigoto_Nariz_Mae)
    gene_pai = random.choice(Zigoto_Nariz_Pai)

    # Soma dos genes para determinar a cor
    soma_Nariz = gene_mae + gene_pai

    # Lógica de determinação da cor dos Nariz com base na soma
    if soma_Nariz == 12:  # Castanho e Preto juntos
        return random.choice(["Largo", "Fino"]) 
    elif soma_Nariz in [10, 9]:  # Predominância de Castanho
        return "Largo"
    elif soma_Nariz in [6, 5]:  # Predominância de Preto
        return "Fino"
    elif soma_Nariz == 3:  # Recessivos (Azul e Verde)
        return random.choice(["Redondo", "Adunco"])
    else:
        print(f"Erro: Soma inesperada ({soma_Nariz}).")
        return "Indefinido"

# Gerar a cor dos Nariz do filho
for i in range (100):
    cor_Nariz_filho = gerar_Nariz_filho(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai)
    print(f"Nariz do filho: {cor_Nariz_filho}")
