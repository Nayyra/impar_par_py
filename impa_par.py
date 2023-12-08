nm = int(input('digite um número entre 0 e 1000: '))
resultado = nm % 2

if (resultado == 0):
    print('o número {} é par'.format(nm))
else:
    print('o número {} é impar'.format(nm))