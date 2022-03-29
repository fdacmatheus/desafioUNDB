import random
import time


fila = ['Matheus', 'Joao', 'Marcos', 'Paulo',
        'Lucas', 'Mario', 'Rodrigo', 'Maria', 'Marilia', 'Joana', 'Perla']
atendente1 = []
atendente2 = []
atendente3 = []
atendente4 = []
horaAtendente1 = []
atendente1atendimentos = []
horaAtendente2 = []
atendente2atendimentos = []
horaAtendente3 = []
atendente3atendimentos = []
horaAtendente4 = []
atendente4atendimentos = []

while True:
    print('-='*20)
    print('Sistema de ligações')
    print('-='*20)
    dash = int(input(
        'Utilize o menu abaixo\n[1] Iniciar programa\n[2] Ver informacoes atendentes \n[3] Adicionar pessoas na fila \n[4] Ver fila\n[0] Sair \n'))
    if dash == 1:
        for i in range(4):
            if len(fila) != 0:
                True
                if len(atendente1) == 0:
                    pegarFila = fila.pop(0)
                    atendente1.append(pegarFila)
                elif len(atendente2) == 0:
                    pegarFila = fila.pop(0)
                    atendente2.append(pegarFila)
                elif len(atendente3) == 0:
                    pegarFila = fila.pop(0)
                    atendente3.append(pegarFila)
                elif len(atendente4) == 0:
                    pegarFila = fila.pop(0)
                    atendente4.append(pegarFila)
            else:
                print('Fila vazia')

        while True:
            if len(atendente1) >= 1:
                if len(fila) != 0:
                    pegarFila = fila.pop(0)
                    atendente1.append(pegarFila)
                    print(f'Clientes na fila: {atendente1}')
                    print(f'Atendendo atualmente {atendente1[0]}')
                    print(f'finalizando...')
                    time.sleep(1)
                    tempo1 = random.randrange(3, 15)
                    print(
                        f'o tempo de atendimento de {atendente1[0]} foi {tempo1} min')
                    horaAtendente1.append(tempo1)
                    tirarCliente = atendente1.pop(0)
                    atendente1atendimentos.append(tirarCliente)
                    print(
                        f'removendo da filae e chamando o próximo: {atendente1[0]}')
                    time.sleep(1)
                else:
                    print('Fila vazia')
            if len(atendente2) >= 1:
                if len(fila) != 0:
                    pegarFila = fila.pop(0)
                    atendente2.append(pegarFila)
                    print(f'Clientes na fila: {atendente2}')
                    print(f'Atendendo atualmente {atendente2[0]}')
                    print(f'finalizando...')
                    time.sleep(1)
                    tempo2 = random.randrange(3, 15)
                    print(
                        f'o tempo de atendimento de {atendente2[0]} foi {tempo2} min')
                    horaAtendente2.append(tempo2)
                    tirarCliente = atendente2.pop(0)
                    atendente2atendimentos.append(tirarCliente)
                    print(
                        f'removendo da fila e chamando o próximo: {atendente2[0]}')
                    time.sleep(1)
                else:
                    print('Fila vazia')
            if len(atendente3) >= 1:
                if len(fila) != 0:
                    pegarFila = fila.pop(0)
                    atendente3.append(pegarFila)
                    print(f'Clientes na fila: {atendente3}')
                    print(f'Atendendo atualmente {atendente3[0]}')
                    print(f'finalizando...')
                    time.sleep(1)
                    tempo3 = random.randrange(3, 15)
                    print(
                        f'o tempo de atendimento de {atendente3[0]} foi {tempo3} min')
                    horaAtendente3.append(tempo3)
                    tirarCliente = atendente3.pop(0)
                    atendente3atendimentos.append(tirarCliente)
                    print(
                        f'removendo da fila e chamando o próximo: {atendente3[0]}')
                    time.sleep(1)
                else:
                    print('Fila vazia')
            if len(atendente4) >= 1:
                if len(fila) != 0:
                    pegarFila = fila.pop(0)
                    atendente4.append(pegarFila)
                    print(f'Clientes na fila: {atendente4}')
                    print(f'Atendendo atualmente {atendente4[0]}')
                    print(f'finalizando...')
                    time.sleep(1)
                    tempo4 = random.randrange(3, 15)
                    print(
                        f'o tempo de atendimento de {atendente4[0]} foi {tempo4} min')
                    horaAtendente4.append(tempo4)
                    tirarCliente = atendente4.pop(0)
                    atendente4atendimentos.append(tirarCliente)
                    print(
                        f'removendo da fila e chamando o próximo: {atendente4[0]}')
                    time.sleep(1)
                else:
                    print('Fila vazia')
            if len(fila) == 0:
                break
    if dash == 2:
        calchorasAtendente1 = sum(horaAtendente1)
        calchorasAtendente2 = sum(horaAtendente2)
        calchorasAtendente3 = sum(horaAtendente1)
        calchorasAtendente4 = sum(horaAtendente2)
        print('-='*20)
        print('Dashboard de resultados')
        print('-='*20)
        print("")
        print('-='*20)
        print(
            f'O atendente 1 atendeu o total de {len(atendente1atendimentos)} pessoas')
        print(
            f'A media de minutos em atendimento do atendente 1 é {calchorasAtendente1/3:.2f} minutos')
        print('-='*20)
        print(
            f'O atendente 2 atendeu o total de {len(atendente2atendimentos)} pessoas')
        print(
            f'A media de minutos em atendimento do atendente 2 é {calchorasAtendente2/3:.2f} minutos')
        print('-='*20)
        print(
            f'O atendente 3 atendeu o total de {len(atendente3atendimentos)} pessoas')
        print(
            f'A media de minutos em atendimento do atendente 3 é {calchorasAtendente3/3:.2f} minutos')
        print('-='*20)
        print(
            f'O atendente 4 atendeu o total de {len(atendente4atendimentos)} pessoa')
        print(
            f'A media de minutos em atendimento do atendente 4 é {calchorasAtendente4/3:.2f} minutos')
    if dash == 3:
        nome = input('Digite o nome: ')
        fila.append(nome)
    if dash == 4:
        print(fila)
    if dash == 0:
        print('Finalizando')
        break
