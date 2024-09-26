def menu():
    menu_text = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """
    return input(menu_text)


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(saldo, valor, extrato, numero_saques, /):
    if valor > saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
    elif valor > limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif numero_saques >= LIMITE_SAQUES:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato, numero_saques):
    total_saques_restantes = LIMITE_SAQUES - numero_saques
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"Saques restantes: {total_saques_restantes}")
    print("==============================")

# Loop do menu
while True:
    opcao = menu()

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor_deposito, extrato)
        
    elif opcao == "s":
        valor_sacar = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo, valor_sacar, extrato, numero_saques)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato, numero_saques)

    elif opcao == "q":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
