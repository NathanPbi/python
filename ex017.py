salario = float(input('Digite o valor do salário: R$ '))
novo = salario + salario * 15 / 100
print('Com base no atual salário de R$ {:.2f}, seu novo salário com 15% de aumento será R$ {:.2f}'.format(salario, novo))
