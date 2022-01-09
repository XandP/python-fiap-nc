from identificacao_de_funcoes import *

minha_lista = []
print('Preenchendo:')
preencher_inventario(minha_lista)
print('Exibindo:')
exibir_inventario(minha_lista)

print('Pesquisando:')
localizar_por_nome(minha_lista)
print('Alterando:')
depreciar_por_nome(minha_lista, 20)

print('Excluindo:')
print(excluir_por_serial(minha_lista))
exibir_inventario(minha_lista)

print('Resumindo:')
resumir_valores(minha_lista)