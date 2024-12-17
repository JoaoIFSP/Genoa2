import random
from Form import Zigoto_Olho_Mae, Zigoto_Olho_Pai
from Genero import Genero

# Dicionário para mapear genes às cores
Olho = {
    8: "Castanho",  # Dominante
    4: "Preto",     # Dominante
    2: "Verde",     # Recessivo
    1: "Azul"       # Recessivo
}
Zigoto_Olho_Filho = [0, 0]
Zigoto_Olho_Filho[0] = random.choice(Zigoto_Olho_Mae)
Zigoto_Olho_Filho[1] = random.choice(Zigoto_Olho_Pai)
soma_olhos_inicial = Zigoto_Olho_Filho[0] + Zigoto_Olho_Filho[1]

if soma_olhos_inicial == 12:  # Castanho e Preto juntos
    primogenito = random.choice(["Preto", "Castanho"]) 
elif soma_olhos_inicial in [16, 10, 9]:  # Predominância de Castanho
    primogenito = "Castanho"
elif soma_olhos_inicial in [8, 6, 5]:  # Predominância de Preto
    primogenito = "Preto"
elif soma_olhos_inicial == 4:
    primogenito = "Verde"
elif soma_olhos_inicial == 2:
    primogenito = "Azul"
elif soma_olhos_inicial == 3:  # Recessivos (Azul e Verde)
    primogenito = random.choice(["Verde", "Azul"])
else:
    print(f"Erro: Soma inesperada ({soma_olhos_inicial}).")
    primogenito = "Indefinido"

    
def conversor_olhos(Zigoto_Olho_Mae, Zigoto_Olho_Pai, Zigoto_Olho_Filho, Genero):
    if Genero == "X":
        Zigoto_Olho_Mae = Zigoto_Olho_Filho
        Zigoto_Olho_Pai = [0, 0]
        Zigoto_Olho_Pai[0] = random.choice(8, 4, 2, 1)
        Zigoto_Olho_Pai[1] = random.choice(8, 4, 2, 1)
        return Zigoto_Olho_Mae, Zigoto_Olho_Pai
    elif Genero == "Y":
        Zigoto_Olho_Pai = Zigoto_Olho_Filho
        Zigoto_Olho_Mae = [0, 0]
        Zigoto_Olho_Mae[0] = random.choice(8, 4, 2, 1)
        Zigoto_Olho_Mae[1] = random.choice(8, 4, 2, 1)
        return Zigoto_Olho_Pai, Zigoto_Olho_Mae
    else:
        print("?????????????")
    
def gerar_olhos_filho(Zigoto_Olho_Mae, Zigoto_Olho_Pai, Zigoto_Olho_Filho):
    # Seleção aleatória de genes da mãe e do pai
    Zigoto_Olho_Filho[0] = random.choice(Zigoto_Olho_Mae)
    Zigoto_Olho_Filho[1] = random.choice(Zigoto_Olho_Pai)

    # Soma dos genes para determinar a cor
    soma_olhos = Zigoto_Olho_Filho[0] + Zigoto_Olho_Filho[1]

    # Lógica de determinação da cor dos olhos com base na soma
    if soma_olhos == 12:  # Castanho e Preto juntos
        return random.choice(["Preto", "Castanho"]) 
    elif soma_olhos in [16, 10, 9]:  # Predominância de Castanho
        return "Castanho"
    elif soma_olhos in [8, 6, 5]:  # Predominância de Preto
        return "Preto"
    elif soma_olhos == 4:
        return "Verde"
    elif soma_olhos == 2:
        return "Azul"
    elif soma_olhos == 3:  # Recessivos (Azul e Verde)
        return random.choice(["Verde", "Azul"])
    else:
        print(f"Erro: Soma inesperada ({soma_olhos}).")
        return "Indefinido"




