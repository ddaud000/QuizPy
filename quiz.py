import time
import random
#variaveis Leia as afirmações a seguir e assinale a resposta errada:", "a)A Floresta Amazônica atua como pulmão do mundo, sendo responsável pela produção de grande parte do oxigênio do mundo.","b)O desmatamento da Floresta Amazônia pode levar à desertificação de áreas localizadas ao sudeste do Brasil.", "c)O Rio Amazonas é o segundo maior rio do mundo, perdendo somente para o Rio Nilo.", "d)A Floresta Amazônica se estende por oito países da América do Sul.", "e)","A",2, "A", ") ","O",", e","P")
continuar = False
#                                                                                                                                                                                                         6    7     8       9        10      11     12
pergunta_1 = ("Quais das alternativas a baixo refere-se as mudanças climáticas?", "a)Aquecimento global", "b)Aumento da temperatura", "c)Ondas de calor", "d)Chuvas intensas", "e)Todas as alternativas","E", 1, "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ", "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ", "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ", "O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ","O termo mudança climático é mais amplo do que aquecimento global, que se refere apenas ao aumento da temperatura. O que se chama de mudanças climáticas inclui temperatura, intensidade das chuvas e eventos climáticos extremos, como furacões e ondas de calor. ")
pergunta_2 = ("Quais são os três maiores países emissores de gases do efeito estufa?", "a)Índia, Rússia e EUA", "b)EUA, Indonésia e Rússia", "c)Brasil, EUA e Canadá", "d)China, EUA e Índia", "e)Rússia, México e Brasil","D", 2, "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.", "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.", "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.", "Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.","Os países que emitem mais gases de efeito estufa são, de longe, a China e os EUA. Juntos, eles são responsáveis por mais de 40 porcento do total global de emissões.")
pergunta_3 =("O que é pegada de carbono?", "a)É um projeto que tem por objetivo diminuir a emissão de carbono nas fabricas","b)É um termo utilizado para fabricas pararem de emitir tanto gás carbônico na produção","c)É quantidade de carbono que alguém ou uma organização emite em um período determinado.","d)Termo utilizado quando ocorre uma transição de gás carbônico em grande quantidade","e)É um jogo infantil criado para ensinar sobre os efeitos do gás carbônico em grande quantidade no ambiente","C", 3, "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ", "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ", "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ", "A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ","A pegada de carbono trata-se da quantidade de carbono emitida por um indivíduo ou uma organização por um período determinado, ou emitida durante o processo de fabricação de um produto. ")
pergunta_4 =("Quais são os setores que mais usam combustíveis fosseis?","a)Elétrico e de transporte", "b)De transporte e indústrial", "c)Residencial e Elétrico", "d)Elétrico e Residencial", "e)Residencial e de transporte", "A", 2, "justA", "justB", "justC", "jusD","jusE")
pergunta_5 = ("Qual é uma consequências do desmatamento na Amazônia?", "a)A diminuição do oxigênio na atmosfera, podendo causar asfixia","b)O desaparecimento dos rios voadores, o que causa secas no Sudeste e no Sul", "c)A diminuição da população de tigres e raposas", "d)Aumento do preço do pedágio na Transamazônica", "e)Aumento do risco de Extinção das Coníferas","B",2, "justA", "justB", "justC", "jusD","jusE")
pergunta_6 = ("Leia as afirmações a seguir e assinale a resposta errada:", "a)A Floresta Amazônica atua como pulmão do mundo, sendo responsável pela produção de grande parte do oxigênio do mundo.","b)O desmatamento da Floresta Amazônia pode levar à desertificação de áreas localizadas ao sudeste do Brasil.", "c)O Rio Amazonas é o segundo maior rio do mundo, perdendo somente para o Rio Nilo.", "d) A Floresta Amazônica se estende por oito países da América do Sul.", "e) A maior espécie de cobra do mundo se encontra na Amazônica","A", 2, "A questão está errada devido ao fato de grande parte do oxigênio produzido pela Floresta Amazônia ser produzido por ela mesma. Os grandes responsáveis pela produção de oxigênio do mundo são as algas marinhas e cianobactérias.", "O desmatamento exacerbado da floresta influencia nos seus processos de evapotranspiração, afetando o transporte de umidade (impulsionado pelos ventos provenientes das Cordilheiras dos Andes) ao sudeste, levando ao declínio no volume das chuvas.","O Rio Nilo mede 6650 quilômetros, enquanto o Rio Amazonas mede 6400 quilômetros.","Com uma área total de mais de 6,7 milhões de metros quadrados, a floresta se estende pela Bolívia, Brasil, Colômbia, Equador, Guiana, Peru e Venezuela. Se fosse considerada um país, ela se encontraria no top 10 de maiores países do mundo.","Podendo pesar até 250 quilos e chegando a quase 5 metros de comprimento, a Sucuri verde (Eunectes murinus) apresenta a maior proporção peso x comprimento do mundo.")
pergunta_7 = ("Em 2 de agosto de 2010, foi promulgada a Lei n°12305 da PNRS (Política Nacional de Resíduos Sólidos, apresentando os processos que devem ser realizados no gerenciamento de resíduos sólidos. Assinale qual alternativa apresenta as opções e ordem corretas:", "a) Reduzir, reusar e reciclar","b) Não geração, Reciclagem, reutilização, filtração, tratamento dos resíduos e disposição final.", "c) Não geração, redução, reutilização, reciclagem, tratamento dos resíduos e disposição final ambientalmente adequada.", "d) Redução, reciclagem e tratamento dos resíduos.", "e) Não geração, redução, reutilização, reciclagem, filtração, tratamento dos resíduos e disposição final ambientalmente adequada.","C",3, "Apesar de “Reduzir, reusar e reciclar” ser uma frase comumente difundida entre textos didáticos, ela está incompleta em relação aos processos descritos na PNRS", "“Filtração” não é um processo descrito na PNRS, além do número de processos e ordem estarem ambos incorretos.", "A alternativa apresenta devidamente os processos em quantidade e ordem corretas.", "A ordem dos processos apresentados está correta, mas há três processos descritos pela PNRS que não estão presentes na alternativa.", "Apesar da ordem estar correta, “filtração” não é um processo descrito pela PNRS.")
pergunta_8 = ("pergunta", "a)","b)", "c)", "d)", "e)","Alternativa correta",2, "justA", "justB", "justC", "justD", "justE")
pergunta_9 = ("pergunta", "a)","b)", "c)", "d)", "e)","Alternativa correta",2, "justA", "justB", "justC", "justD", "justE")
pergunta_10 = ("pergunta", "a)","b)", "c)", "d)", "e)","Alternativa correta",2, "justA", "justB", "justC", "justD", "justE")
perguntas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5, pergunta_6, pergunta_7, pergunta_8, pergunta_9 , pergunta_10]
pontuacao_max = 0
for i in perguntas:
    pontuacao_max += i[7]

#funcoes
def linha():
    print("_"*40)

def inicio():
    print('Quiz ...\Quiz feito por ... ... ... ...')
    linha()
    continuar = input("\nDeseja iniciar o Quiz? [S/N]: ")
    linha()
    if continuar == 'S' or continuar == 's':
        status = True
    else:
        status = False
    return status
    

def info(pont, numero): 
    if pont==1: 
        nivel = "Facil" 
    elif pont ==2:
        nivel="Médio"
    else:
        nivel="Dificil"
    print("\nPergunta: %d Nivel: %s" %(numero,nivel))


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

def justificativa(pergunta, resposta_usuario):
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

def tentar_novamente():
    x = input("Você deseja tentar novamente?[S/N] ").upper()
    if x =="S": 
        continuar = True
    else: 
        continuar = False
    return continuar

#inicio
continuar = inicio()

#programa principal
while continuar == True:
    acertos =[] #essas variaveis tem que ficar aqui para serem zeradas caso o usuário queira tentar novamente. 
    erros=[]
    pontuacao_final = 0
    random.shuffle(perguntas)
    for i in range(len(perguntas)): 
        pontos, acertos, erros = questao(perguntas[i], i+1, acertos, erros)
        pontuacao_final = pontuacao_final+pontos
        time.sleep(2)
        linha()
        time.sleep(1)
    
    print("Você acertou as questões:")
    print(*acertos, sep = ", ")
    time.sleep(1)
    print("Você errou as questões:")
    print(*erros, sep = ", ")
    time.sleep(1)
    print("\nSua pontuação final foi: %d/%d" %(pontuacao_final,pontuacao_max))

    continuar = tentar_novamente()
