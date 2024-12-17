import random
from Olhos import gerar_olhos_filho  # Nome correto da função
from Cabelo import gerar_Cabelo_filho
from Tipo_Cabelo import gerar_Tipo_Cabelo_filho
from Pele import gerar_Pele_filho
from Nariz import gerar_Nariz_filho
from Altura import gerar_Altura_filho
from Genero import escolha_X_Y
from Form import Zigoto_Olho_Mae, Zigoto_Olho_Pai, Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai, Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai, Zigoto_Pele_Mae, Zigoto_Pele_Pai, Zigoto_Nariz_Mae, Zigoto_Nariz_Pai, Zigoto_Altura_Mae, Zigoto_Altura_Pai

# Função para gerar múltiplas gerações com todas as características unidas
def gerar_geracoes(num_geracoes, 
                    Zigoto_Olhos_Mae, Zigoto_Olhos_Pai,
                    Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai,
                    Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai,
                    Zigoto_Pele_Mae, Zigoto_Pele_Pai,
                    Zigoto_Nariz_Mae, Zigoto_Nariz_Pai,
                    Zigoto_Altura_Mae, Zigoto_Altura_Pai):
    
    for geracao in range(1, num_geracoes + 1):
        Genero = escolha_X_Y()  # Determina o gênero
        
        # Gerar os filhos para todos os genes
        Zigoto_Olhos_Filho, cor_Olhos = gerar_olhos_filho(Zigoto_Olhos_Mae, Zigoto_Olhos_Pai)
        Zigoto_Cabelo_Filho, cor_Cabelo = gerar_Cabelo_filho(Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai)
        Zigoto_Tipo_Cabelo_Filho, cor_Tipo_Cabelo = gerar_Tipo_Cabelo_filho(Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai)
        Zigoto_Pele_Filho, cor_Pele = gerar_Pele_filho(Zigoto_Pele_Mae, Zigoto_Pele_Pai)
        Zigoto_Nariz_Filho, cor_Nariz = gerar_Nariz_filho(Zigoto_Nariz_Mae, Zigoto_Nariz_Pai)
        Zigoto_Altura_Filho, cor_Altura = gerar_Altura_filho(Zigoto_Altura_Mae, Zigoto_Altura_Pai)

        # Imprime os resultados da geração atual
        print(f"Geração {geracao}:")
        print(f"Gênero: {Genero}")
        print("\n")
        print(f"Olhos Mãe/Pai:          ({Zigoto_Olhos_Mae}) / ({Zigoto_Olhos_Pai})")
        print(f"Cabelo Mãe/Pai:         ({Zigoto_Cabelo_Mae}) / ({Zigoto_Cabelo_Pai})")
        print(f"Tipo de cabelo Mãe/Pai: ({Zigoto_Tipo_Cabelo_Mae}) / ({Zigoto_Tipo_Cabelo_Pai})")
        print(f"Pele Mãe/Pai:           ({Zigoto_Pele_Mae}) / ({Zigoto_Pele_Pai})")
        print(f"Nariz Mãe/Pai           ({Zigoto_Nariz_Mae}) / ({Zigoto_Nariz_Pai})")
        print(f"Altura Mãe/Pai          ({Zigoto_Altura_Mae}) / ({Zigoto_Altura_Pai})")
        print("\n")
        print(f"Olhos Filho:                 ({Zigoto_Olhos_Filho})")
        print(f"Cabelo Filho:                ({Zigoto_Cabelo_Filho})")
        print(f"Tipo de Cabelo Filho:        ({Zigoto_Tipo_Cabelo_Filho})")
        print(f"Pele Filho:                  ({Zigoto_Pele_Filho})")
        print(f"Nariz Filho:                 ({Zigoto_Nariz_Filho})")
        print(f"Altura FIlho:                ({Zigoto_Altura_Filho})")
        print("\n")
        print(f"Olhos: {cor_Olhos}")
        print(f"Cabelo: {cor_Cabelo} ")
        print(f"Tipo de Cabelo: {cor_Tipo_Cabelo} ")
        print(f"Cor da Pele: {cor_Pele} ")
        print(f"Formato do Nariz: {cor_Nariz} ")
        print(f"Altura: {cor_Altura} ")
        print("-" * 30)
        
        # Atualiza os genes com base no gênero
        if Genero == "X":
            Zigoto_Olhos_Mae = Zigoto_Olhos_Filho
            Zigoto_Olhos_Pai = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Cabelo_Mae = Zigoto_Cabelo_Filho
            Zigoto_Cabelo_Pai = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Tipo_Cabelo_Mae = Zigoto_Tipo_Cabelo_Filho
            Zigoto_Tipo_Cabelo_Pai = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Pele_Mae = Zigoto_Pele_Filho
            Zigoto_Pele_Pai = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Nariz_Mae = Zigoto_Nariz_Filho
            Zigoto_Nariz_Pai = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Altura_Mae = Zigoto_Altura_Filho
            Zigoto_Altura_Pai = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
        elif Genero == "Y":
            Zigoto_Olhos_Pai = Zigoto_Olhos_Filho
            Zigoto_Olhos_Mae = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Cabelo_Pai = Zigoto_Cabelo_Filho
            Zigoto_Cabelo_Mae = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Tipo_Cabelo_Pai = Zigoto_Tipo_Cabelo_Filho
            Zigoto_Tipo_Cabelo_Mae = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Pele_Pai = Zigoto_Pele_Filho
            Zigoto_Pele_Mae = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Nariz_Pai = Zigoto_Nariz_Filho
            Zigoto_Nariz_Mae = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]
            
            Zigoto_Altura_Pai = Zigoto_Altura_Filho
            Zigoto_Altura_Mae = [random.choice([8, 4, 2, 1]), random.choice([8, 4, 2, 1])]

# Configuração inicial
num_geracoes = 10  # Defina o número de gerações diretamente no código

# Chame a função passando os zigotos iniciais de Form.py
gerar_geracoes(num_geracoes, 
                Zigoto_Olho_Mae, Zigoto_Olho_Pai,
                Zigoto_Cabelo_Mae, Zigoto_Cabelo_Pai,
                Zigoto_Tipo_Cabelo_Mae, Zigoto_Tipo_Cabelo_Pai,
                Zigoto_Pele_Mae, Zigoto_Pele_Pai,
                Zigoto_Nariz_Mae, Zigoto_Nariz_Pai,
                Zigoto_Altura_Mae, Zigoto_Altura_Pai)
