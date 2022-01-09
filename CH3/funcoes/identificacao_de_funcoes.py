def preencher_inventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento = [input('Equipamento: '),
                    float(input('Valor: ')),
                    int(input('Número Serial: ')),
                    input('Departamento: ')]
        lista.append(equipamento)
        resp = input('Digite "S" para continuar: ').upper()

    return equipamento

def exibir_inventario(lista):
    for elemento in lista:
        print('Nome.........', elemento[0])
        print('Valor........', elemento[1])
        print('Serial.......', elemento[2])
        print('Departamento.', elemento[3])

def localizar_por_nome(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])

def depreciar_por_nome(lista,pct):
    depreciacao = input("Digite o nome do equipamento que será depreciado em 20%: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-pct/100)
            print("Novo valor: ", elemento[1])

def excluir_por_serial(lista):
    serial=int(input('Digite o Serial do equipamento que será excluído: '))
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
    return 'Itens excluídos.'

def resumir_valores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])

    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O valor total dos equipamentos é de: ", sum(valores))