

class Conta:
    def __init__(self, numero, titular="Clara Fernandes", saldo=0.0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    def extrato(self):
        return f"Conta: {self._numero} | Titular: {self._titular} | Saldo: R${self._saldo:.2f}"

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return (
            "Dados da Conta:\nNúmero: {}\nTitular: {}\nSaldo: R${:.2f}\nLimite: R${:.2f}"
            .format(self._numero, self._titular, self._saldo, self._limite)
        )


class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0.0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        print("----- Atualizando Conta -----")
        print("Titular:", conta._titular)
        print("Saldo anterior: R${:.2f}".format(conta.saldo))
        conta.atualiza(self._selic)
        print("Saldo após atualização: R${:.2f}".format(conta.saldo))
        self._saldo_total += conta.saldo
        print("-----------------------------\n")


if __name__ == '__main__':
    c = Conta('123-4', 'Felipe Ramos', 1000.0)
    cc = ContaCorrente('123-5', 'Beatriz Costa', 1000.0)
    cp = ContaPoupanca('123-6', 'Renato Lima', 1000.0)

    atualizador = AtualizadorDeContas(selic=0.01)
    atualizador.roda(c)
    atualizador.roda(cc)
