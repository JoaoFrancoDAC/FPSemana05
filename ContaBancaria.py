class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, valor):
        if valor > 0:
            if self.limite < 500:
                diferenca = 500 - self.limite

                if valor <= diferenca:
                    self.limite += valor

                else:
                    self.limite = 500
                    self.saldo += valor - diferenca

            else:
                self.saldo += valor
            print(1)

        else:
            print(0)
    
    def levantar(self, valor):
        if valor <= (self.saldo + self.limite) and valor > 0:
            if valor <= self.saldo:
                # Se o valor é menor ou igual ao saldo, apenas subtrai do saldo
                self.saldo -= valor
            else:
                # Se o valor é maior que o saldo, usa o limite
                diferenca = valor - self.saldo
                self.saldo = 0
                self.limite -= diferenca
            print(1)
        else:
            print(0)
    
    def exibir_saldo(self):
        print(f"{self.saldo:.2f}")
    
    def exibir_info(self):
        print(f"[{self.titular}] [{self.saldo:.2f}] [{self.limite}]")

ContaJoao = ContaBancaria("João", 1000, 500)

ContaJoao.exibir_info()
ContaJoao.levantar(1200)
ContaJoao.exibir_info()
ContaJoao.levantar(300)
ContaJoao.exibir_info()

ContaJoao.depositar(200)
ContaJoao.exibir_info()
ContaJoao.depositar(400)
ContaJoao.exibir_info()
ContaJoao.depositar(-50)
ContaJoao.levantar(-50)
ContaJoao.levantar(0)
