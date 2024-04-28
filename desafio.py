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
    return (saldo,extrato)

def depositar(saldo, valor, extrato, /):
    if valor >= 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
    else:
        print("Não é possível depositar valores negativos!")

    return (saldo,extrato)

def mostrar_extrato(saldo, /, *, extrato):
    print("\n****************EXTRATO***************")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("**************************************")

# def criar_cliente():

# def criar_conta():


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
        
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()