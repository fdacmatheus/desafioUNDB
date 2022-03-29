import random  # biblioteca para numeros aleatorios
import time  # biblioteca para inserir tempo de espera


fila = ['Matheus', 'Joao', 'Marcos', 'Paulo',
        'Lucas', 'Mario', 'Rodrigo', 'Maria', 'Marilia', 'Joana', 'Perla']  # fila de clientes
atendente1 = []  # fila de atendimento atendente 1
atendente2 = []  # fila de atendimento atendente 2
atendente3 = []  # fila de atendimento atendente 3
atendente4 = []  # fila de atendimento atendente 4
horaAtendente1 = []  # banco de horas Atendente 1
atendente1atendimentos = []  # Atendimentos finalizados atendente 1
horaAtendente2 = []  # banco de horas Atendente 2
atendente2atendimentos = []  # Atendimentos finalizados atendente 2
horaAtendente3 = []  # banco de horas Atendente 3
atendente3atendimentos = []  # Atendimentos finalizados atendente 3
horaAtendente4 = []  # banco de horas Atendente 2
atendente4atendimentos = []  # Atendimentos finalizados atendente 4

while True:  # Inicio do sistema de escolhas
    print('-='*20)
    print('Sistema de ligações')
    print('-='*20)
    dash = int(input(
        'Utilize o menu abaixo\n[1] Iniciar programa\n[2] Ver informacoes atendentes \n[3] Adicionar pessoas na fila \n[4] Ver fila\n[0] Sair \n'))
    if dash == 1:
        for i in range(4):  # Coletar os primeiros 4 clientes
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

        # Coletar os clientes restantes que estão na fila e atende-los em ordem de chegada.
        while True:

            if len(fila) != 0:
                if len(atendente1) < 1:
                    pegarFila = fila.pop(0)
                    atendente1.append(pegarFila)
                else:
                    if len(atendente2) == 0:
                        print('NAO TEM CLIENTES PARA ATENDER')
                    else:
                        print('-='*20)
                        print('Atendente 1')
                        print('-='*20)
                        print(f'Clientes na fila: {atendente1}')
                        print(f'Atendendo atualmente {atendente1[0]}')
                        print(f'finalizando...')
                        time.sleep(0.5)
                        tempo1 = random.randrange(3, 15)
                        print(
                            f'o tempo de atendimento de {atendente1[0]} foi {tempo1} min')
                        horaAtendente1.append(tempo1)
                        tirarCliente = atendente1.pop(0)
                        atendente1atendimentos.append(tirarCliente)
                        print(
                            f'removendo da filae e chamando o próximo')
                        time.sleep(0.5)
            else:
                print('Fila vazia')

            if len(fila) != 0:
                if len(atendente2) < 1:
                    pegarFila = fila.pop(0)
                    atendente2.append(pegarFila)
                else:
                    if len(atendente2) == 0:
                        print('NAO TEM CLIENTES PARA ATENDER')
                    else:
                        print('-='*20)
                        print('Atendente 2')
                        print('-='*20)
                        print(f'Clientes na fila: {atendente2}')
                        print(f'Atendendo atualmente {atendente2}')
                        print(f'finalizando...')
                        time.sleep(0.5)
                        tempo2 = random.randrange(3, 15)
                        print(
                            f'o tempo de atendimento de {atendente2[0]} foi {tempo2} min')
                        horaAtendente2.append(tempo2)
                        tirarCliente = atendente2.pop(0)
                        atendente2atendimentos.append(tirarCliente)
                        print(
                            f'removendo da fila e chamando o próximo')
                        time.sleep(0.5)
            else:
                print('Fila vazia')

            if len(fila) != 0:
                if len(atendente3) < 1:
                    pegarFila = fila.pop(0)
                    atendente3.append(pegarFila)
                else:
                    if len(atendente3) == 0:
                        print('NAO TEM CLIENTES PARA ATENDER')
                    else:
                        print('-='*20)
                        print('Atendente 3')
                        print('-='*20)
                        print(f'Clientes na fila: {atendente3}')
                        print(f'Atendendo atualmente {atendente3}')
                        print(f'finalizando...')
                        time.sleep(0.5)
                        tempo3 = random.randrange(3, 15)
                        print(
                            f'o tempo de atendimento de {atendente3[0]} foi {tempo3} min')
                        horaAtendente3.append(tempo3)
                        tirarCliente = atendente3.pop(0)
                        atendente3atendimentos.append(tirarCliente)
                        print(
                            f'removendo da fila e chamando o próximo')
                        time.sleep(0.5)
            else:
                print('Fila vazia')

            if len(fila) != 0:
                if len(atendente4) < 1:
                    pegarFila = fila.pop(0)
                    atendente4.append(pegarFila)
                else:
                    if len(atendente4) == 0:
                        print('NAO TEM CLIENTES PARA ATENDER')
                    else:
                        print('-='*20)
                        print('Atendente 4')
                        print('-='*20)
                        print(f'Clientes na fila: {atendente4}')
                        print(f'Atendendo atualmente {atendente4}')
                        print(f'finalizando...')
                        time.sleep(0.5)
                        tempo4 = random.randrange(3, 15)
                        print(
                            f'o tempo de atendimento de {atendente4[0]} foi {tempo4} min')
                        horaAtendente4.append(tempo4)
                        tirarCliente = atendente4.pop(0)
                        atendente4atendimentos.append(tirarCliente)
                        print(
                            f'removendo da fila e chamando o próximo')
                        time.sleep(0.5)

                    # ATENDER CLIENTES QUE FICARAM NA FILA
            if len(atendente1) != 0:
                print('-='*20)
                print('Atendente 1')
                print('-='*20)
                print(f'Clientes na fila: {atendente1}')
                print(f'Atendendo atualmente {atendente1}')
                print(f'finalizando...')
                time.sleep(0.5)
                tempo1 = random.randrange(3, 15)
                print(
                    f'o tempo de atendimento de {atendente1[0]} foi {tempo1} min')
                horaAtendente1.append(tempo1)
                tirarCliente = atendente1.pop(0)
                atendente1atendimentos.append(tirarCliente)
                time.sleep(0.5)
            if len(atendente2) != 0:
                print('-='*20)
                print('Atendente 2')
                print('-='*20)
                print(f'Clientes na fila: {atendente2}')
                print(f'Atendendo atualmente {atendente2}')
                print(f'finalizando...')
                time.sleep(0.5)
                tempo2 = random.randrange(3, 15)
                print(
                    f'o tempo de atendimento de {atendente2[0]} foi {tempo2} min')
                horaAtendente2.append(tempo2)
                tirarCliente = atendente2.pop(0)
                atendente1atendimentos.append(tirarCliente)
                time.sleep(0.5)

            if len(atendente3) != 0:
                print('-='*20)
                print('Atendente 3')
                print('-='*20)
                print(f'Clientes na fila: {atendente3}')
                print(f'Atendendo atualmente {atendente3}')
                print(f'finalizando...')
                time.sleep(0.5)
                tempo3 = random.randrange(3, 15)
                print(
                    f'o tempo de atendimento de {atendente3[0]} foi {tempo3} min')
                horaAtendente3.append(tempo3)
                tirarCliente = atendente3.pop(0)
                atendente3atendimentos.append(tirarCliente)
                time.sleep(0.5)
            if len(atendente4) != 0:
                print('-='*20)
                print('Atendente 4')
                print('-='*20)
                print(f'Clientes na fila: {atendente4}')
                print(f'Atendendo atualmente {atendente4}')
                print(f'finalizando...')
                time.sleep(0.5)
                tempo4 = random.randrange(3, 15)
                print(
                    f'o tempo de atendimento de {atendente4[0]} foi {tempo4} min')
                horaAtendente4.append(tempo4)
                tirarCliente = atendente4.pop(0)
                atendente4atendimentos.append(tirarCliente)
                time.sleep(0.5)
            else:
                print('Fila vazia')
                if len(fila) == 0:
                    break
    if dash == 2:
        calchorasAtendente1 = sum(horaAtendente1)/3
        calchorasAtendente2 = sum(horaAtendente2)/3
        calchorasAtendente3 = sum(horaAtendente3)/3
        calchorasAtendente4 = sum(horaAtendente4)/3
        print('-='*20)
        print('Dashboard de resultados')
        print('-='*20)
        print("")
        if int(calchorasAtendente1) > int(calchorasAtendente2) and int(calchorasAtendente1) > int(calchorasAtendente3) and int(calchorasAtendente1) > int(calchorasAtendente4):
            print(
                f'O atendente 1 teve  o maior tempo de atendimento: {calchorasAtendente1:.2f}')
        elif int(calchorasAtendente2) > int(calchorasAtendente1) and int(calchorasAtendente2) > int(calchorasAtendente3) and int(calchorasAtendente2) > int(calchorasAtendente4):
            print(
                f'O atendente 2 teve o  maior tempo de atendimento: {calchorasAtendente2:.2f}')
        elif int(calchorasAtendente3) > int(calchorasAtendente1) and int(calchorasAtendente3) > int(calchorasAtendente2) and int(calchorasAtendente3) > int(calchorasAtendente4):
            print(
                f'O atendente 3 teve o  maior tempo de atendimento: {calchorasAtendente3:.2f}')
        elif int(calchorasAtendente4) > int(calchorasAtendente1) and int(calchorasAtendente4) > int(calchorasAtendente2) and int(calchorasAtendente4) > int(calchorasAtendente3):
            print(
                f'O atendente 4 teve o  maior tempo de atendimento: {calchorasAtendente4:.2f}')
        print("")
        print('-='*20)
        print(
            f'O atendente 1 atendeu o total de {len(atendente1atendimentos)} pessoas')
        print(
            f'A media de minutos em atendimento do atendente 1 é {calchorasAtendente1:.2f} minutos')
        print('-='*20)
        print(
            f'O atendente 2 atendeu o total de {len(atendente2atendimentos)} pessoas')
        print(
            f'A media de minutos em atendimento do atendente 2 é {calchorasAtendente2:.2f} minutos')
        print('-='*20)
        print(
            f'O atendente 3 atendeu o total de {len(atendente3atendimentos)} pessoas')
        print(
            f'A media de minutos em atendimento do atendente 3 é {calchorasAtendente3:.2f} minutos')
        print('-='*20)
        print(
            f'O atendente 4 atendeu o total de {len(atendente4atendimentos)} pessoa')
        print(
            f'A media de minutos em atendimento do atendente 4 é {calchorasAtendente4:.2f} minutos')
        print("")
    if dash == 3:
        nome = input('Digite o nome: ')
        fila.append(nome)
    if dash == 4:
        if len(fila) == 0:
            print('FILA VAZIA')
        else:
            print(fila)
    if dash == 0:
        print('Finalizando')
        break
