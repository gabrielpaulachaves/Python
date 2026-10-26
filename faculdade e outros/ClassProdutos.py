class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def calcularTotal(self):
        return self.preco * self.quantidade 
class Estoque:
    def __init__(self):
        self.produtos = {}
    def cadastrar(self):
        print("<====Cadastro de produto====>")
        codigo = input("Digite o codigo do produto: ").strip()
        if codigo == "":
            print("Código vazio")
            return 
        if codigo in self.produtos:
            print("Esse código já existe")
            return
        nome = input("Nome: ").strip()
        if  nome == "":
            print("nome vazio")
            return
        try:
            preco = float(input("Digite o valor: ").replace(",", "."))
            if preco < 0:
                print("Valor não pode ser menor que 0")
                return
            quantidade = int(input("Digite a quantidade do produto"))
            if quantidade < 0:
                print("quantidade não pode ser negativa")
                return
        except ValueError:
            print("valors inválidos")
            return
        produto = Produto(codigo, nome, preco, quantidade)
        self.produtos[codigo] = produto
        print("Produto cadastrado!")
    