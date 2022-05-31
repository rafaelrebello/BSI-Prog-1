dias = int(input('Digite os dias: '))
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

print(dias, horas, minutos, segundos)

segundosDias = dias * 86400
segundosHoras = horas * 3600
segundosMinutos = minutos * 60

totalSegundos = segundosDias + segundosHoras + segundosMinutos + segundos

print('O total de segundos é de: ', totalSegundos)

#d = d * 86400 h = h*3600 m = m*60 r = d+h+m+ss
'''
teste
'''