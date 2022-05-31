cigarrosDia = int(input('Digite o número de cigarros fumados por dia: '))
anosDeFumo = int(input('Digite o número de anos de fumo: '))

totalCigarros = (cigarrosDia * 365) * anosDeFumo

print('Você já fumou: ',totalCigarros)

diasVidaPerdidos = int((totalCigarros * 10) / 1440)

print('Você já perdeu', diasVidaPerdidos, 'dias de vida')