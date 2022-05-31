texto = "fisl2013"
x = "aegisto"
y = "4391570"
table = {'A' : '4',
        'a':'4',
        'G':'9',
        'g':'9',
        'S':'5',
        's':'5',
        'O':'0',
        'o':'0',
        'E':'3',
        'e':'3',
        'I':'1',
        'i':'1',
        'T':'7',
        't':'7'}

mytable = texto.maketrans(table)
print(texto.translate(mytable))