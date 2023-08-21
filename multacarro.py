print('')
v = float(input('A velocidade que foi detectada pelo radar é: '))
if v > 80:
    print('')
    print('Multado, você excedeu o limite de velocidade permitido que é de 80km/h')
    multa = (v-80) * 7
    print('Valor da Multa: R${:.2f}'.format(multa))
print('')
print('Dirija com segurança!')

