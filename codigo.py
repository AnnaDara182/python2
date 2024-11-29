#Boas vindas e o cardápio para visualização pro cliente
print('Bem vindo(a) a loja de marmitas da Anna Dara Moraes Araujo\n')
print('-'*23 + 'Cardápio' + '-'*27)
print('-'*58)
print('-'*2 + '| ' + 'Tamanho ' + '| ' + 'Bife Acebolado (BA) ' + '| ' + 'Filé de Frango (FF)' + '|' + '-'*2)
print('-'*2 + '| ' + ' '*3 + 'P ' + ' '*3 + '|' + ' '*7 + 'R$16,00 ' + ' '*6 + '| ' + ' '*6 + 'R$15,00' + ' '*6 + '|' + '-'*2)
print('-'*2 + '| ' + ' '*3 + 'M ' + ' '*3 + '|' + ' '*7 + 'R$18,00 ' + ' '*6 + '| ' + ' '*6 + 'R$17,00' + ' '*6 + '|' + '-'*2)
print('-'*2 + '| ' + ' '*3 + 'G ' + ' '*3 + '|' + ' '*7 + 'R$22,00 ' + ' '*6 + '| ' + ' '*6 + 'R$21,00' + ' '*6 + '|' + '-'*2)
print('-'*58)

#Acumuladores para soma dos valores
valor = 0
total = 0

#Variáveis para escolher o sabor e o tamanho
while True:
  sabor = input('\nEscolha o sabor (BA/FF): ').upper()
  if(sabor != 'BA' and sabor != 'FF'):
    print('Sabor inválido, tente novamente')
    continue

  tamanho = input('Escolha o tamaho (P/M/G): ').upper()
  if(tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
    print('Tamanho inválido, tente novamente')
    continue

#Verificando os valores conforme o sabor e o tamanho escolhido
  if sabor == 'BA':
    if tamanho == 'P':
      print('Você pediu um bife acebolado pequeno e o total é de R$16,00\n')
      valor = 16
    elif tamanho == 'M':
      print('Você pediu um bife acebolado médio e o total é de R$18,00\n')
      valor = 18
    else:
      print('Você pediu um bife acebolado grande e o total é de R$22,00\n')
      valor = 22

  if sabor == 'FF':
    if tamanho == 'P':
      print('Você pediu um filé de frango pequeno e o total é de R$15,00\n')
      valor = 15
    elif tamanho == 'M':
      print('Você pediu um filé de frango pequeno e o total é de R$17,00\n')
      valor = 17
    else:
      print('Você pediu um filé de frango pequeno e o total é de R$21,00\n')
      valor = 21
  total=total+valor
#Verificar se deseja pedir algo mais, se não finaliza o pedido.
  if input('Deseja pedir mais alguma coisa? (S/N) ').upper() == 'N':
    print('O valor total do pedido é de R${:.2f}'.format(total))
    break