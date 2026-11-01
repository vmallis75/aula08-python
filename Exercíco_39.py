valor_venda = 0
valor_total = 0
continuar = "sim"

while continuar == "sim":
    valor_venda = float(input("Qual o valor da sua venda? R$ "))
    valor_total = valor_total + valor_venda
    continuar = input("Registrar outra venda? (sim/nao):").lower()
print(f"O valor total registrado das suas vendas foi: R${valor_total}")