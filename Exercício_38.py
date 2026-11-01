despesas = 0
valor_total = 0

for despesas in range(1, 5):
    despesas = float(input("Qual foi o valor da sua despesa? R$ "))
    valor_total = valor_total + despesas

print(f"Valor total foi: R${valor_total}")