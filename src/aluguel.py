
#Definindo as classes do meu prejetoe ele contem: cliente, veiculo, loja e aluguel.
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Veiculo:
    def __init__(self, modelo, cor, ano, preco_diaria):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco_diaria = preco_diaria
        self.disponivel = True

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

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
    loja = Loja("LocarCar")

    # Adicionando veículos
    loja.adicionar_veiculo(Veiculo("Polo", "Branco", 2020, 120))
    loja.adicionar_veiculo(Veiculo("Onix", "Preto", 2022, 150))
    loja.adicionar_veiculo(Veiculo("T-Cross", "Azul", 2025, 220))
    loja.adicionar_veiculo(Veiculo("Nivus", "Prata", 2025, 250))
    loja.adicionar_veiculo(Veiculo("BYD", "Branco", 2024, 300))
    loja.adicionar_veiculo(Veiculo("Onix Plus", "Preto", 2024, 240))
    loja.adicionar_veiculo(Veiculo("Gol", "Cinza", 2024, 150))
    loja.adicionar_veiculo(Veiculo("HB20", "Azul", 2023, 140))
    loja.adicionar_veiculo(Veiculo("Corolla", "Prata", 2022, 450))
    loja.adicionar_veiculo(Veiculo("Honda Civic", "Vermelho", 2026, 450))

    print("Bem-vindo à LocarCar!")
    print("Aqui você pode escolher o veículo desejado.\n")

    while True:
        print("\nCatálogo de veículos:")
        for i, v in enumerate(loja.veiculos, start=1):
            status = "Disponível" if v.disponivel else "Indisponível"
            print(f"{i}. {v.modelo} ({v.ano}, {v.cor}) - R${v.preco_diaria}/dia [{status}]")

        try: 
            escolha = int(input("\nDigite o número do veículo desejado (ou 0 para sair): "))
            if escolha == 0:
                print("Encerrar atendimento.")
                break
            if escolha < 1 or escolha > len(loja.veiculos):
                print("Opção inválida, tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida, digite apenas números.")
            continue

        veiculo = loja.veiculos[escolha - 1]
        if not veiculo.disponivel:
            print("Esse veículo já foi alugado, escolha outro.")
            continue

        dias = int(input("Quantos dias deseja alugar? "))
        cliente = Cliente(input("Nome do cliente: "), input("CPF do cliente: "))

        aluguel = Aluguel(cliente, veiculo, dias)
        print(aluguel.resumo())

        continuar = input("\nAtender outro cliente? (s/n): ")
        if continuar.lower() != "s":
            print("Obrigado por escolher a LocarCar, Obrigado e volte sempre.")
        
            break

if __name__ == "__main__":
    main()






        
        







    
          
    










        

        









        