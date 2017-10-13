# -*-coding: utf-8 -*-

# Pack de Funções
def substituicao(arquivo,tamanho,posicao,objeto):
    file = open(arquivo, 'r')
    lista = []
    for k in range(tamanho):
        lista.append(file.readline()[0:-1])
    file.close()

    lista[posicao-1] = objeto

    file = open(arquivo, 'w')
    for k in lista:
        file.write(str(k) + '\n')
    file.close()

def busca(arquivo,posicao):
    file = open(arquivo, 'r')
    busc = 0
    for k in range(posicao):
        busc = file.readline()[0:-1]
    file.close()
    return busc

def t_str_list(string):
    a,b,c,d,e = string.split('/')
    a = int(a)
    c = float(c)
    d = float(d)
    e = float(e)
    lista = []
    for k in [a,b,c,d,e]:
       lista.append(k)
    return lista

def t_list_str(lista):
    string = ''
    for k in range(5):
        if (k==4):
            string = string + str(lista[k])
            return string
        string = string + str(lista[k]) + '/'

def t_str_list_cad(string):
    a, b, c, d,= string.split('-')
    lista = []
    for k in [int(a), b, c, d]:
        lista.append(k)
    return lista

def login_adm(Verdade,Falso):
    x = 'sim'
    while(x == 'sim'):
        login = raw_input('Login: ')
        senha = raw_input('Senha: ')
        if (login[0] == '1'):
            lista = t_str_list_cad(busca('c:\Angus System\cadastros1.sim',int(login[1:4])))
            if (senha == decodificador(lista[2])):
                print 'Login efetuado com sucesso!'
                print
                print 'Bem-vindo(a) %s!' %lista[1]
                return Verdade
            else:
                print 'Senha Inválida!'
                x = raw_input('Tentar Novamente? (sim/nao): ')
        else:
            print 'Você não tem direitos de administrador!'
            x = 'nao'
        print
    return Falso

def login_caixa(Falso):
    x = 'sim'
    while(x == 'sim'):
        print 'LOGIN DO OPERADOR DO CAIXA:'
        login = raw_input('Login: ')
        senha = raw_input('Senha: ')
        if (login[0] == '1'):
            lista = t_str_list_cad(busca('c:\Angus System\cadastros1.sim',int(login[1:4])))
            if (senha == decodificador(lista[2])):
                print 'Login efetuado com sucesso!'
                print
                print 'Bem-vindo(a) %s!' %lista[1]
                return lista[1]
            else:
                print 'Senha Inválida!'
                x = raw_input('Tentar Novamente? (sim/nao): ')
                print
        elif (login[0] == '2'):
            lista = t_str_list_cad(busca('c:\Angus System\cadastros2.sim',int(login[1:4])))
            if (senha == decodificador(lista[2])):
                print 'Login efetuado com sucesso!'
                print
                print 'Bem-vindo(a) %s!' %lista[1]
                return lista[1]
            else:
                print 'Senha Inválida!'
                x = raw_input('Tentar Novamente? (sim/nao): ')
                print
    return Falso

def codificador(senha):
    senha_cod = ''
    for k in range(len(senha)):
        if (senha[k] == '1'):
            senha_cod += '0001'
        elif (senha[k] == '2'):
            senha_cod += '0010'
        elif (senha[k] == '3'):
            senha_cod += '0011'
        elif (senha[k] == '4'):
            senha_cod += '0100'
        elif (senha[k] == '5'):
            senha_cod += '0101'
        elif (senha[k] == '6'):
            senha_cod += '0110'
        elif (senha[k] == '7'):
            senha_cod += '0111'
        elif (senha[k] == '8'):
            senha_cod += '1000'
        elif (senha[k] == '9'):
            senha_cod += '1001'
    return senha_cod

def decodificador(senha):
    digitos = len(senha)/4
    senha_dec = ''
    ini = 0
    fin = 4
    for k in range(digitos):
        if (senha[ini:fin] == '0001'):
            senha_dec += '1'
        elif (senha[ini:fin] == '0010'):
            senha_dec += '2'
        elif (senha[ini:fin] == '0011'):
            senha_dec += '3'
        elif (senha[ini:fin] == '0100'):
            senha_dec += '4'
        elif (senha[ini:fin] == '0101'):
            senha_dec += '5'
        elif (senha[ini:fin] == '0110'):
            senha_dec += '6'
        elif (senha[ini:fin] == '0111'):
            senha_dec += '7'
        elif (senha[ini:fin] == '1000'):
            senha_dec += '8'
        elif (senha[ini:fin] == '1001'):
            senha_dec += '9'
        ini += 4
        fin += 4
    return senha_dec

# Registro Inicial do Programa (Executa somente no primeiro acesso)
import os
if (not os.path.exists('C:\Angus System')):
    print 'SISTEMA INFORMATIZADO ANGUS v1.0'
    os.mkdir (R'c:\Angus System')
    os.mkdir(R'c:\Angus System\Notas Fiscais de Compra')
    os.mkdir(R'c:\Angus System\Registros de Vendas')

    estoque =  open ('c:\Angus System\estoque.sim','w')
    estoque.close()

    cadastros1 = open('c:\Angus System\cadastros1.sim', 'w')
    print
    print'1º Acesso: Cadastro de Administrador:'
    nome = raw_input('Digite o nome: ')
    print 'Login: 1001'
    senha = codificador(raw_input('Digite uma senha (somente numeros): '))
    print 'Cadastro realizado com sucesso!'
    print

    cadastros2 = open('c:\Angus System\cadastros2.sim', 'w')
    cadastros2.close()

    dados = open('c:\Angus System\dados.sim', 'w')
    print'1º Acesso: Preenchimento de dados iniciais'
    nome_empresa = raw_input('Informe o nome da empresa: ')
    cnpj = raw_input('Informe o CNPJ: ')
    data = raw_input('Informe a data de hoje (**/**/****): ')
    print

    dados.write(nome_empresa + '\n')
    dados.write(cnpj + '\n')
    dados.write('1001' + '\n') #Quantidade de Administradores
    dados.write('2000' + '\n') #Quantidade de Colaboradores
    dados.write('0' + '\n') #Quantidade de Produtos
    dados.write(data + '\n')
    dados.write('fechado' + '\n') #Situação do Caixa
    dados.write('' + '\n') #Operador
    dados.write('0' + '\n') #Valor
    dados.close()

    colaborador = '%i-%s-%s-%s' % (1001, nome, senha, data)
    cadastros1.write(colaborador + '\n')
    cadastros1.close()

#Data de Abertura
d,m,a = busca('c:\Angus System\dados.sim', 6).split('/')
d = int(d)
m = int(m)
a = int(a)
data_dia = '%i/%i/%i' %(d,m,a)
nome_arquivo = 'c:\Angus System\Registros de Vendas\%i-%i-%i.re' %(d,m,a)

#Login de Acesso ao Sistema e Arquivo de Registro
print 'BEM-VINDO AO SISTEMA INFORMATIZADO ANGUS -', data_dia
x = login_adm('sim','nao')

# Menu Principal do Programa
while (x != 'nao' and x != 10):
    print 'MENU:'
    if (busca('c:\Angus System\dados.sim', 7) == 'aberto'):
        print '1 - Caixa Aberto (%s)' %busca('c:\Angus System\dados.sim', 8)
    else:
        print '1 - Abrir Caixa'
    print '2 - Consultar Estoque'
    print '3 - Atualizar Informações'
    print '4 - Compra de Mercadorias'
    print '5 - Cadastrar Produto'
    print '6 - Configurações'
    print '7 - Encerrar Dia'
    print '0 - Sair'
    x = input('Informe a opção desejada: ')
    print

    # Realizar Venda
    if (x == 1):
        vendas = open(nome_arquivo, 'a')
        if (busca('c:\Angus System\dados.sim', 7) == 'fechado'):
            print 'ATIVAÇÃO DE CAIXA - LOGIN DE ADMINISTRADOR'
            x = login_adm(1,11)
            if (x == 1):
                x = login_caixa(11)
                substituicao('c:\Angus System\dados.sim', 9, 7, 'aberto')
                substituicao('c:\Angus System\dados.sim', 9, 8, x)
                vendas.write(x + ':')
        # Busca de arquivos em Dados
        nome_mercantil = busca('c:\Angus System\dados.sim', 1)
        cnpj = busca('c:\Angus System\dados.sim', 2)
        operador = busca('c:\Angus System\dados.sim', 8)
        total_de_vendas = float(busca('c:\Angus System\dados.sim', 9))

        print 'Operador Logado:', operador
        while (x != 11):
            print 'CAIXA DE VENDAS:'
            soma = 0
            contador = 0
            nota = []
            while (True):
                produto = []
                cod = input('Informe o código (0 - Menu): ')
                qtd = 1
                if (cod == 0):
                    print '0 - Quantidade / 1 - Fechar Nota / 2 - Sair do Caixa / 3 - Fechar Caixa'
                    opcao = input('Escolha a opção: ')
                    if (opcao == 0):
                        qtd = input('Quantidade: ')
                        cod = input('Informe o código: ')
                    elif (opcao == 1):
                        break
                    elif (opcao == 2):
                        break
                    elif (opcao == 3):
                        break
                lista = t_str_list(busca('c:\Angus System\estoque.sim', cod))
                lista[4] -= qtd
                # Atualização de estoque e contadores
                substituicao('c:\Angus System\estoque.sim', int(busca('c:\Angus System\dados.sim',5)),cod,t_list_str(lista))
                soma += lista[3] * qtd
                contador += 1
                # Alimentação da nota
                produto.append(str(contador) + ' ' + lista[1])
                produto.append(qtd)
                produto.append(lista[3])
                nota.append(produto)
            print
            if (opcao == 1):
                # Pagamento
                print 'Total: R$', soma
                print
                print 'Forma de pagamento:'
                print '1 - Dinheiro'
                print '2 - Cartão de Crédito'
                pag = input('Informe a opção desejada: ')
                if (pag == 1):
                    dinheiro = input('Valor recebido: R$ ')
                    troco = dinheiro - soma
                    pagamento = 'Dinheiro: R$ %.2f / Troco: R$ %.2f' % (dinheiro, troco)
                elif (pag == 2):
                    print '1 - Visa'
                    print '2 - Martercard'
                    cartao = input('Informe a opção desejada: ')
                    if (cartao == 1):
                        cartao = 'Visa'
                    elif (cartao == 2):
                        cartao = 'Mastercard'
                    pagamento = 'Pago com cartão de crédito %s' % cartao
                nota.append(pagamento)

                # Nota fiscal
                print
                print '---------------------------------------'
                print '       Cupom Fiscal'
                print nome_mercantil, '-', data_dia
                print 'CNPJ:', cnpj
                print 'Operador:', operador
                print
                for i in range(contador):
                    print nota[i][0], '-', nota[i][1], 'x R$', nota[i][2], '= R$', nota[i][1] * nota[i][2]
                print
                print 'Total: R$ %.2f' % soma
                print pagamento
                print 'Volte Sempre!'
                print '---------------------------------------'
                print
                # Atualização de Dados
                vendas.write('#' + str(nota))
                total_de_vendas += soma
            elif (opcao == 2):
                substituicao('c:\Angus System\dados.sim', 9, 9, total_de_vendas)
                print 'Caixa Desligado'
                print 'OBS: Operador não fechou o caixa!'
                print
                break
            elif (opcao == 3):
                print 'FECHAMENTO DE CAIXA - LOGIN DE ADMINISTRADOR'
                opcao = login_adm(1,3)
                if (opcao == 1):
                    substituicao('c:\Angus System\dados.sim', 9, 7, 'fechado')
                    substituicao('c:\Angus System\dados.sim', 9, 7, 'fechado')
                    substituicao('c:\Angus System\dados.sim', 9, 9, total_de_vendas)
                    vendas.write('\n')
                    print 'O CAIXA FOI ENCERRADO COM SUCESSO!'
                    print
                    break
        vendas.close()

    # Consultar Estoque
    elif (x == 2):
        while(True):
            print 'CONSULTA DE ESTOQUES'
            print '1 - Mostrar todos os produtos'
            print '2 - Mostrar produto pelo código'
            print '0 - Voltar'
            x = input('Informe a opção desejada: ')
            print
            if (x == 1):
                for k in range(int(busca('c:\Angus System\dados.sim',5))):
                    lista = t_str_list(busca('c:\Angus System\estoque.sim',k+1))
                    print '-------------------------------------'
                    print 'Código:', lista[0]
                    print 'Nome:', lista[1]
                    print 'Valor de Compra: R$ ', lista[2]
                    print 'Valor de Venda: R$ ', lista[3]
                    print 'Quantidade:', lista[4]
                    print
            elif (x == 2):
                while (True):
                    print 'Consulta de produto'
                    cod = input('Informe o código (0 - Voltar): ')
                    if (cod == 0):
                        print
                        break
                    lista = t_str_list(busca('c:\Angus System\estoque.sim',cod))
                    print 'Nome: ', lista[1]
                    print 'Valor de Compra: R$ ', lista[2]
                    print 'Valor de Venda: R$ ', lista[3]
                    print 'Quantidade: ', lista[4]
                    print
            elif (x == 0):
                break
            else:
                print 'Opção Inválida!'
                print

    # Atualizar Informações
    elif (x == 3):
        while(True):
            print 'ATUALIZAÇÃO DE DADOS'
            print '1 - Alterar valor de venda'
            print '2 - Alterar o estoque'
            print '3 - Alterar o cadastro'
            print '0 - Voltar'
            x = input('Informe a opção desejada: ')
            print
            if (x == 1): #valor de venda
                while (True):
                    cod = input('Informe o código (0 - Voltar): ')
                    if (cod == 0):
                        print
                        break
                    lista = t_str_list(busca('c:\Angus System\estoque.sim', cod))
                    print 'Nome:', lista[1]
                    print 'Preço:', lista[3]
                    lista[3] = input('Informe o novo valor: R$ ')
                    produto = t_list_str(lista)
                    qtd_produtos = int(busca('c:\Angus System\dados.sim',5))
                    substituicao('c:\Angus System\estoque.sim',qtd_produtos,cod,produto)
                    print 'Alteração realizada com sucesso!'
                    print
            elif (x == 2): #estoque
                while (True):
                    cod = input('Informe o código (0 - Voltar): ')
                    if (cod == 0):
                        print
                        break
                    lista = t_str_list(busca('c:\Angus System\estoque.sim', cod))
                    print 'Nome:', lista[1]
                    print 'Estoque:', lista[4]
                    lista[4] = input('Informe a quantidade em estoque: ')
                    produto = t_list_str(lista)
                    qtd_produtos = int(busca('c:\Angus System\dados.sim', 5))
                    substituicao('c:\Angus System\estoque.sim', qtd_produtos, cod, produto)
                    print 'Alteração realizada com sucesso!'
                    print
            elif (x == 3): #geral
                cod = input('Informe o código (0 - Voltar): ')
                if (cod == 0):
                    print
                    break
                lista = t_str_list(busca('c:\Angus System\estoque.sim', cod))
                print 'Nome:', lista[1]
                lista[1] = raw_input('Informe o novo nome: ')
                print 'Compra:', lista[2]
                lista[2] = raw_input('Informe o valor de compra: ')
                print 'Preço:', lista[3]
                lista[3] = raw_input('Informe o novo valor: ')
                print 'Estoque:', lista[4]
                lista[4] = raw_input('Informe a quantidade em estoque: ')
                produto = t_list_str(lista)
                qtd_produtos = int(busca('c:\Angus System\dados.sim', 5))
                substituicao('c:\Angus System\estoque.sim', qtd_produtos, cod, produto)
                print 'Alteração realizada com sucesso!'
                print
            elif (x == 0):
                break
            else:
                print 'Opção Inválida!'
                print

    # Compra de Mercadorias
    elif (x == 4):
        while(True):
            print 'COMPRA DE MERCADORIAS'
            print '1 - Carregar Arquivo'
            print '2 - Entrada Manual'
            print '0 - Voltar'
            x = input('Informe a opção desejada: ')
            print
            if (x == 1): #carregar arquivo
                arquivo = 'c:\Angus System\Notas Fiscais de Compra\%s.xm' %raw_input('Digite o nome do arquivo: ')
                xm = open (arquivo,'r')

                for k in range(4):
                   x = xm.readline()
                z,z,z,qtd_nota = x.split()
                qtd_nota = int(qtd_nota)

                for k in range(qtd_nota):
                    lista_nota = t_str_list(busca(arquivo, 6+k))
                    cod = lista_nota[0]

                    lista_estoque = t_str_list(busca('c:\Angus System\estoque.sim', cod))
                    lista_estoque[2] = lista_nota[2]
                    lista_estoque[4] += lista_nota[4]
                    produto = t_list_str(lista_estoque)
                    qtd_produtos = int(busca('c:\Angus System\dados.sim', 5))
                    substituicao('c:\Angus System\estoque.sim', qtd_produtos, cod, produto)

                print 'Arquivo Carregado com Sucesso!'
                print
            elif (x == 2): #entrada manual
                while (True):
                    cod = input('Informe o código (0 - Voltar): ')
                    if (cod == 0):
                        print
                        break
                    lista = t_str_list(busca('c:\Angus System\estoque.sim', cod))
                    lista[2] = input('Informe o valor de compra: R$ ')
                    lista[3] = input('Informe o valor de venda: R$ ')
                    lista[4] += input('Informe a quantidade: ')
                    produto = t_list_str(lista)
                    qtd_produtos = int(busca('c:\Angus System\dados.sim', 5))
                    substituicao('c:\Angus System\estoque.sim', qtd_produtos, cod, produto)
                    print 'Entrada Realizada com Sucesso!'
                    print
            elif (x == 0):
                break
            else:
                print 'Opção Inválida!'
                print

    # Cadastrar Produto
    elif (x == 5):
        print 'CADASTRO DE MERCADORIAS'
        estoque = open('c:\Angus System\estoque.sim', 'a')
        res = 'sim'
        while (res == 'sim'):
            nome = raw_input('Infome o nome do produto (0 - Voltar): ')
            if (nome == '0'):
                print
                break
            cod = int(busca('c:\Angus System\dados.sim',5)) + 1
            produto = '%s/%s/0/0/0' %(cod, nome)
            estoque.write(produto + '\n')
            substituicao('c:\Angus System\dados.sim', 9, 5, cod)
            res = raw_input('Cadastrar outro produto? (sim/nao): ')
            print
        estoque.close()

    # Configurações
    elif (x == 6):
        print 'Entrar como administrador:'
        x = login_adm(6,11)
        while (x != 11):
            print 'CONFIGURAÇÕES:'
            print '1 - Alterar Nome da Empresa e CNPJ'
            print '2 - Cadastro de Colaboradores'
            print '3 - Informações do Colaborador'
            print '4 - Informações da Empresa'
            print '0 - Sair'
            x = input('Informe a opção desejada: ')
            print

            if (x == 1):
                nome = raw_input('Informe o Nome da Empresa: ')
                substituicao('c:\Angus System\dados.sim',9,1,nome)
                cnpj = raw_input('Informe o número do CNPJ: ')
                substituicao('c:\Angus System\dados.sim', 9, 2, cnpj)
                print 'Alteração realizada com sucesso!'
                print
            elif (x == 2):
                print 'Cadastro de Colaboradores:'

                res = 'sim'
                while (res == 'sim'):
                    colaborador = []
                    nome = raw_input('Digite o nome: ')
                    senha = codificador(raw_input('Digite uma senha (somente numeros): '))
                    data = data_dia
                    print 'Cadastrar como administrador?'
                    r = input('(1-Sim / 2-Não): ')

                    if (r == 1):
                        cadastro = int(busca('c:\Angus System\dados.sim', 3)) + 1
                        print 'Login:', cadastro
                        substituicao('c:\Angus System\dados.sim',9,3,cadastro)
                    elif (r == 2):
                        cadastro = int(busca('c:\Angus System\dados.sim', 4)) + 1
                        print 'Cadastro:', cadastro
                        substituicao('c:\Angus System\dados.sim',9,4, cadastro)

                    colaborador = '%i-%s-%s-%s' %(cadastro, nome, senha, data)

                    if (r == 1):
                        cadastro1 = open('c:\Angus System\cadastros1.sim', 'a')
                        cadastro1.write(colaborador + '\n')
                        cadastro1.close()
                    elif (r == 2):
                        cadastro2 = open('c:\Angus System\cadastros2.sim', 'a')
                        cadastro2.write(colaborador + '\n')
                        cadastro2.close()
                    print 'Cadastro realizado com sucesso!'
                    print
                    res = raw_input('Cadastrar outro colaborador? (sim/nao): ')
                    print

            elif (x == 3):
                print 'Informações do Colaborador:'
                cod = raw_input('Informe o cadastro: ')
                if (cod[0] == '1'):
                    lista = t_str_list_cad(busca('c:\Angus System\cadastros1.sim',int(cod[1:4])))
                elif (cod[0] == '2'):
                    lista = t_str_list_cad(busca('c:\Angus System\cadastros2.sim',int(cod[1:4])))
                print 'Nome:', lista[1]
                print 'Senha:', decodificador(lista[2])
                print 'Cadastro em', lista[3]
                print
            elif (x == 4):
                dados = open ('c:\Angus System\dados.sim', 'r')
                print 'Informações da Empresa:'
                print 'Nome:', dados.readline()[0:-1]
                print 'CNPJ:', dados.readline()[0:-1]
                print 'Quantidade de Administradores:', dados.readline()[1:-1]
                print 'Quantidade de Colaboradores:', dados.readline()[1:-1]
                print 'Produtos Cadastrados:', dados.readline()[0:-1]
                dados.close()
                print
            elif (x == 0):
                x = 11

    # Fechar Sistema
    elif (x == 7):
        print 'FECHAMENTO DO SISTEMA - LOGIN DE ADMINISTRADOR'
        x = login_adm(10, 7)
        if (busca('c:\Angus System\dados.sim',7) == 'aberto'):
            print 'A operação solicitada não foi concluída:'
            print 'O caixa não foi encerrado!'
            print
            x = 7
            y = 7
        else:
            y = 10
        if (x == 10 and y == 10):
            # Atualização de Data
            d += 1
            if (m == 2 and d == 29):
                d = 1
                m += 1
            elif ((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d == 32):
                d = 1
                m += 1
            elif ((m == 4 or m == 6 or m == 9 or m == 11) and d == 31):
                d = 1
                m += 1
            if (m == 13):
                m = 1
                a += 1
            data_proximo = '%i/%i/%i' %(d,m,a)

            # Atualização de Arquivo
            total_de_vendas = busca('c:\Angus System\dados.sim', 9)
            substituicao('c:\Angus System\dados.sim', 9, 6, data_proximo)
            substituicao('c:\Angus System\dados.sim', 9, 9, 0)
            vendas = open(nome_arquivo, 'a')
            vendas.write(total_de_vendas)
            print 'O SISTEMA ANGUS FOI ENCERRADO COM SUCESSO'

    # Sair
    elif (x == 0):
        x = 10

    else:
        print 'Opção Inválida!'
        print

print 'SISTEMA ANGUS - v1.0'
print 'PROGRAMA FINALIZADO', data_dia