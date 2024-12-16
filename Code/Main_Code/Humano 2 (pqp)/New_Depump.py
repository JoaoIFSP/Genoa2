import random

# Importar as funções de herança genética de cada característica
from Pele import gerar_Pele_filho
from Tipo_Cabelo import gerar_Tipo_Cabelo_filho
from Cabelo import gerar_Cabelo_filho
from Olhos import gerar_olhos_filho
from Nariz import gerar_Nariz_filho
from Altura import gerar_Altura_filho

# Importar os zigotos definidos no Form.py
from Form import (
    Zigoto_Pele_Mae, Zigoto_Pele_Pai,
    Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai,
    Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai,
    Zigoto_Olho_Mae, Zigoto_Olho_Pai,
    Zigoto_Nariz_Mae, Zigoto_Nariz_Pai,
    Zigoto_Altura_Mae, Zigoto_Altura_Pai
)

def gerar_caracteristicas_completas():
    """
    Função para gerar todas as características de um indivíduo com base nos genes dos pais.
    Retorna um dicionário contendo as características.
    """
    # Gerar características individuais
    pele = gerar_Pele_filho(Zigoto_Pele_Mae, Zigoto_Pele_Pai)
    tipo_cabelo = gerar_Tipo_Cabelo_filho(Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai)
    cor_cabelo = gerar_Cabelo_filho(Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai)
    cor_olhos = gerar_olhos_filho(Zigoto_Olho_Mae, Zigoto_Olho_Pai)
    tipo_nariz = gerar_Nariz_filho(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai)
    altura = gerar_Altura_filho(Zigoto_Altura_Mae, Zigoto_Altura_Pai)


if __name__ == "__main__":
    # Número de indivíduos para gerar
    n_individuos = 100

    print(f"Gerando características para {n_individuos} indivíduos:\n")

    for i in range(n_individuos):
        caracteristicas = gerar_caracteristicas_completas()
        print(f"Indivíduo {i + 1}: {caracteristicas}")
