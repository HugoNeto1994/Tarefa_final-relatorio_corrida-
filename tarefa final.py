# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:51:35 2025

@author: hugon
"""

from abc import ABC, abstractmethod

import random

mensagem =""
class Veiculo(ABC):
    def __init__(self, nome,  velocidade_Max, numero_pneus):
        self.__velocidade_Max = float(velocidade_Max)
        self.__numero_pneus = numero_pneus
        self.__nome = nome
        self.__ativo = True
        self.__pontuacao = 0
        self.__pontuacaoTotal = 0

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
    
    @property
    def ativo(self):
        return self.__ativo
        
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo
        
    @property
    def pontuacao(self):
        return self.__pontuacao
        
    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

    @property
    def pontuacaoTotal(self):
        return self.__pontuacaoTotal
        
    @pontuacaoTotal.setter
    def pontuacaoTotal(self, pontuacaoTotal):
        self.__pontuacaoTotal = pontuacaoTotal
    
    @abstractmethod
    def velocidade_media():
        pass
    
    @abstractmethod
    def desgaste_pneu():
        pass
    
class Moto(Veiculo):
    def __init__(self,nome,  velocidade_Max, numero_pneus):
        super().__init__(nome, velocidade_Max, numero_pneus)

        
    def velocidade_media(self):
        velocidade_media = self.velocidade_Max*0.65
        velocidade_media_minima = velocidade_media - 15
        return velocidade_media, velocidade_media_minima
        
    def desgaste_pneu(self):
        return 0.95
    
class Formula(Veiculo):
    def __init__(self, nome, velocidade_Max, numero_pneus):
        super().__init__(nome, velocidade_Max, numero_pneus)
        
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
    tempo = random.randint(20, 25)
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
        if any(equipa.nome.lower() == nome.strip().lower() for equipa in equipas_formula):
            print("⚠️ Já existe uma equipa com esse nome! Tente novamente.")
        else:
            break
    velocidade = int(input("Indique a velocidade máxima (até 340km/h): "))
    
    formula1 = Formula(nome, velocidade, 2)
    equipas_formula.append(formula1)
    
    return equipas_formula

def imprimir_ficheiro(mensagem):
    ficheiro = open('relatorio_corrida.txt', 'w')
    ficheiro.write(mensagem)
    ficheiro.close()
    

print("\nOlá, bem vindo ao centro dos desportos motorizados\n")

escolha = int(input("Indique o desporto que pretende seguir:\n 1 - MotoGP \n 2 - Formula 1\n"))

def equipa():
 equipa = []
 if escolha == 1:
     escolha_ficheiro = int(input("1 - Criar equipas \n2 - Carregar um ficheiro"))
     if escolha_ficheiro == 2:
         try: 
             ficheiro_moto = open('dados_motos.txt', 'r')
             for linha in ficheiro_moto:
                 linha = linha.strip()
                 if linha:
                     nome, velocidade, pneu = linha.split(',')
                     moto = Moto(nome, velocidade, pneu)
                     equipa.append(moto)
         except:
              print("Ficheiro não existe ou não foi lido corretamente")
              equipa = criar_equipa_moto()
        
     else:
        equipa = criar_equipa_moto()
        
 else:
    escolha_ficheiro = int(input("1 - Criar equipas \n2 - Carregar um ficheiro"))
    if escolha_ficheiro == 2:
        try:
            ficheiro_carro = open('dados_carro.txt', 'r')
            for linha in ficheiro_carro:
                linha = linha.strip()
                if linha:
                    nome, velocidade, pneu = linha.split(',')
                    carro = Formula(nome, velocidade, pneu)
                    equipa.append(carro)
        except:
            print("Ficheiro não existe ou não foi lido corretamente")
            equipa = criar_equipa_formula()
            
    else:
        equipa = criar_equipa_formula()
 return equipa   

def escolher_pista():
    
    while True:
        for index, pista in enumerate(pistas, start=1):
            print(index, pista.nome)
    
        pista_escolhida = input("Indique o número da pista que pretende correr ou digite 0 para realizar um campeonato!\n s- sair")

        if pista_escolhida.isdigit():
            pista_escolhida = int(pista_escolhida)
            
            if 1 <= pista_escolhida < len(pistas)+1:
                return pista_escolhida
            elif pista_escolhida == 0:
                print("🏆 Iniciando campeonato...")
                return pista_escolhida
            else:
                print("⚠️ Número fora do intervalo! Escolha uma pista válida.")
        
        elif pista_escolhida.lower() == "s":
            return "s"
        else:
            "Opção inválida, insira uma opção válida"
            
def numero_voltas():
    while True:
        numero_voltas = int(input("Indique o número de voltas que pretende. (20 a 40)"))
        
        if 2 <= numero_voltas <= 40:
            return numero_voltas
        else:
            print("Numero inválido, insira um número entre 20 e 40")

def formatar_tempo(tempo_em_min):
    tempo_em_segundos = tempo_em_min * 60  
    minutos, segundos = divmod(tempo_em_segundos, 60)  
    return f"{int(minutos)} min {segundos:.2f} s"  

            
def simular_corrida(equipas, pista, numero_voltas, mensagem, campeonato):
    tempos_de_volta = {}
    melhor_volta = float('inf') 
    melhor_volta_carro = ""
    
    if not campeonato:
        mensagem += (f"Bem vindo ao Grande Prémio {pista.nome}\n")
    
    for i in equipas:
        i.ativo = True
        i.pontuacao = 0
    
    # Verifica se choveu
    choveu = random.random() < pista.probabilidade_chuva
    if choveu and not campeonato:
        mensagem +=(f"🌧️ Chove no grande prêmio do {pista.nome}\n")

    # Inicializa o dicionário de tempos de volta para cada carro
    for carro in equipas:
        tempos_de_volta[carro.nome] = []

    # Dicionário para armazenar os tempos de cada carro por volta
    tempos_por_volta = {volta: [] for volta in range(1, numero_voltas + 1)}

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
                if not campeonato:
                 mensagem +=(f"❌ {carro.nome} perdeu o controle e está FORA da corrida!\n")
                 carro.ativo = False
                 break  # Sai do loop de voltas se o carro não estiver mais ativo
            
            # Calcula o tempo da volta
            tempo_volta = ((pista.comprimento * 60) / random.randint(velocidade_media_minima, velocidade_media))
            tempos_de_volta[carro.nome].append(tempo_volta)  # Adiciona o tempo da volta à lista
            
            # Guarda o tempo e o carro na volta correspondente
            tempos_por_volta[volta].append((carro.nome, tempo_volta))
        
        if numero_voltas >= 30:
            tempo = pit_stop()
            print(f"Paragem de {tempo} para a {carro.nome}")
            tempos_de_volta[carro.nome].append(tempo)
    
    
        
    if not campeonato:
     for volta, tempos in tempos_por_volta.items():
        for carro_nome, tempo in tempos:
            # Verifica se é a melhor volta
            if tempo < melhor_volta:
                melhor_volta_carro = carro_nome
                melhor_volta = tempo
                mensagem += (f"🏆 Melhor volta feita por {carro_nome} na volta {volta} com {formatar_tempo(tempo)}\n")
    
     # Verifica carros que ainda estão na corrida
    if campeonato or not campeonato:
      carros_ativos = [c for c in equipas if c.ativo]
      if not carros_ativos:
         mensagem += ("🏁 Todos os carros abandonaram! Fim da corrida!\n")
         return

    # Atribui pontos com base na posição
    if campeonato or not campeonato:
     resultados = sorted(carros_ativos, key=lambda c: sum(tempos_de_volta[c.nome]))  # Ordena pelos tempos totais
     for posicao, carro in enumerate(resultados):
        if posicao == 0:
            carro.pontuacao = 12  # 1º lugar
            carro.pontuacaoTotal += 12
        elif posicao == 1:
            carro.pontuacao = 8   # 2º lugar
            carro.pontuacaoTotal +=8
        elif posicao == 2:
            carro.pontuacao = 5   # 3º lugar
            carro.pontuacaoTotal +=5
        elif posicao == 3:
            carro.pontuacao = 3   # 4º lugar
            carro.pontuacaoTotal +=3
        elif posicao == 4:
            carro.pontuacao = 1   # 5º lugar
            carro.pontuacaoTotal +=1
        else:
            carro.pontuacao = 0

    # Atribui bônus de 1 ponto para o carro com a melhor volta
    if melhor_volta_carro:
        for carro in equipas:
            if carro.nome == melhor_volta_carro and carro.ativo:
                carro.pontuacao += 1

    # Exibe a pontuação final
    if not campeonato:
     mensagem += (f"\n🏁 Pontuação Final Grande prémio {pista.nome}:\n")
     for carro in equipas:
        if carro.ativo:
            mensagem += (f"{carro.nome:<10} |Pontos: {carro.pontuacao:<3} | Tempo: {formatar_tempo(sum(tempos_de_volta[carro.nome]))}\n")
        else:
            mensagem += (f"{carro.nome:<10} |Pontos: {carro.pontuacao:<3} | ❌ {carro.nome} não terminou\n")
    else:
        mensagem += (f"\n🏁 Pontuação Final Grande prémio {pista.nome}:\n")
        for carro in equipas:
           mensagem += (f"{carro.nome:<10} |Pontos: {carro.pontuacao:<3}\n")
           
    return mensagem

pistas = []
qatar = Pista("Qatar", 5.38, 0.01, 0.005)
monaco = Pista("Monaco", 3.34, 0.1, 0.01)
spa = Pista("Spa-Francorchamps", 7, 0.15, 0.008)
brasil = Pista("Brasil", 4.31, 0.65, 0.01)
pistas.append(qatar)
pistas.append(monaco)
pistas.append(spa)
pistas.append(brasil)

 
equipa_escolhida = equipa()
numero_pista = escolher_pista()


if  numero_pista == "s": 
    print("Até uma próxima!")
else:    
    if numero_pista != 0:
        numero_voltas = numero_voltas()
        pista = pistas[numero_pista-1]
        campeonato = False
        mensagem = simular_corrida(equipa_escolhida, pista, numero_voltas, mensagem, campeonato)
        print(mensagem)
        imprimir_ficheiro(mensagem)
    elif numero_pista == 0:
        numero_voltas = numero_voltas()
        for i in pistas:
            campeonato = True
            mensagem += simular_corrida(equipa_escolhida, i, numero_voltas, "", campeonato) 
        mensagem += ("\n🏁 Pontuação Final do campeonato:\n")
        for carro in equipa_escolhida:
          pontuacaoT = carro.pontuacaoTotal
          mensagem += (f"{carro.nome:<10} |Pontos: {pontuacaoT:<3}\n")  
        print(mensagem)
        imprimir_ficheiro(mensagem)

    

        
    


