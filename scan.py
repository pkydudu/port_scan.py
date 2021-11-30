import socket
from time import sleep
resp = ''
print('\033[34m-=' * 20)
print(f'{"PORTA SCAN DO DUDU".center(40)}')
print('-=' * 20)
print('\033[m')
while True:
    ip = input('Digite o ip: ')
    ports = [80, 8080, 23, 21, 22, 843, 3333, 443, 2222]
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for p in ports:
        sleep(0.5)
        if con.connect_ex((ip, p)) == 0:
            print(f'\033[32m{p} -> Aberta\033[m')

        else:
            print(f'\033[31m{p} -> Fechada\033[m')
    resp = str(input('deseja continuar?[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('\033[31mValor invalído!! Tente novamente\033[m')
        resp = str(input('deseja continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('\033[31mFINALIZANDO.....\033[m')
        sleep(1)
        break

