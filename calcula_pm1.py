from decimal import Decimal

valor_total_dos_ativos = 0
quantidade_total_dos_ativos = 0

while True:
    valor_do_ativo = input("Insira o valor do ativo (ou 'Q' para sair): ").upper()
    if valor_do_ativo == 'Q':
        break
    valor_do_ativo = float(valor_do_ativo)
    quantidade_do_ativo = int(input("Insira a quantidade do ativo: "))

    valor_total_dos_ativos += valor_do_ativo * quantidade_do_ativo
    quantidade_total_dos_ativos += quantidade_do_ativo

    if quantidade_total_dos_ativos == 0:
        print("Não é possível calcular o preço médio dos ativos, quantidade total é 0")
    else:
        preco_medio = valor_total_dos_ativos / quantidade_total_dos_ativos
        preco_mediof = "{:.2f}".format(preco_medio)
        print("Preço médio dos ativos:", preco_mediof)
