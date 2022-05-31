palindromo = ' !subi no onibus!?? ! '
x = ""
y = ""
z = "!?@, "
palindromo = palindromo.lower()
mytable = palindromo.maketrans(x, y, z)
palindromo = palindromo.translate(mytable)
inverso = palindromo[::-1]
print(inverso == palindromo)
#return palindromo == inverso