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
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade < 0:
                print("quantidade não pode ser negativa")
                return
        except ValueError:
            print("valores inválidos")
            return
        produto = Produto(codigo, nome, preco, quantidade) #cada "produto" vai receber um objeto
            #basicamente passamos todas as variaveis acima para dentro dos parametros da class, e guardamos esse essa geração de objeto dentro da variavel produto.
            # 
            # Aqui, cada objeto será guardado no dicionario produtos criado lá encima, tendo o "codigo" como primary key 
        self.produtos[codigo] = produto #esse [codigo] significa que ele é a "primary key"
        print("Produto cadastrado!")
    def consultar(self):
        codigo = int(input("Digite o código que deseja consultar: ").strip())
        if codigo == "":
            print("Não foi digitado nenhum código")
            return
        if not codigo:
            print("Esse código não existe. produto nâo encontrado")
            return
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            print(f"Produto: {produto.nome}")
            print(f"Preço: R${produto.preco}")
            print(f"Quantidade: {produto.quantidade}")
            print(f"Total: {produto.calcularTotal():.2f}")
    def relatorio(self):
        print("<====RELATÓRIO DO ESTOQUE====>")
        valorGeral = 0
        for codigo, produto in self.produtos.items():
            total = self.produto.calcularTotal()
            print(f"Código: {codigo}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: {produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")
            print(f"Total: {total:.2f}")
            valorGeral += total
        print(f"Valor geral do estoque: {valorGeral:.2f}")
estoque = Estoque()
while True:  #enquanto for  verdade, só vai parar quando tiver um break
    print("<====MENU====>")  
    print("1 -- Cadastrar produto")
    print("2 -- Consultar produto")
    print("3 -- Relatório")
    print("4 - Terminar")
    opcao = input("Qual opção deseja escolher: ")
    if opcao == "1":
        estoque.cadastrar()
    elif opcao == "2":
        estoque.consultar()
    elif opcao == "3":
        estoque.relatorio()
    elif opcao == "4":
        print("Programa encerrado")
        break
    else:
        print("opção inválida")