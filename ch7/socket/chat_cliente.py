from socket import *

msg = ''
servidor = '127.0.0.1'
porta = 43210

print('Digite algo para enviar uma mensagem ou digite "SAIR" para fechar o chat.')

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input('Você: '), 'utf-8')
    obj_socket.send(msg)
    resposta = obj_socket.recv(1024)
    print('Resposta do Servidor: ', str(resposta)[2:-1])

    if str(msg)[2:-1].upper() == 'SAIR':
        break

obj_socket.close()
