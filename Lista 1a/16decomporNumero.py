
numero = int(input('digite o número menor que 1000: '))

centenas = numero // 100
dezenas = numero // 10 - (centenas * 10)
unidades = numero - ((numero//10) * 10)

'''
centenas = numero //100
dezenas = (numero%100)//10
unidades = numero%10
'''

print('centenas: ',centenas,'dezenas: ', dezenas,'unidades: ', unidades)
