""" Faça um programa que jogue PAR OU IMPAR com o computador. O jogo só será interrompido quando o jogador Perder mos-
trando o total de vitórias consecutivas que ele conquistou no final do jogo """
from random import randint
from time import sleep

v = 0
print('\033[33m=+\033[0m' * 20)
print('       \033[37mVAMOS JOGAR PAR OU ÍMPAR ?\033[0m')
print('\033[33m=+\033[0m' * 20)
while True:
    jogador = int(input(' Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[37m Ímpar ou Par \033[0m[\033[31mI\033[0m/\033[31mP\033[0m]? ')).strip().upper()[0]
    print('\033[33m--\033[0m' * 20)
    print(f'Você jogou {jogador}! E o computador {computador}! O total de {total} = ', end='')
    print('\033[33mDEU PAR\033[0m' if total % 2 == 0 else '\033[33mDEU ÍMPAR\033[0m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[32mVOCÊ VENCEU\033[0m!')
            sleep(2)
            v += 1
        else:
            print('\033[31mVOCÊ PERDEU\033[0m!')
            sleep(2)
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[32mVOCÊ VENCEU\033[0m!')
            sleep(2)
            v += 1
        else:
            print('\033[31mVOCÊ PERDEU\033[0m!')
            sleep(2)
            break
    print('\033[33m--\033[0m' * 20)
    print('\033[37mVamos jogar novamente!\033[0m')
    print('--' * 20)
print('\033[33m--\033[0m' * 20)
print(f'\033[31mGAMER OVER!\033[0m Você venceu apenas {v} vezes')
print('\033[33m=-\033[0m' * 20)
