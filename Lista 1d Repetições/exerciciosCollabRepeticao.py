# Dado o seguinte conjunto de valores, correspondente a compras de uma pessoa  
# no mercado, escreva o código que encontre as respostas pedidas.
# Observação: utilize a estrutura for em todas as soluções, mesmo quando for
# possível obtê-las de outra forma. Nosso objetivo aqui é exercitar o uso do for.
compra = [10.00, 15.50, 4.50, 3.50, 7.50, 1.50, 5.50, 4.50, 3.50, 1.50, 18.50]

# 1- Qual foi o valor total da compra?

valorTotal = 0
for i in compra:
    valorTotal += i
print("O valor total foi de ", valorTotal)
# 2- Quantos items custam 10 reais ou mais?

quantDeItensAcimaDe10 = 0
for i in compra:
    if i>=10:
        quantDeItensAcimaDe10 += 1
print("A quantidade de itens que custam mais de 10 são ", quantDeItensAcimaDe10)

# 3- Qual a soma dos valores dos itens que custam 5 reais ou menos?

quantDeItensAbaixoDe5 = 0
for i in compra:
    if i<=10:
        quantDeItensAbaixoDe5 += 1
print("A quantidade de itens que custam menos que 5 são ", quantDeItensAbaixoDe5)
