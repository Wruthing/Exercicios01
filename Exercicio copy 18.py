# Solicita ao usuário um número inteiro menor que 1000
numero = int(input("Digite um número inteiro menor que 1000: "))

# Verifica se o número está dentro do intervalo permitido
if numero < 0 or numero >= 1000:
    print("Número fora do intervalo permitido.")
else:
    # Calcula as centenas, dezenas e unidades
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    # Cria as strings para os termos no plural, se necessário
    str_centenas = f"{centenas} centena{'s' if centenas > 1 else ''}"
    str_dezenas = f"{dezenas} dezena{'s' if dezenas > 1 else ''}"
    str_unidades = f"{unidades} unidade{'s' if unidades > 1 else ''}"

    # Constrói a mensagem final
    mensagem = ""

    if centenas > 0:
        mensagem += str_centenas

    if dezenas > 0:
        if centenas > 0:
            if unidades > 0:
                mensagem += ", "
            else:
                mensagem += " e "
        mensagem += str_dezenas

    if unidades > 0:
        if centenas > 0 or dezenas > 0:
            mensagem += " e "
        mensagem += str_unidades

    print(f"{numero} = {mensagem}")
