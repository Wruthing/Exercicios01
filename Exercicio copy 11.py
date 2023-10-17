# Solicita o salário atual do colaborador
salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

# Calcula o percentual de aumento com base no salário atual
if salario_atual <= 280.00:
    percentual_aumento = 20
elif salario_atual <= 700.00:
    percentual_aumento = 15
elif salario_atual <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

# Calcula o valor do aumento
valor_aumento = (salario_atual * percentual_aumento) / 100

# Calcula o novo salário após o aumento
novo_salario = salario_atual + valor_aumento

# Exibe as informações
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
