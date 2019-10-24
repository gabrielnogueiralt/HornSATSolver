#Abrindo cada uma das entradas.
entrada = open('entradas/Entrada.in')
entrada2 = open('entradas/Entrada2.in')
fnc = open('entradas/!FNC.in')
horn = open('entradas/!Horn.in')
sat = open('entradas/SAT.in')


def main(entrada):
    #Gerando o arquivo de saída.
    f = open("saida.out","w+")
    #Lendo o tamanho da entrada.
    n = entrada.readline()
    for i in range(1, int(n)+1):
        #Lendo cada linha da entrada, pegando as expressões.
        expressao = entrada.readline()
        print("Problema #", i)
        f.write("Problema #{}\n".format(i))
        if(isFnc(expressao)):
            if(isHorn(expressao)):
                literais = arrayLiterais(expressao)
                if(isUnitario(expressao)):
                    print("Sim, é satisfatível.\n")
                    f.write("Sim, é satisfatível.\n\n")
                elif(isSAT(expressao, literais)):
                    print("Sim, é satisfatível.\n")
                    f.write("Sim, é satisfatível.\n\n")
                else:
                    print("Não, não é satisfatível.\n")
                    f.write("Não, não é satisfatível.\n\n")
            else:
                print("Nem todas as cláusulas são de Horn.\n")
                f.write("Nem todas as cláusulas são de Horn.\n\n")
        else:
            print("Não está na FNC.\n")
            f.write("Não está na FNC.\n\n")

    print("\n")
    f.write("\n\n")

#Método que verifica se a expressão está na FNC.
def isFnc(expressao):
    contador = 0
    for i in range(len(expressao)):
        if(expressao[i] == ">" or expressao[i] == "<"):
            return False
        if(expressao[i] == "("):
            contador += 1
            if(contador > 1):
                return False
        if(expressao[i] == ")"):
            contador = 0

    return True

#Método que verifica se expressão é de Horn.
def isHorn(expressao):
    contador = 0
    for i in range(len(expressao)):
        if (expressao[i] == "P" or expressao[i] == "Q" or expressao[i] == "R" or expressao[i] == "S"):
            if(expressao[i - 1] != "~"):
                contador += 1
                if(contador > 1):
                    return False
        elif(expressao[i] == "("):
            contador = 0

    return True

#Método que verifica se a expressão possui cláusulas unitárias.
def isUnitario(expressao):
    for i in range(len(expressao)):
        if ((expressao[i] == "(" and expressao[i + 2] == ")") or (expressao[i] == "(" and expressao[i + 3] == ")")):
            return False

#Método que cria array de literais, no caso 4 que são os possíveis literais do problema (P,Q,R,S).
def arrayLiterais(exp):
    literais = ["G", "G", "G", "G"]
    expressao = exp.replace(" ", "")
    clausulas = expressao.split("&")
    for i in range(len(clausulas)):
        if(len(clausulas[i]) == 3):
            for j in range(len(literais)):
                str = clausulas[i]
                if(literais[j] == str[1]):
                    break
                elif(literais[j] == "G"):
                    literais[j]
                    break
    return literais

#Método que verifica se a expressão é ou não satisfatível
def isSAT(exp, literais):
    #Remoção de espaços e quebra das cláusulas unidas por &, colocando em cada posição da
    #string "clausulas" uma cláusula da expressão.
    expressao = exp.replace(" ", "")
    clausulas = expressao.split("&")
    for i in range(4):
        if(literais[i] != "G"):
            for x in range(len(clausulas)):
                index = clausulas[x].index(literais[i])
                str = list(clausulas[x])
                #Verifica se cláusula possui um dos literais positivos, para poder remove-la
                if(str.__contains__(literais[i]) and str.index(index - 1) != "~"):
                    str = ""
                    clausulas[x] = str
                #Verifica se cláusula possui um dos literais negados, para poder reduzí-la
                elif(str.contains(literais[i]) and str[index - 1] == '~'):
                    remover = "~" + str[index]
                    str = str.replace(remover, "")
                    clausulas[x] = str
                    j = 0
                    #Verifica se há "v" fora de ordem para formatar de modo correto a cláusula
                    while(j < len(clausulas[x])):
                        if(str[j] == "v" and (str[j+1] != "~") and (str[j+1] != "P" and str[j+1] != "Q" and str[j+1] != "R" and str[j+1] != "S") or str[j-1] == "("):
                            aux = str
                            aux[j] = " "
                            if(aux[1] == "v"):
                                aux[1] = " "
                            str = ""
                            clausulas[x] = str
                            for k in range(len(aux)):
                                if(not(aux[k] == " ")):
                                    str += aux[k]
                                    clausulas[x] = str
                                else:
                                    j = 0
                        j += 1
                    #Verifica se há cláusula vazia
                    if(str[0] == "(" and str[1] == ")"):
                        return False
                    elif(str[0] == "(" and str[2] == ")"):
                        for j in range(4):
                            if(literais[j] == str[1]):
                                break
                            elif(literais[j] == "G"):
                                literais[j] = str[1]
                                break
                    x -=1

#Passe como parâmetro uma das opções por vez: entrada, entrada2, fnc, horn ou sat
main(entrada2)
#Fechando o processo de abertura dos arquivos de entrada
entrada.close()
entrada2.close()
fnc.close()
horn.close()
sat.close()