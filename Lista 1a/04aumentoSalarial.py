salario = float(input('Digite o valor do salário: '))
aumento = int(input('Digite a porcentagem do aumento: '))

valorAumento = salario * ((aumento/100))
novoSalario = salario + valorAumento

print('O valor do aumento é de:', valorAumento, 'e o novo salário é de:',  novoSalario)