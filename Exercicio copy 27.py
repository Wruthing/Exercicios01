# Solicita a quantidade de morangos e maçãs ao usuário
quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

# Calcula o preço dos morangos de acordo com a quantidade
if quantidade_morangos <= 5:
    preco_morangos = 2.50
else:
    preco_morangos = 2.20

# Calcula o preço das maçãs de acordo com a quantidade
if quantidade_macas <= 5:
    preco_macas = 1.80
else:
    preco_macas = 1.50

# Calcula o valor total da compra
valor_total = (quantidade_morangos * preco_morangos) + (quantidade_macas * preco_macas)

# Verifica se o cliente recebe o desconto
if quantidade_morangos + quantidade_macas > 8 or valor_total > 25.00:
    desconto = valor_total * 0.10
else:
    desconto = 0

# Calcula o valor a ser pago pelo cliente
valor_a_pagar = valor_total - desconto

# Exibe o valor a ser pago
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
