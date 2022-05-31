ganhoPorHora = input('Digite o salário por hora: ')
horasTrabalhadas = int(input('Digite as horas trabalhadas: '))

salarioBruto = float(ganhoPorHora) * horasTrabalhadas

descontoInss = salarioBruto * 0.08 
descontoIr = salarioBruto*0.11 
descontoSind = salarioBruto*0.05     
salarioLiq = salarioBruto- descontoInss - descontoIr - descontoSind

print('salario bruto: ', salarioBruto)
print('desconto do INSS:', descontoInss)
print('desconto do IR', descontoIr)
print('desconto do sindicato:', descontoSind)
print('salário líquido:', salarioLiq)
