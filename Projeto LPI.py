ListaNome = []
ListaTele = []
ListaMorada = []
Listacc = []
ListaData = []
ListaLVL = []
ListaLimit = []
EmptyList = []
i = len(ListaNome) + 1
OPT = 100
ListaTreinos = []
itreino = len(ListaTreinos) + 1
ListaPresencas = []


def ListaS(TestListx, ListaxS):
    for y, xN in enumerate(TestListx):
        x = (xN[4:])
        ListaxS = ListaxS + [x]
    return ListaxS


def Ordenar(Lista):
    ListaVazia = []
    for Element, Name in enumerate(ListaS(Lista, ListaVazia)):
        NName = ('{} - {}'.format(Element + 1, Name))
        ListaVazia = ListaVazia + [NName]
    Lista = ListaVazia
    return Lista

def OrdenarG(Lista):
    ListaVazia = []
    for Element, Name in enumerate(ListaS(Lista, ListaVazia)):
        NName = ('({}-)  {}'.format(Element + 1, DataTreino))
        ListaVazia = ListaVazia + [NName]
    Lista = ListaVazia
    return Lista


ListaS(ListaNome, EmptyList)
ListaS(ListaTele, EmptyList)
ListaS(ListaMorada, EmptyList)
ListaS(Listacc, EmptyList)
ListaS(ListaData, EmptyList)
ListaS(ListaLVL, EmptyList)
ListaS(ListaLimit, EmptyList)
while OPT != 0:  # Starting Menu
    print('---------MENU PRINCIPAL---------')
    print('')
    print('Desportista: ')
    print('1 - Introduzir novo')
    print('2 - Alterar dados pessoais')
    print('3 - Remover')
    print('')
    print('Presenças em Treino: ')
    print('4 - Registar Treino e Presenças')
    print('5 - Remover Treino')
    print('')
    print('Gravação: ')
    print('6 - Gravar dados')
    print('7 - Carregar dados')
    print('')
    print('8 - Consultas')
    print('')
    print('0 - Sair')
    print('')
    OPT = int(input('Escolha uma opção: '))
    if OPT == 1 or OPT == "1":
        print('--------------ADICIONAR UM DESPORTISTA--------------')
        print('')
        InputString = str(input('Nome do Desportista a Adicionar: '))


        def ADDSTR(InputString, Lista):
            InputString = ('{} - {}'.format(i, InputString))
            Lista = Lista + [InputString]
            return Lista


        ListaNome = ADDSTR(InputString, ListaNome)  # Nome da Lista Numerada com todos os Nomes: ListaNome
        # print(ListaNome)

        InputTele = str(input('Nº telefone (9 dígitos): '))
        telefoneL = ('{} - {}'.format(i, InputTele))
        telefoneint = int(InputTele)
        while True:
            if 100000000 <= telefoneint <= 999999999:
                ListaTele = ListaTele + [
                    telefoneL]  # Nome da Lista Numerada com todos os Numeros de Telefone: ListaTele
                # print(ListaTele)
                break
            else:
                print('Erro - telemovel invalido')

        InputString = str(input('Morada: '))
        ListaMorada = ADDSTR(InputString, ListaMorada)  # Nome da Lista Numerada com todas as Moradas: ListaMorada
        # print(ListaMorada)

        Inputcc = str(input('Nº Cartão do Cidadão (8 dígitos): '))
        ccL = ('{} - {}'.format(i, Inputcc))
        ccint = int(Inputcc)
        while True:
            if 10000000 <= ccint <= 99999999:
                Listacc = Listacc + [ccL]  # Nome da Lista Numerada com todos as CCs: Listacc
                # print(Listacc)
                break
            else:
                print('Erro - Nº Cartão do Cidadão invalido')

        print('Data de nascimento: ')
        while True:
            dd = int(input('Dia: '))
            mm = int(input('Mes: '))
            aaaa = int(input('Ano: '))
            if 1 <= dd <= 31 and 1 <= mm <= 12 and 1900 <= aaaa <= 2100:
                if 1 <= dd < 10:
                    dd = str(dd)
                    dd = "0" + dd
                if 1 <= mm < 10:
                    mm = str(mm)
                    mm = "0" + mm
                DataN = ('{}-{}-{}'.format(dd, mm, aaaa))
                DataL = ('{} - {}'.format(i, DataN))
                ListaData = ListaData + [DataL]  # Nome da Lista Numerada com todos as Datas de Nascimento: ListaData
                # print(ListaData)
                break
            else:
                print('Erro - Data de nascimento invalida')

        LVLN = str(input('Nível (Baixo, Mediano, Alto): '))
        baixo = ['Iniciante', 'iniciante', 'baixo', 'Baixo', 'basico', 'elementar', 'Basico', 'Elementar', '1']
        medio = ['Mediano', 'mediano', 'Intermedio', 'intermedio', 'Intermédio', 'intermédio', 'Medio', 'medio', '2']
        alto = ['Avançado', 'avancado', 'Avancado', 'avançado', 'Alto', 'alto', 'Elevado', 'elevado', '3']
        while LVLN not in baixo and LVLN not in medio and LVLN not in alto:
            LVLN = str(input('Nível: '))
            if LVLN in baixo:
                print('Baixo')
            if LVLN in medio:
                print('Medio')
            if LVLN in alto:
                print('Alto')
            if LVLN not in baixo and LVLN not in medio and LVLN not in alto:
                print('Erro - Nivel Invalido')
        LVLL = ('{} - {}'.format(i, LVLN))
        ListaLVL = ListaLVL + [LVLL]
        # print(ListaLVL)

        InputString = str(input('Limitações: '))
        ListaLimit = ADDSTR(InputString, ListaLimit)  # Nome da Lista Numerada com todas as limitacoes: ListaLimit
        # print(ListaNome)
        print('------------------------------------')
        print('')
        print('Desportista adicionado com sucesso !')
        print('')
        continuar = input('Deseja fazer mais alguma operação ? (s/n) : ')
        if continuar == 'n' or continuar == 'N':
            OPT = 0
        else:
            OPT = 100
    if OPT == 2:
        ALT = 100
        while ALT != 0:
            print('---------ALTERAR DADOS---------')
            print('')
            print('1 - Nome')
            print('2 - Nº telefone')
            print('3 - Morada')
            print('4 - Cartão do Cidadão')
            print('5 - Data de nascimento')
            print('6 - Nível')
            print('7 - Limitações')
            print('')
            print('0 - Voltar')
            print('')
            ALT = int(input('Escolha uma opção para alterar: '))
            if ALT == 1:
                print('Lista de Nomes do Sistema: ', ListaNome)
                print('Lista de CCs do Sistema: ', Listacc)
                ind = int(input('Numero da referencia do individuo a alterar os dados: '))
                print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
                print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
                NewNome = input('Novo nome: ')
                ListaNome[ind - 1] = ('{} - {}'.format(ind, NewNome))
                print(ListaNome)
                input('Digite qualquer valor para continuar . . . ')
                ALT = 0
            if ALT == 2:  # ALT Telefone
                print('Lista de Nomes do Sistema: ', ListaNome)
                print('Lista de CCs do Sistema: ', Listacc)
                print('Lista de Nº telefone do Sistema: ', ListaTele)
                ind = int(input('Numero da referencia do individuo a alterar os dados: '))
                print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
                print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
                print('Telefone: ', ListaS(ListaTele, EmptyList)[ind - 1])
                NewTele = int(input('Novo telefone (9 dígitos): '))
                if 100000000 <= NewTele <= 999999999:
                    ListaTele[ind - 1] = ('{} - {}'.format(ind, NewTele))
                else:
                    print('Erro - telemovel invalido')
                print(ListaTele)
                input('Digite qualquer valor para continuar . . . ')
                ALT = 0

            if ALT == 3:
                print('Lista de Nomes do Sistema: ', ListaNome)
                print('Lista de CCs do Sistema: ', Listacc)
                print('Lista de Moradas do Sistema: ', ListaMorada)
                ind = int(input('Numero da referencia do individuo a alterar os dados: '))
                print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
                print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
                print('Morada: ', ListaS(ListaMorada, EmptyList)[ind - 1])
                NewMorada = input('Nova Morada: ')
                ListaMorada[ind - 1] = ('{} - {}'.format(ind, NewMorada))
                print(ListaMorada)
                input('Digite qualquer valor para continuar . . . ')
                ALT = 0
            if ALT == 4:
                print('Lista de Nomes do Sistema: ', ListaNome)
                print('Lista de CCs do Sistema: ', Listacc)
                ind = int(input('Numero da referencia do individuo a alterar os dados: '))
                print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
                print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
                Newcc = int(input('Novo Cartão do Cidadão (8 dígitos): '))
                if 10000000 <= Newcc <= 99999999:
                    Listacc[ind - 1] = ('{} - {}'.format(ind, Newcc))
                else:
                    print('Erro - Cartão do Cidadão invalido')
                print(Listacc)
                input('Digite qualquer valor para continuar . . . ')
                ALT = 0
            if ALT == 5:
                print('Lista de Nomes do Sistema: ', ListaNome)
                print('Lista de CCs do Sistema: ', Listacc)
                print('Lista de Datas de Nascimento do Sistema: ', ListaData)
                ind = int(input('Numero da referencia do individuo a alterar os dados: '))  # Index Para a lista
                print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
                print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
                print('Data de Nascimento: ', ListaS(ListaData, EmptyList)[ind - 1])
                print('')
                print('Digite a Nova Data: ')
                dd = int(input('Dia: '))
                mm = int(input('Mes: '))
                aaaa = int(input('Ano: '))
                if 1 <= dd <= 31 and 1 <= mm <= 12 and 1900 <= aaaa <= 2100:
                    if 1 <= dd < 10:
                        dd = str(dd)
                        dd = "0" + dd
                    if 1 <= mm < 10:
                        mm = str(mm)
                        mm = "0" + mm
                NewData = ('{}-{}-{}'.format(dd, mm, aaaa))
                ListaData[ind - 1] = ('{} - {}'.format(ind, NewData))
                print(ListaData)
                input('Digite qualquer valor para continuar . . . ')
                ALT = 0
            if ALT == 6:
                print('Lista de Nomes do Sistema: ', ListaNome)
                print('Lista de CCs do Sistema: ', Listacc)
                print('Lista Niveis do Sistema: ', ListaLVL)
                ind = int(input('Numero da referencia do individuo a alterar os dados: '))  # Index Para a lista
                print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
                print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
                print('Nivel: ', ListaS(ListaLVL, EmptyList)[ind - 1])
                NewLVL = str(input('Novo Nivel: '))
                baixo = ['Iniciante', 'iniciante', 'baixo', 'Baixo', 'basico', 'elementar', 'Basico', 'Elementar', '1']
                medio = ['Mediano', 'mediano', 'Intermedio', 'intermedio', 'Intermédio', 'intermédio', 'Medio', 'medio',
                         '2']
                alto = ['Avançado', 'avancado', 'Avancado', 'avançado', 'Alto', 'alto', 'Elevado', 'elevado', '3']
                while NewLVL not in baixo and NewLVL not in medio and NewLVL not in alto:
                    NewLVL = str(input('Nível: '))
                    if NewLVL in baixo:
                        print('Baixo')
                    if NewLVL in medio:
                        print('Medio')
                    if NewLVL in alto:
                        print('Alto')
                    if NewLVL not in baixo and NewLVL not in medio and NewLVL not in alto:
                        print('Erro - Nivel Invalido')
                ListaLVL[ind - 1] = ('{} - {}'.format(ind, NewLVL))
                print(ListaLVL)
                input('Digite qualquer valor para continuar . . . ')
                ALT = 0
            if ALT == 7:
                print('Lista de Nomes do Sistema: ', ListaNome)
                print('Lista de CCs do Sistema: ', Listacc)
                print('Lista Limitações do Sistema: ', ListaLimit)
                ind = int(input('Numero da referencia do individuo a alterar os dados: '))  # Index Para a lista
                print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
                print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
                print('Limitacoes: ', ListaS(ListaLimit, EmptyList)[ind - 1])
                NewLimit = str(input('Novo Limite: '))
                ListaLimit[ind - 1] = ('{} - {}'.format(ind, NewLimit))
                print(ListaLimit)
                input('Digite qualquer valor para continuar . . . ')
                ALT = 0
            else:
                ALT = 0
            continuar = input('Deseja fazer mais alguma operação ? (s/n) : ')
            if continuar == 'n' or continuar == 'N':
                OPT = 0
            else:
                OPT = 100

    if OPT == 3:
        print('--------REMOVER DESPORTISTA--------')
        print('')
        print('Lista de Nomes do Sistema: ', ListaNome)
        print('Lista de CCs do Sistema: ', Listacc)
        print('')
        ind = int(input('Numero da Referencia do Individuo Remover: '))  # Index Para a lista
        print('')
        print('Nome: ', ListaS(ListaNome, EmptyList)[ind - 1])
        print('CC: ', ListaS(Listacc, EmptyList)[ind - 1])
        Confirm = input('Tem a certeza que deseja remover este Desportista ? (s/n): ')
        if Confirm == 's' or Confirm == "S":
            del ListaNome[ind - 1]
            del ListaTele[ind - 1]
            del ListaMorada[ind - 1]
            del Listacc[ind - 1]
            del ListaData[ind - 1]
            del ListaLVL[ind - 1]
            del ListaLimit[ind - 1]
            print('Desportista Removido com Sucesso! ')
        else:
            print('Operação cancelada. . .')

        Ordenar(ListaNome)
        Ordenar(ListaTele)
        Ordenar(ListaMorada)
        Ordenar(Listacc)
        Ordenar(ListaData)
        Ordenar(ListaLVL)
        Ordenar(ListaLimit)

        continuar = input('Deseja fazer mais alguma operação ? (s/n) : ')
        if continuar == 'n' or continuar == 'N':
            OPT = 0
        else:
            OPT = 100
    if OPT == 4:
        RES = 100
        while RES != 0:
            print('---------MENU DE TREINOS---------')
            print('')
            print('1 - Novo Treino')
            print('')
            print('2 - Marcar Presencas')
            print('')
            print('0 - Voltar')
            print('')
            RES = int(input('Escolha uma opção: '))
            print('==================================')
            if RES == 1:
                print("Insira as seguintes informacões sobre o novo Treino: ")
                print('Data do Treino (Cuidado para nao criar treinos repetidos!): ')
                while True:

                    dd = int(input('Dia: '))
                    mm = int(input('Mes: '))
                    aaaa = int(input('Ano: '))
                    hora = int(input('Hora (24): '))
                    minuto = int(input('Minutos: '))
                    if 1 <= dd <= 31 and 1 <= mm <= 12 and 2021 <= aaaa <= 2100 and 00 <= hora <= 24 and 00 <= minuto <= 60:
                        if 1 <= dd < 10:
                            dd = str(dd)
                            dd = "0" + dd
                        if 1 <= mm < 10:
                            mm = str(mm)
                            mm = "0" + mm
                        if 0 <= hora < 10:
                            hora = str(hora)
                            hora = "0" + hora
                        if 0 <= minuto < 10:
                            hora = str(hora)
                            hora = "0" + hora
                        DataTreino = ('({}-)  {}-{}-{} || {}:{}'.format(itreino, dd, mm, aaaa, hora, minuto))
                        DataTDMA = ('{}-{}-{} || {}:{}'.format(dd, mm, aaaa, hora, minuto))
                        ListaTreinos = ListaTreinos + [DataTreino]
                        print('')
                        print('Treino Criado com Sucesso !')
                        print('')
                        continuar = input('Deseja fazer mais alguma operação ? (s/n) : ')
                        if continuar == 'S' or continuar == 's':
                            break
                        if continuar == 'n' or continuar == 'N':
                            RES = 0
                            break
                        else:
                            RES = 100
                    else:
                        print('Erro - Data/Hora do Treino invalida')
                    print()
            if RES == 2:
                print("Insira a Data e o Horario do Treino a Marcar Presencas: ")
                print('Data do Treino: ')
                while True:

                    dd = int(input('Dia: '))
                    mm = int(input('Mes: '))
                    aaaa = int(input('Ano: '))
                    hora = int(input('Hora (24): '))
                    minuto = int(input('Minutos: '))
                    if 1 <= dd <= 31 and 1 <= mm <= 12 and 2021 <= aaaa <= 2100 and 00 <= hora <= 24 and 00 <= minuto <= 60:
                        if 1 <= dd < 10:
                            dd = str(dd)
                            dd = "0" + dd
                        if 1 <= mm < 10:
                            mm = str(mm)
                            mm = "0" + mm
                        if 0 <= hora < 10:
                            hora = str(hora)
                            hora = "0" + hora
                        if 0 <= minuto < 10:
                            hora = str(hora)
                            hora = "0" + hora
                        DataTreino = ('({}-)  {}-{}-{} || {}:{}'.format(itreino, dd, mm, aaaa, hora, minuto))
                        break
                    else:
                        print('Erro - Data/Hora do Treino invalida')

                if DataTreino in ListaTreinos:  # Se o Treino Existe
                    Continuar = 9999999
                    continuar = str(Continuar)
                    INDL = []
                    for y, Nome in enumerate(ListaNome):
                        print(ListaNome[y])
                        ListaNome[y] = Nome
                        IND = Nome[0]
                        INDL = INDL + [IND]
                    while Continuar != 0:
                        Continuar = eval(
                            input('Referencia do Desportista que esteve presente no treino (0 para parar): '))
                        continuar = str(Continuar)
                        if continuar in INDL:
                            ListaPresencas[Continuar] = ('{}'.format(ListaPresencas[Continuar] + 1 ))
    if OPT == 5:
        print('OPT 5')

print('Programa Terminado.')
