def menu():
    menu = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova Conta
        [lc] Listar Contas
        [ncl] Novo Cliente
        [q] Sair

        => """
    answer = input(menu)
    return answer


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    if numero_saques < limite_saque:
        if valor > saldo:
            print("Não será possível realizar a operação. Saldo insuficiente!")
        elif valor > 0:
            if valor <= limite:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque de R$ {valor:.2f}\n"
            elif valor > limite:
                print(f"Não é possível realizar saque de valor maior que {limite} por operação!")
            else:
                print("Não é possível realizar saque de valores negativos!")
        else:
            print(f"Não é possível realizar mais do que {limite_saque} por dia!")
    return (saldo, extrato)


def depositar(saldo, valor, extrato, /):
    if valor >= 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
    else:
        print("Não é possível depositar valores negativos!")

    return (saldo, extrato)


def mostrar_extrato(saldo, /, *, extrato):
    print("\n****************EXTRATO***************")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("**************************************")


def criar_cliente(clientes):
    cpf = input("Informe o número do CPF: ")
    cliente = filtrar_usuario(cpf, clientes)

    if cliente:
        print(f"Cliente com CPF {cpf} já está cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, n° bairro - cidade/uf): ")
    clientes.append({"nome": nome, "nasc": nascimento,
                    "cpf": cpf, "endr": endereco})
    print("Cliente cadastrado com sucesso!\n")


def filtrar_usuario(cpf, clientes):
    clientes_filtrados = [
        cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o número do CPF: ")
    cliente = filtrar_usuario(cpf, clientes)

    if cliente:
        print("Conta criada com sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    print("Cliente não encontrado! Fluxo de criação de conta encerrado...\n")


def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta["agencia"]}")
        print(f"Número da Conta: {conta["numero_conta"]}")
        print(f"Cliente: {conta["cliente"]["nome"]}")


def main():
    saldo = 0
    extrato = ""
    numero_saques = 0
    contas = []
    clientes = []
    LIMITE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Qual é o valor do depósito? "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Qual é o valor do saque? "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUES
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "ncl":
            criar_cliente(clientes)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    
main()
