faturamento_mensal = 0 
meses = 0
total_faturado = 0

for meses in range(1, 7):
    faturamento_mensal = float(input("Quanto você faturou esse mês? R$ "))
    total_faturado = total_faturado + faturamento_mensal
    média_mensal = total_faturado / meses
print(f"O faturamento médio mensal foi: R${média_mensal}")