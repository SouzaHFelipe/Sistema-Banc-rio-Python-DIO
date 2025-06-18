menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        deposito_valor = int(input('Qual o valor do deposito : '))

        if deposito_valor >= limite or deposito_valor <= -1:
            print('Valor invalido')
        

        else:            
            saldo += deposito_valor
            extrato += "\nDeposito realizado R$ " + str(deposito_valor)


            print(f'saldo atualizado R${saldo:.2f} ')
        
    elif opcao == "s":
        
        saque_valor = int(input('Qual o valor do saque : '))
        
        if saldo <= saque_valor:
            print('Sem saldo')
        elif numero_saques == LIMITE_SAQUES:
            print('Limite de saques ja realizado hoje')
        
        else:
            saldo -= saque_valor
            extrato += '\nSaque Realizado R$ ' + str(saque_valor)
            numero_saques += 1
 
            print(f'R${saldo:.2f}')
        
        

    elif opcao == "e":
        n = str('\n')
        print(f'Seu extrato {n + extrato}')
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")