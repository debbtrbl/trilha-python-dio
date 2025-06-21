class Pedido:
    def __init__(self):
        self.itens = []  
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    def adicionar_item(self, nome, preco):
        # TODO: Adicione o preço do item à lista:
        self.itens.append({"nome": nome, "preco": preco})

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    def calcular_total(self):
      soma = 0
      for item in self.itens:
        soma += item["preco"] 
        # TODO: Retorne a soma de todos os preços
      return soma
        

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    preco = float(preco)
    
    #TODO: Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(nome, preco)
# TODO: Exiba o total formatado com duas casas decimais:
print(f"{pedido.calcular_total():.2f}")