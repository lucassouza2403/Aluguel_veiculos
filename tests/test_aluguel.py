class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Veiculo:
    def __init__(self, modelo, ano, cor, preco_diaria):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco_diaria = preco_diaria
        self.disponivel = True

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def buscar_veiculo(self, modelo, ano, cor):
        for v in self.veiculos:
            if v.modelo == modelo and v.ano == ano and v.cor == cor and v.disponivel:
                return v
        return None

class Aluguel:
    def __init__(self, cliente, veiculo, dias):
        self.cliente = cliente
        self.veiculo = veiculo
        self.dias = dias
        self.valor_total = veiculo.preco_diaria * dias
        veiculo.disponivel = False

    def resumo(self):
        return f"{self.cliente.nome} alugou {self.veiculo.modelo} por {self.dias} dias. Valor: R${self.valor_total}"

def main():
    loja = Loja("AlugaCar")
    loja.adicionar_veiculo(Veiculo("Gol", 2018, "Preto", 120))
    loja.adicionar_veiculo(Veiculo("Fiat Uno", 2015, "Prata", 100))

    cliente = Cliente("Lucas", "123.456.789-00")
    veiculo = loja.buscar_veiculo("Gol", 2018, "Preto")

    if veiculo:
        aluguel = Aluguel(cliente, veiculo, 5)
        print(aluguel.resumo())
    else:
        print("Veículo não disponível.")

if __name__ == "__main__":
    main()
