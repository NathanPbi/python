n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

adi = n1 + n2
mul = n1 * n2
div = n1 / n2
divInt = n1 // n2
pot = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(adi, mul, div))
print('Divisão inteira {} e potência {}'.format(divInt, pot))