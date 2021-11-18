import time
import random

#dados perguntas
pergunta_1 = ("Quais das alternativas a baixo refere-se as mudanças climáticas?", 
              "a) Aquecimento global", 
              "b) Aumento da temperatura", 
              "c) Ondas de calor", 
              "d) Chuvas intensas", 
              "e) Todas as alternativas",
              "E", 1, 
              "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ", 
              "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ", 
              "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ", 
              "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ",
              "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ")

pergunta_2 = ("Quais são os três maiores países emissores de gases do efeito estufa?", 
              "a) Índia, Rússia e EUA", 
              "b) EUA, Indonésia e Rússia", 
              "c) Brasil, EUA e Canadá", 
              "d) China, EUA e Índia", 
              "e) Rússia, México e Brasil",
              "D", 2, 
              "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.", 
              "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.", 
              "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.", 
              "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.",
              "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.")

pergunta_3 = ("O que é pegada de carbono?", 
              "a) É um projeto que tem por objetivo diminuir a emissão de carbono nas fabricas",
              "b) É um termo utilizado para fabricas pararem de emitir tanto gás carbônico na produção",
              "c) É quantidade de carbono que alguém ou uma organização emite em um período determinado.",
              "d) Termo utilizado quando ocorre uma transição de gás carbônico em grande quantidade",
              "e) É um jogo infantil criado para ensinar sobre os efeitos do gás carbônico em grande quantidade no ambiente",
              "C", 3, 
              "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ", 
              "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ", 
              "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ", 
              "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ",
              "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ")

pergunta_4 = ("Quais são os setores que mais usam combustíveis fosseis?",
              "a) Elétrico e de transporte", 
              "b) De transporte e indústrial", 
              "c) Residencial e Elétrico", 
              "d) Indústria e Residencial", 
              "e) Residencial e de transporte", 
              "A", 2, 
              "Os setores elétricos e de transporte são os que mais se utilizam de combustíveis fósseis, juntos sendo responsáveis por quase dois terços (aproximadamente 63%) do uso de combustíveis fósseis", 
              "O setor de transporte é o setor que mais utiliza combustíveis fósseis (aproximadamente 31,5%), mas o setor de indústrias (aproximadamente 27,15%) perde para o setor de energia.", 
              "O setor elétrico é o segundo setor que mais utiliza combustíveis fósseis (aproximadamente 28%), porém o setor residencial é o setor entre os citados que menos utiliza o recurso (aproximadamente 7,8%).", 
              "Ambos os setores industrial (aproximadamente 27,15%) e residencial (aproximadamente 7,8%) não são os dois maiores que utilizam combustíveis fósseis, com os setores de transporte (aproximadamente 31,5%) e energia (aproximadamente 28%) em primeiro e segundo lugar.",
              "Porém o setor de transporte é o que mais utliza combustíveis fósseis (aproximadamente 31,5%), o setor residencial é o que menos utiliza do recurso entre os listados (aproximadamente 7,8%).")

pergunta_5 = ("Qual é uma consequências do desmatamento na Amazônia?", 
              "a) A diminuição do oxigênio na atmosfera, podendo causar asfixia",
              "b) O desaparecimento dos rios voadores, o que causa secas no Sudeste e no Sul", 
              "c) A diminuição da população de tigres e raposas", 
              "d) Aumento do preço do pedágio na Transamazônica", 
              "e) Aumento do risco de Extinção das Coníferas",
              "B",2, 
              "Apesar da Amazônia produzir muito oxigênio, grande parte dele é consumido por ela mesma. As principais produtoras de oxigênio são as algas marinhas.", 
              "Os rios voadores consistem em massas de ar carregadas com água provenientes da evapotranspiração na Amazônia. Os ventos carregam estas massar em direção ao sudeste e sul do país, sendo responsáveis pelo aumento de até 60% da umidade nessas regiões. O desmatamento exarcebado atrapalha este processo, afetando gravemente o clima delas.", 
              "As únicas espécies similares a raposas no Brasil se encontram no Cerrado. Não há tigres na Amazônia.", 
              "O desmatamento não irá levar a um aumento no pedágio da Transamazônica, mas sua construção contribuiu para a aceleração do processo de degradação ambiental da floresta.",
              "As coníferas são comuns em climas frios, como no sul do Brasil e no hemisfério norte. Não existem árvores coníferas na Floresta Amazônica.")

pergunta_6 = ("Leia as afirmações a seguir e assinale a resposta errada:", 
              "a) A Floresta Amazônica atua como pulmão do mundo, sendo responsável pela produção de grande parte do oxigênio do mundo.",
              "b) O desmatamento da Floresta Amazônia pode levar à desertificação de áreas localizadas ao sudeste do Brasil.", 
              "c) O Rio Amazonas é o segundo maior rio do mundo, perdendo somente para o Rio Nilo.", 
              "d) A Floresta Amazônica se estende por oito países da América do Sul.", 
              "e) A maior espécie de cobra do mundo se encontra na Amazônica",
              "A", 2, 
              "A questão está errada devido ao fato de grande parte do oxigênio produzido pela Floresta Amazônia ser produzido por ela mesma. Os grandes responsáveis pela produção de oxigênio do mundo são as algas marinhas e cianobactérias.", 
              "O desmatamento exacerbado da floresta influencia nos seus processos de evapotranspiração, afetando o transporte de umidade (impulsionado pelos ventos provenientes das Cordilheiras dos Andes) ao sudeste, levando ao declínio no volume das chuvas.",
              "O Rio Nilo mede 6650 quilômetros, enquanto o Rio Amazonas mede 6400 quilômetros.",
              "Com uma área total de mais de 6,7 milhões de metros quadrados, a floresta se estende pela Bolívia, Brasil, Colômbia, Equador, Guiana, Peru e Venezuela. Se fosse considerada um país, ela se encontraria no top 10 de maiores países do mundo.",
              "Podendo pesar até 250 quilos e chegando a quase 5 metros de comprimento, a Sucuri verde (Eunectes murinus) apresenta a maior proporção peso x comprimento do mundo.")

pergunta_7 = ("Em 2 de agosto de 2010, foi promulgada a Lei n°12305 da PNRS (Política Nacional de Resíduos Sólidos, apresentando os processos que devem ser realizados no gerenciamento de resíduos sólidos. Assinale qual alternativa apresenta as opções e ordem corretas:", 
              "a) Reduzir, reusar e reciclar",
              "b) Não geração, Reciclagem, reutilização, filtração, tratamento dos resíduos e disposição final.", 
              "c) Não geração, redução, reutilização, reciclagem, tratamento dos resíduos e disposição final ambientalmente adequada.", 
              "d) Redução, reciclagem e tratamento dos resíduos.", 
              "e) Não geração, redução, reutilização, reciclagem, filtração, tratamento dos resíduos e disposição final ambientalmente adequada.",
              "C",3, 
              "Apesar de “Reduzir, reusar e reciclar” ser uma frase comumente difundida entre textos didáticos, ela está incompleta em relação aos processos descritos na PNRS", 
              "'Filtração' não é um processo descrito na PNRS, além do número de processos e ordem estarem ambos incorretos.", 
              "A alternativa apresenta devidamente os processos em quantidade e ordem corretas.", 
              "A ordem dos processos apresentados está correta, mas há três processos descritos pela PNRS que não estão presentes na alternativa.", 
              "Apesar da ordem estar correta, “filtração” não é um processo descrito pela PNRS.")

pergunta_8 = ("Quais dos listados abaixo não causa poluição atmosférica:", 
              "a) Monóxido de Carbono",
              "b) Dióxido de Enxofre", 
              "c) Chumbo", 
              "d) Dióxido de Nitrogênio", 
              "e) Hidrogênio",
              "E",2, 
              "O monóxido de carbono (CO) é encontrado na atmosfera quando ocorre uma combustão incompleta de combustíveis de carbono, com falta de oxigênio na formação do dióxido de carbono (CO2).", 
              "O dióxido de carbono (SO2) é emitido pelo uso de combustiveis fósseis (via usinas eletricas).",  
              "A emissão do chumbo (Pb) chega à atmosfera através do uso de combustivel.", 
              "O Dióxido de Nitrogênio (NO2) chega à atmosfera na queima de combustível.", 
              "O hidrogênio não causa poluição atmosférica.")

pergunta_9 = ("Nos últimos 200 anos, o nível de dióxido de carbono na atmosfera tem:",
              "a) Aumentado firmemente.",
              "b) Diminuido firmemente.",
              "c) Oscilado.",
              "d) Aumentado porém com um declínio nos últimos anos.",
              "e) Sem mudança.",
              "A", 1,
              "Atividades humanas, principalmente na queima de combustíveis, contribuiu nos ultimos anos no aumento do CO2 atmosférico, sem previsão de cessar as atividades.",
              "Atividades humanas, principalmente na queima de combustíveis, contribuiu nos ultimos anos no aumento do CO2 atmosférico, logo aumentando o nível de CO2.",
              "Atividades humanas, principalmente na queima de combustíveis, contribuiu nos ultimos anos no aumento do CO2 atmosférico, sem diminuição das atividades para que ocorra uma oscilação.",
              "Atividades humanas, principalmente na queima de combustíveis, contribuiu nos ultimos anos no aumento do CO2 atmosférico, sem diminuição das atividades para que o nível de CO2 diminua.", 
              "Atividades humanas, principalmente na queima de combustíveis, contribuiu nos ultimos anos no aumento do CO2 atmosférico, atividades que aumentaram o impacto com os anos.")

pergunta_10= ("Uma das maiores tragédias ocorridas no Brasil foi o rompimento da barragem do Fundão, ocorrida em Mariana em novembro de 2015, onde rejeitos da mineração correram pela cidade, causando muitas tragédias. Sobre o acontecimento, identifique a alternativa correta:",
              "a) Além de abalar a flora, deixando o solo infértil, os compostor encontrados no rejeito são extremamante tóxicos ao homem.",
              "b) Mesmo com a flora devastada, a cobertura de lama, ao secar, tem propriedades que a deixarão apropriada para a plantação na região", 
              "c) O rejeito foi responsável pela a alteração do pH do solo, além de ser infértil e logo impossibilitando o crescimento de plantas na região", 
              "d) A cobertura irá formar uma espécie de pavimentação ao secar, um processo que ocorre rapidamente após o rompimento.", 
              "e) Apenas o impacto do rejeito foi responsável pela destruição do ambiente, com o composto não apresentando nenhuma propriedade que evita a restauração da flora e fauna.",
              "C",3, 
              "Mesmo abalando a flora e deixando o solo infértil e inadaptável para as plantas locais, o rejeito não é tóxico ao ser humano.", 
              "Com um período de secamento longo do composto, sua rigidez e infertilidade deixa impossível a formação de e crescimento das plantas da região.", 
              "O solo foi também responsável pela desestruturação química do solo." 
              "A secagem do composto é extremamente lenta, com esse tempo de espera impossibilitando a construção de novas estruturas nos locais afetados", 
              "Além do impacto, o rejeito tem propriedades que desapropriam o solo para cultivo, plantação e sobrevivência da flora da região.")

#variaveis
continuar = False
perguntas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5, pergunta_6, pergunta_7, pergunta_8, pergunta_9 , pergunta_10]
pontuacao_max = 0
for i in perguntas:
    pontuacao_max += i[7]


#função linha
def linha():
    print("_"*40)

#função início
def inicio():
    linha()
    print('\nQuiz sobre o Meio Ambiente')
    linha()
    print("\nEsse quiz consiste de 10 perguntas apresentadas em ordem aleatória.")
    time.sleep(1)
    print("\n-Duas(2) perguntas são fáceis e valem 1 pontos cada.")
    time.sleep(1)
    print("\n-Cinco(5) perguntas são médias e valem 2 pontos cada.")
    time.sleep(1)
    print("\n-Três(3) perguntas são difíceis e valem 3 pontos cada.")
    time.sleep(1)
    print("\nA pontuação máxima é %d pontos."%(pontuacao_max))
    time.sleep(1)
    print("\nPontuacão  /  Desempenho")
    print("   ≤10    --> Regular")
    print("   ≥11    --> Bom")
    print("   ≥15    --> Ótimo")
    print("   =21    --> Perfeito")
    print("\nApós realizar o quiz, você terá a oportunidade de tentar novamente")
    comecar = input("\nDeseja iniciar o Quiz? [S/N]: ")
    linha()
    if comecar == 's' or comecar == "S":
        status = True
    else:
        print("Volte quando quiser começar")
        status = False
    return status
    
#função info 
def info(pont, numero): 
    if pont==1: 
        nivel = "Facil" 
    elif pont ==2:
        nivel="Médio"
    else:
        nivel="Dificil"
    print("\nPergunta: %d Nivel: %s" %(numero,nivel))

#função questao
def questao(pergunta, numero, acertos, erros):
    info(pergunta[7], numero)
    print("\n",pergunta[0],"\n", pergunta[1],"\n",pergunta[2],"\n", pergunta[3],"\n", pergunta[4],"\n", pergunta[5], "\n")
    linha()
    resposta_usuario = str(input("\nDigite a sua resposta: ")).upper() 
    if resposta_usuario == pergunta[6]: 
        print("Parabéns, você acertou")
        print("Justificativa: ",justificativa(pergunta, resposta_usuario))
        pontuacao = pergunta[7] 
        acertos.append(numero)
    else:
        print("Você errou, a resposta correta era", pergunta[6])
        print("Justificativa: ",justificativa(pergunta, resposta_usuario))
        pontuacao = 0
        erros.append(numero)

    return pontuacao, acertos, erros

#funcao justificativa
def justificativa(pergunta, resposta_usuario):
    time.sleep(1)
    if resposta_usuario == "A":
        return pergunta[8]
    elif resposta_usuario == "B":
        return pergunta[9]
    elif resposta_usuario == "C":
        return pergunta[10]
    elif resposta_usuario == "D":
        return pergunta[11]
    elif resposta_usuario == "E":
        return pergunta[12]

#funcao tentar_novamente
def tentar_novamente():
    x = input("Você deseja tentar novamente?[S/N] ").upper()
    if x =="S": 
        continuar = True
    else: 
        continuar = False
    return continuar

#funcao desempenho
def desempenho(pontuacao_final):
    if pontuacao_final <= 10:
        print('Seu desempenho foi regular.')
    elif pontuacao_final >= 11 and pontuacao_final <= 15:
        print('Seu desempenho foi bom.')
    elif pontuacao_final >= 16 and pontuacao_final <= 20:
        print('Seu desempenho foi ótimo!')
    elif pontuacao_final == 21:
        print('Seu desempenho foi perfeito!')


#inicio
continuar = inicio()

#programa principal
while continuar == True:
    #variáveis que mudam com o loop
    acertos =[] 
    erros=[]
    pontuacao_final = 0
    #muda a ordem das perguntas
    random.shuffle(perguntas)
    #faz cada perguntas
    for i in range(len(perguntas)): 
        pontos, acertos, erros = questao(perguntas[i], i+1, acertos, erros)
        pontuacao_final = pontuacao_final+pontos
        time.sleep(2)
        linha()
        time.sleep(1)
    
    #dados no final do jogo
    print("Você acertou as questões:")
    print(*acertos, sep = ", ")
    time.sleep(1)
    print("Você errou as questões:")
    print(*erros, sep = ", ")
    time.sleep(1)
    puntuacao_de_dez =  (pontuacao_final*10)/21
    print("\nSua pontuação final foi:\n%d/%d ou %d/10" %(pontuacao_final,pontuacao_max, puntuacao_de_dez))
    desempenho(pontuacao_final)

    #pergunta se o usuário deseja tentar novamente
    linha()
    continuar = tentar_novamente()