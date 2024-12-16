import random
from Form import Zigoto_Pele_Mae, Zigoto_Pele_Pai, Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai, Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai, Zigoto_Olho_Mae, Zigoto_Olho_Pai, Zigoto_Nariz_Mae, Zigoto_Nariz_Pai, Zigoto_Altura_Mae, Zigoto_Altura_Pai

# Importando as funções de geração de características
from Pele import gerar_Pele_filho
from Tipo_Cabelo import gerar_Tipo_Cabelo_filho
from Cabelo import gerar_Cabelo_filho
from Olhos import gerar_olhos_filho
from Nariz import gerar_Nariz_filho
from Altura import gerar_Altura_filho

# Função para gerar uma ficha de filho
def gerar_ficha_filho(numero):
    print(f"\nFilho número {numero}\n")
    print(f"Pele: {gerar_Pele_filho(Zigoto_Pele_Mae, Zigoto_Pele_Pai)}")
    print(f"Tipo de cabelo: {gerar_Tipo_Cabelo_filho(Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai)}")
    print(f"Cabelo: {gerar_Cabelo_filho(Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai)}")
    print(f"Olhos: {gerar_olhos_filho(Zigoto_Olho_Mae, Zigoto_Olho_Pai)}")
    print(f"Nariz: {gerar_Nariz_filho(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai)}")
    print(f"Altura: {gerar_Altura_filho(Zigoto_Altura_Mae, Zigoto_Altura_Pai)}")

# Gerar várias fichas de filhos
def gerar_varios_filhos(numero_filhos):
    for i in range(1, numero_filhos + 1):
        gerar_ficha_filho(i)

# Número de filhos a serem gerados
numero_filhos = 10
gerar_varios_filhos(numero_filhos)
