class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            print(f'Depósito de R${quantia:.2f} realizado com sucesso.')
        else:
            print('Quantia para depósito deve ser positiva.')

    def sacar(self, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            print(f'Saque de R${quantia:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou quantia inválida para saque.')

    def verificar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

# Exemplo de uso da classe ContaBancaria

# Criação de uma nova conta bancária
conta = ContaBancaria('João Silva', 1000)

# Verificar o saldo inicial
conta.verificar_saldo()

# Realizar um depósito
conta.depositar(500)

# Verificar o saldo após o depósito
conta.verificar_saldo()

# Realizar um saque
conta.sacar(200)

# Verificar o saldo após o saque
conta.verificar_saldo()

# Tentar sacar uma quantia maior que o saldo
conta.sacar(2000)

# Tentar depositar uma quantia negativa
conta.depositar(-100)
