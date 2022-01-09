equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Número Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite "S" para continuar: ').upper()

serial_deletar = int(input('Digite o Número Serial do equipamento que será eliminado: '))

for i in range(0,len(equipamentos)):
    if seriais[i] == serial_deletar:
        del(equipamentos[i], valores[i], seriais[i], departamentos[i])
        break

for indice in range(0,len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print('Nome.........', equipamentos[indice])
    print('Valor........', valores[indice])
    print('Serial.......', seriais[indice])
    print('Departamento.', departamentos[indice])