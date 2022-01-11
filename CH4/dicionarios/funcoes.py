def selecionar_opt():
    response = input('Escolha uma opção: '+
                       'I - Inserir '+
                       'P - Pesquisar '+
                       'E - Excluir '+
                       'L - Listar '+
                       'S - Sair ').upper()
    return response

def inserir(dicionario):
    apelido = input('Digite o apelido do usuário: ')
    nome_usuario = input('Digite o nome do usuário: ')
    data_atual = input('Digite o dia de hoje: ')
    nome_area = input('Digite o nome da área onde o programa está sendo acessado: ')
    dicionario[apelido] = [nome_usuario, data_atual, nome_area]

def pesquisar(dicionario,chave):
    lista = dicionario.get(chave)
    if lista != None:
        print('Nome........... ', lista[0])
        print('Último acesso.. ', lista[1])
        print('Última estação. ', lista[2])
    else:
        print('Usuário não encontrado.')

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print('Usuário removido.')

def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Login:', chave)
        print('Dados:', valor)