class Produto:
    def __init__(self, codigo, nome, preco, quantidade): #sem o def __init__, precisariamos criar as propriedades manualmente
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def calculartotal(self):
        return self.preco * self.quantidade 
class Estoque:
    def __init__(self):
        self.produtos = {}
    def cadastrar(self):
        print("<====Cadastro de produto====>")
        try:
            codigo = int(input("Digite o codigo do produto: ").strip())
        except ValueError:
                print("valor inválido")
                return
        if codigo in self.produtos:
            print("Esse código já existe")
            return
        nome = input("Nome: ").strip()
        if  nome == "":
            print("nome vazio")
            return
        try:  #usamos try e except com float e int
            preco = float(input("Digite o valor: ").replace(",", "."))
            if preco < 0:
                print("Valor não pode ser menor que 0")
                return
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade < 0:
                print("quantidade não pode ser negativa")
                return
        except ValueError:
            print("Preço deve ser número")
            return
        produto = Produto(codigo, nome, preco, quantidade) #cada "produto" vai receber um objeto
            #basicamente passamos todas as variaveis acima para dentro dos parametros da class, e guardamos essa geração de objeto dentro da variavel produto.
            #duvida: como que cada produto vai receber um objeto? por tras da logica, nao criamos apenas uma vez a variavel produto? R: essa variavel produto muda de valor toda vez que chamamos essa funcao, para nao perdermos os valores anteriores, a gente guarda no objeto self.produtos
            #logo depois de guardar o objeto criado pela class, guardamos essa variavel no self.produtos[codigo], pois a variavel "produto" mudará de valor quando cadastrarmos um novo produto. É tipo uma variavel de transferencia rapida, só guarda por um curto periodo e ja passa pro dicionario.

            #"entao eu posso criar varias vezes um produto com o mesmo codigo, já que o produto será resetado". Não, pois fazemos uma verificação lá encima com uma condição que verifica se o codigo já existe

            # Aqui, cada objeto será guardado no dicionario produtos criado lá encima, tendo o "codigo" como primary key 
         
        self.produtos[codigo] = produto #esse [codigo] é o que vai buscar o objeto baseado no codigo
        print("Produto cadastrado!")
    def consultar(self):
        try:
            codigo = int(input("Digite o código que deseja consultar: ").strip()) 
        except ValueError:
            print("Digite um código válido")
            return
        if codigo in self.produtos:
            produto = self.produtos[codigo] #produto igual a self.produtos[codigo digitado acima]
            print(f"Produto: {produto.nome}")
            print(f"Preço: R${produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")
            print(f"Total: {produto.calculartotal():.2f}")
        else:
            print("Produto não encontrado")
    def relatorio(self):
        print("<====RELATÓRIO DO ESTOQUE====>")
        valorgeral = 0
        for codigo, produto in self.produtos.items():
            total = produto.calculartotal()
            print(f"Código: {codigo}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: {produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")
            print(f"Total: {total:.2f}")
            valorgeral += total
        print(f"Valor geral do estoque: {valorgeral:.2f}")
estoque = Estoque()  #vai servir para chamarmos os metodos no menu. Ele guarda dados e regras
 #só precisamos de apenas um estoque, dentro do estoque guardaremos outros objetos.
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

        #duvida: ao criar uma class, ela já nao cria um objeto? a gente está criando a class Estoque apenas para criar um dicionario vazio e guardar esses objetos criados no class Produto? Não, criamos a class Estoque para criarmos as regras (metodos)
        #duvida: o dicionario produtos está dentro da class Estoque, entao como acessamos? pois os metodos sao executados uma vez só.