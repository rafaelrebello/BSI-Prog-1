entrada = "Testando um valor de entrAda abcde"
entrada = entrada.lower()
mytable = entrada.maketrans("aeiou", "AEIOU")
print(entrada.translate(mytable))