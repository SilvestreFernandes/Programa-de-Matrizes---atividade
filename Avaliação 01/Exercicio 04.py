SI = int(input("Qual seu saldo inicial? "))
if (SI < 0):
    print("Saldo inicial inválido.")
    SI = int(input("Qual seu saldo inicial? Tem que ser um valor positivo. "))
    if (SI < 0):
        print("Saldo inicial inválido. O programa será encerrado.")
        exit()

while True:
    print ("1. Consultar saldo")
    print ("2. Sacar valor")
    print ("3. Depositar valor")
    print ("4. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if (opcao == 1):
        print("Seu saldo é: R$ ", SI)
    elif (opcao == 2):
        valor_saque = int(input("Digite o valor que deseja sacar: "))
        if (valor_saque > SI):
            print("Saldo insuficiente para realizar o saque.")
        else:
            SI -= valor_saque
            print("Saque realizado com sucesso. Seu novo saldo é: R$ ", SI)
    elif (opcao == 3):
        valor_deposito = int(input("Digite o valor que deseja depositar: "))
        SI += valor_deposito
        print("Depósito realizado com sucesso. Seu novo saldo é: R$ ", SI)
    elif (opcao == 4):
        print("Obrigado por utilizar nosso serviço.")
        break
    else:
        print("Opção inválida. Tente novamente.")
