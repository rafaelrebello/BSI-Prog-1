prova1 = float(input('digite a nota da primeira prova: '))
prova2 = float(input('digite a nota da segunda prova: '))
trabalho1 = float(input('digite a nota do primeiro trabalho: '))
trabalho2 = float(input('digite a nota do segundo trabalho: '))

media = ((prova1 * 7) + (prova2 *7) + (trabalho1 * 3) + (trabalho2 * 3)) / 20

print('A média do aluno foi de', media)

if(media>7):
        print('True')
else:
        print('False')