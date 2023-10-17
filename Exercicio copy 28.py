# Solicita o tipo de carne e a quantidade ao usuário
tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
quantidade = float(input("Digite a quantidade em Kg: "))

# Verifica o preço de acordo com a quantidade
if quantidade <= 5:
    if tipo_carne == "File Duplo":
        preco_por_kg = 4.90
    elif tipo_carne == "Alcatra":
        preco_por_kg = 5.90
    elif tipo_carne == "Picanha":
        preco_por_kg = 6.90
    else:
        print("Tipo de carne inválido.")
        exit()
else:
    if tipo_carne == "File Duplo":
        preco_por_kg = 5.80
    elif tipo_carne == "Alcatra":
        preco_por_kg = 6.80
    elif tipo_carne == "Picanha":
        preco_por_kg = 7.80
    else:
        print("Tipo de carne inválido.")
        exit()

# Calcula o valor da compra
valor_total = quantidade * preco_por_kg

# Verifica se a compra será feita no cartão Tabajara
cartao_tabajara = input("A compra será feita no cartão Tabajara? (S/N): ").strip().lower()
if cartao_tabajara == "s":
    desconto = valor_total * 0.05
else:
    desconto = 0

# Calcula o valor a pagar
valor_a_pagar = valor_total - desconto

# Exibe o cupom fiscal
print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço por Kg: R$ {preco_por_kg:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if cartao_tabajara == 's' else 'Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
