print("Qual tipo de atendimento deseja solicitar?")
print("1 - Troca")
print("2 - Devolução")
print("3 - Suporte")
print("")
atendimento =  int(input("Digite o número: "))

match atendimento:
    case 1:
        print("")
        print("Solicitando seu atendimento, um instante...")
    case 2:
        print("")
        print("Solicitando seu atendimento, um instante...")
    case 3:
        print("")
        print("Solicitando seu atendimento, um instante...")
    case _:
        print("")
        print("Opção inválida!")