print('')
print ('Escolha entre "Multa Carro" e "Media Nota" ')
print('')
print ('Multa Carro: 1')
print ('Media Nota: 2')
print('')

nome = int(input('Escolha entre 1 e 2: '))

match nome:
    case 1:
        import multacarro

    case 2:
        import medianota

    case _:
        ValueError
        print('ERRO: Digite apenas NÚMEROS entre 1 e 2! ')

