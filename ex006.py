# A variável algo vira um OBJETO que recebe ATRIBUTOS e PARÂMETROS
# Os as strings tem os MÉTODOS... ex.. .isalpha, .isalnum....
algo = input('Digite algo na tela: ')
print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços: ', algo.isspace())
print('É um número? ', algo.isalnum())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minúsculas? ', algo.islower())
print('Está capitalizada: ', algo.istitle())
