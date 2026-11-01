valor_vendas = 0
valor_total = 0
valores_acima = 0

for valor_vendas in range(5):
    valor_vendas = float(input("Qual foi o valor da venda? R$ "))
    valor_total = valor_total + valor_vendas
    if valor_total > 500:
        valores_acima += 1
    else:
        valores_acima = valores_acima
print(f"O total foi: R${valor_total}. Valores acima: {valores_acima}")