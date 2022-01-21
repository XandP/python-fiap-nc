import getpass
from datetime import datetime

print('Usuário............. ', getpass.getuser())
print('Data Completa....... ', datetime.now())
print('Dia de hoje......... ', datetime.now().day)
print('Mês atual........... ', datetime.now().month)
print('Ano atual........... ', datetime.now().year)
print('Hora atual.......... ', datetime.now().hour)
print('Minuto atual........ ', datetime.now().minute)
print('Segundo atual....... ', datetime.now().second)
