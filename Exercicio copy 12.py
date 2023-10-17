# Solicita o valor da hora e a quantidade de horas trabalhadas ao usuário
valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcula o desconto do Imposto de Renda
if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20

# Calcula o desconto do INSS
desconto_inss = salario_bruto * 0.10

# Calcula o FGTS
fgts = salario_bruto * 0.11

# Calcula o total de descontos
total_descontos = desconto_ir + desconto_inss

# Calcula o salário líquido
salario_liquido = salario_bruto - total_descontos

# Exibe as informações
print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas})        : R$ {salario_bruto:.2f}")
print(f"(-) IR ({'5%' if salario_bruto <= 1500 else '10%' if salario_bruto <= 2500 else '20%'})                     : R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%)                 : R$ {desconto_inss:.2f}")
print(f"FGTS (11%)                      : R$ {fgts:.2f}")
print(f"Total de descontos              : R$ {total_descontos:.2f}")
print(f"Salário Líquido                 : R$ {salario_liquido:.2f}")
