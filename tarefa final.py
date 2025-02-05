# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:51:35 2025

@author: hugon
"""

from abc import ABC, abstractmethod

import random


class Veiculo(ABC):
    def __init__(self, nome,  velocidade_Max, numero_pneus):
        self.__velocidade_Max = float(velocidade_Max)
        self.__numero_pneus = numero_pneus
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome       
    
    @property
    def velocidade_Max(self):
        return self.__velocidade_Max
        
    @velocidade_Max.setter
    def velocidade_Max(self, velocidade_Max):
        self.__velocidade_Max = velocidade_Max
        
    @property
    def numero_pneus(self):
        return self.__numero_pneus
        
    @numero_pneus.setter
    def numero_pneus(self, numero_pneus):
        self.__numero_pneus = numero_pneus
    
    @abstractmethod
    def velocidade_media():
        pass
    
    @abstractmethod
    def desgaste_pneu():
        pass
    
class Moto(Veiculo):
    def __init__(self,nome,  velocidade_Max, numero_pneus):
        super().__init__(nome, velocidade_Max, numero_pneus)
        self.ativo = True
        self.pontuacao = 0
        
    def velocidade_media(self):
        velocidade_media = self.velocidade_Max*0.65
        velocidade_media_minima = velocidade_media - 15
        return velocidade_media, velocidade_media_minima
        
    def desgaste_pneu(self):
        return 0.95
    
class Formula(Veiculo):
    def __init__(self, nome, velocidade_Max, numero_pneus):
        super().__init__(nome, velocidade_Max, numero_pneus)
        self.ativo = True
        self.pontuacao = 0
        
    def velocidade_media(self):
        velocidade_media = self.velocidade_Max*0.75
        velocidade_media_minima = velocidade_media - 12
        return velocidade_media, velocidade_media_minima
        
    def desgaste_pneu(self):
        return 0.87
    
class Pista():
    def __init__(self, nome, comprimento, probabilidade_chuva, dificuldade):
        self.__nome = nome
        self.__comprimento = comprimento 
        self.__probabilidade_chuva = probabilidade_chuva
        self.__dificuldade = dificuldade
        
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome 
        
    @property
    def comprimento(self):
        return self.__comprimento
        
    @comprimento.setter
    def comprimento(self, comprimento):
        self.__comprimento = comprimento 

    @property
    def probabilidade_chuva(self):
        return self.__probabilidade_chuva
        
    @probabilidade_chuva.setter
    def probabilidade_chuva(self, probabilidade_chuva):
        self.__probabilidade_chuva = probabilidade_chuva 
        
    @property
    def dificuldade(self):
        return self.__dificuldade
        
    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade
    

def pit_stop():
    tempo = random.randint(25, 20)
    return tempo
        
    
        

def criar_equipa_moto():
    equipas_moto = []
    ducati = Moto("Ducati", 320, 2)
    equipas_moto.append(ducati)
    yamaha = Moto("Yamaha", 318, 2)
    equipas_moto.append(yamaha)
    ktm = Moto("KTM", 312,2)
    equipas_moto.append(ktm)
    honda = Moto("Honda", 317, 2)
    equipas_moto.append(honda)
    
    nome = input("Indique o nome da equipa")
    velocidade_Max = int(input("Indique a velocidade máxima entre 325 e 300"))
    
    moto1 = Moto(nome, velocidade_Max, 2)
    equipas_moto.append(moto1)
    
    return equipas_moto
    

def criar_equipa_formula():
    equipas_formula = []
    equipas_formula.append(Formula("Redbull", 335, 4))
    equipas_formula.append(Formula("Ferrari", 330, 4))
    equipas_formula.append(Formula("Mercedes", 322, 4))
    equipas_formula.append(Formula("McLaren", 328, 4))
    
    while True:
        nome = input("Indique o nome da equipa: ")
        
        # Verifica se já existe uma equipa com esse nome
        if any(equipa.nome == nome for equipa in equipas_formula):
            print("⚠️ Já existe uma equipa com esse nome! Tente novamente.")
        else:
            break
    velocidade = int(input("Indique a velocidade máxima (até 340km/h): "))
    
    formula1 = Formula(nome, velocidade, 2)
    equipas_formula.append(formula1)
    
    return equipas_formula
    

print("Olá, bem vindo ao centro dos desportos motorizados")

escolha = int(input("Indique o desporto que pretende seguir:\n 1 - MotoGP \n 2 - Formula 1\n"))

def equipa():
 equipa = []
 equipa_formula = []
 if escolha == 1:
     escolha_ficheiro = int(input("1 - Criar equipas \n2 - Carregar um ficheiro"))
     try: 
         if escolha_ficheiro == 1:
             ficheiro_moto = open('dados_motos.txt', 'r')
             for linha in ficheiro_moto:
                 linha = linha.strip()
                 if linha:
                     nome, velocidade, pneu = linha.split(',')
                     equipa = Moto(nome, velocidade, pneu)
                     equipa_motos.append(equipa)
            return equipa_motos
        
     else:
        equipa_motos = criar_equipa_moto()
        return equipa_motos
        
 else:
    escolha_ficheiro = int(input("1 - Criar equipas \n2 - Carregar um ficheiro"))
    if escolha_ficheiro == 2:
        try:
            ficheiro_carro = open('dados_carro.txt', 'r')
            for linha in ficheiro_carro:
                linha = linha.strip()
                if linha:
                    nome, velocidade, pneu = linha.split(',')
                    equipa = Formula(nome, velocidade, pneu)
                    equipa_formula.append(equipa)
                
                return equipa_formula
        except:
            print("Ficheiro não existe ou não foi lido corretamente")
            equipa_formula = criar_equipa_formula()
            return equipa_formula
    else escolha_ficheiro == 1:
        equipa_formula = criar_equipa_formula()
        return equipa_formula
        

def escolher_pista():
    
    while True:
        for index, pista in enumerate(pistas):
            print(index, pista.nome)
    
        pista_escolhida = input("Indique o número da pista que pretende correr ou digite 0 para realizar um campeonato!\n s- sair")

        if pista_escolhida.isdigit():
            pista_escolhida = int(pista_escolhida)
            
            if 0 <= pista_escolhida < len(pistas):
                return pista_escolhida
            elif pista_escolhida == 0:
                print("🏆 Iniciando campeonato...")
                return pista_escolhida
            else:
                print("⚠️ Número fora do intervalo! Escolha uma pista válida.")
        
        elif pista_escolhida.lower() == "s":
            break
        else:
            "Opção inválida, insira uma opção válida"
            
def numero_voltas():
    while True:
        numero_voltas = int(input("Indique o número de voltas que pretende. (20 a 40)"))
        
        if 2 <= numero_voltas <= 40:
            return numero_voltas
        else:
            print("Numero inválido, insira um número entre 20 e 40")
            
def simular_corrida(equipas, pista, numero_voltas):
    tempos_de_volta = {}
    melhor_volta = float('inf')  # Inicia com infinito para encontrar a menor volta
    melhor_volta_carro = ""
    
    # Verifica se choveu
    choveu = random.random() < pista.probabilidade_chuva
    if choveu:
        print(f"🌧️ Chove no grande prêmio do {pista.nome}")

    # Inicializa o dicionário de tempos de volta para cada carro
    for carro in equipas:
        tempos_de_volta[carro.nome] = []

    # Simulação de voltas
    for carro in equipas:
        if not carro.ativo:  
            continue
            
        velocidade_media, velocidade_media_minima = carro.velocidade_media()
        velocidade_media = int(velocidade_media)
        velocidade_media_minima = int(velocidade_media_minima)
        
        # Ajuste de velocidades em caso de chuva
        if choveu:
            velocidade_media -= 30
            velocidade_media_minima -= 50
            probabilidade = 0.01 + pista.dificuldade
        else:
            probabilidade = pista.dificuldade

        for volta in range(1, numero_voltas + 1):
            if random.random() < probabilidade:
                print(f"❌ {carro.nome} perdeu o controle e está FORA da corrida!")
                carro.ativo = False
                break  # Sai do loop de voltas se o carro não estiver mais ativo
            
            # Calcula o tempo da volta
            tempo_volta = (pista.comprimento / random.randint(velocidade_media_minima, velocidade_media))
            tempos_de_volta[carro.nome].append(tempo_volta)  # Adiciona o tempo da volta à lista
            
            # Verifica se a volta foi a melhor
            if tempo_volta < melhor_volta:
                print(f"🏆 Melhor volta feita por {carro.nome} na volta {volta} com {tempo_volta:.2f} min!")
                melhor_volta_carro = carro.nome
                melhor_volta = tempo_volta

    # Verifica carros que ainda estão na corrida
    carros_ativos = [c for c in equipas if c.ativo]
    if not carros_ativos:
        print("🏁 Todos os carros abandonaram! Fim da corrida!")
        return

    # Atribui pontos com base na posição
    resultados = sorted(carros_ativos, key=lambda c: sum(tempos_de_volta[c.nome]))  # Ordena pelos tempos totais
    for posicao, carro in enumerate(resultados):
        if posicao == 0:
            carro.pontuacao += 12  # 1º lugar
        elif posicao == 1:
            carro.pontuacao += 8   # 2º lugar
        elif posicao == 2:
            carro.pontuacao += 5   # 3º lugar
        elif posicao == 3:
            carro.pontuacao += 3   # 4º lugar
        elif posicao == 4:
            carro.pontuacao += 1   # 5º lugar

    # Atribui bônus de 1 ponto para o carro com a melhor volta
    if melhor_volta_carro:
        for carro in equipas:
            if carro.nome == melhor_volta_carro:
                carro.pontuacao += 1

    # Exibe a pontuação final
    print("\n🏁 Pontuação Final:")
    for carro in equipas:
        print(f"{carro.nome}: {carro.pontuacao} pontos")


pistas = []
qatar = Pista("Qatar", 5.38, 1, 0.005)
monaco = Pista("Monaco", 3.34, 0.1, 0.01)
spa = Pista("Spa-Francorchamps", 7, 0.05, 0.008)
brasil = Pista("Brasil", 4.31, 0.2, 0.01)
pistas.append(qatar)
pistas.append(monaco)
pistas.append(spa)
pistas.append(brasil)

    
equipa_escolhida = equipa()
numero_pista = escolher_pista()
pista = pistas[numero_pista]
numero_voltas = numero_voltas()

if pista != 0:
    simular_corrida(equipa_escolhida, pista, numero_voltas)
else:
    print("nada")
    


for i in equipa_escolhida:
        print(i.nome)
