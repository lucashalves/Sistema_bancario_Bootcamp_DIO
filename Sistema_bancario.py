menu = """
=-=-=-=-=-=- BANCO BANCÁRIO =-=-=-=-=-=-

Seja bem-vindo(a)!

[S] Saque
[D] Depósito
[L] Saldo na tela
[E] Extrato
[Q] Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

extrato = ""
LIMITE_SAQUE = 3
qtd_saque = 0
limite_valor = 500
saldo_conta = 0

while True:
    print(menu)
    operacao = input("Selecione a operação desejada: ").upper().strip()
    print()
    if operacao == 'S':
        print()
        print('=-=-=-=-=-=- SAQUE =-=-=-=-=-=-')    
        if qtd_saque < LIMITE_SAQUE:
            valor_saque = int(input('Qual o valor você deseja sacar? R$ '))
            if valor_saque <= saldo_conta and valor_saque < limite_valor:
                qtd_saque += 1
                print(f'Saque Realizado com sucesso! Retire as notas na boca do caixa!')
                print(f'Você ainda pode sacar mais {LIMITE_SAQUE - qtd_saque} vezes hoje')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
                saldo_conta -= valor_saque
                extrato += f'SAQUE: R${valor_saque:.2f}\n'                
            else:
                print('Não foi possível realizar essa operação! Favor Verificar seu saldo!')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        else:
            print('Você já realizou o limite diário de saque.')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif operacao == 'D':
        print()
        print('=-=-=-=-=-=- DEPÓSITO =-=-=-=-=-=-')
        valor_deposito = int(input('Qual o valor você deseja depositar? R$'))
        if valor_deposito > 0:
            print(f'Você despositou R${valor_deposito:.2f}')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            extrato += f'DEPÓSITO: R$ {valor_deposito:.2f}\n'
            saldo_conta += valor_deposito
        else:
            print(f'Não é possível depositar: R${valor_deposito}')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif operacao == 'L':
        print()
        print('=-=-=-=-=-=- SALDO NA TELA =-=-=-=-=-=-')
        print(f'Seu saldo é {saldo_conta:.2f}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif operacao == 'E':
        print()
        print('=-=-=-=-=-=- EXTRATO =-=-=-=-=-=-')
        if not extrato:
            print('Nenhuma operação realizada')
        else:
            print(f'{extrato}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif operacao == 'Q':
        print()
        print('Obrigado por usar nosso banco, até logo!')
        print()
        break
    else:
        print('***ERRO*** Por favor digite o comando corretamente!')
    