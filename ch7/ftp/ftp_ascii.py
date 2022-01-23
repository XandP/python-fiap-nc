import os
from ftplib import *


def escrever_linha(data):
    arq.write(data)
    arq.write(os.linesep)


ftp_ativo = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
arquivo = 'LEIAME'
ftp.set_pasv(ftp_ativo)
with open(arquivo, 'w') as arq:
    ftp.retrlines('RETR README', escrever_linha)
ftp.quit()
