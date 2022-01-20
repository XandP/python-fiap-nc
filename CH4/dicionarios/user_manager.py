from funcoes.funcoes_dicionarios import *
usuarios = {}
opcao_cadastro = ''

while opcao_cadastro != 'S':
    opcao_cadastro = selecionar_opt()

    if opcao_cadastro == 'I':
        inserir(usuarios)

    elif opcao_cadastro == 'P':
        pesquisar(usuarios,input('Digite o apelido do usuário que deseja buscar: '))

    elif opcao_cadastro == 'E':
        excluir(usuarios,input('Digite o apelido do usuário que deseja remover: '))

    elif opcao_cadastro == 'L':
        listar(usuarios)

print('Encerrando o programa.')