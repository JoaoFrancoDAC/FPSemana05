import argparse

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
                
                self.saldo -= valor
            else:
                
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerir Uma Conta Bancária")
    parser.add_argument(
        "-A",
        "--acao",
        required=True,
        choices=["depositar", "levantar", "saldo", "info"],
        help="Ação a Executar",
    )
    parser.add_argument(
        "-V", "--valor", type=float, help="Valor para Depositar ou Levantar"
    )
    args = parser.parse_args()

    conta = ContaBancaria("Carlos", 500.0, 100.0)

    if args.acao == "depositar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Depositar.")
        else:
            conta.depositar(args.valor)
    elif args.acao == "levantar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Levantar (-v VALOR).")
        else:
            conta.levantar(args.valor)
    elif args.acao == "saldo":
        conta.exibir_saldo()
    elif args.acao == "info":
        conta.exibir_info()
