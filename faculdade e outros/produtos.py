produtos = {}
while True:
	print("Cadastro de produtos")
	codigo = input("Digite o código do produto: ").strip()
	if codigo == "":
		print("Erro: não é permitido codigo vazio")
		continue
	if codigo in produtos:
		print("Erro: esse código já existe")
		continue
	nome = input("Digite o nome do produto: ").strip()
	if nome == "":
		print("Erro: campo nome não preenchido")
		continue
	try:
		preco = float(input("Digite o valor do produto: ").replace(",", "."))
		if preco <= 0:
			print("Erro: Preço deve ser maior que zero")
			continue
	except ValueError:
		print("Erro: digite um valor válido")
		continue
	try:
		quantidade = int(input("Digite a quantidade do produto: "))
		if quantidade < 0:
			print("Erro: Quantidade não pode ser menor que zero")
			continue
	except ValueError:
		print("Digite um número inteiro")
		continue
	total = preco * quantidade
	produtos[codigo] = {
		"nome": nome,
		"preco": preco,
		"quantidade": quantidade,
		"total": total
	}
	print("Produto cadastrado com sucesso!")
	continuar = input("Deseja cadastrar mais um produto(S/N)?").upper()
	if continuar != "S":
		break

print("---RELATÓRIO DE ESTOQUE---")
valor_geral = 0
for codigo, produto in produtos.items():
	print(f"\nCódigo: {codigo}")
	print(f'\nNome: {produto["nome"]}')
	print(f'\nPreço: R${produto["preco"]:.2f}')
	print(f'\nQuantidade: {produto["quantidade"]}')
	print(f'\nTotal: {produto["total"]:.2f}')
	valor_geral += produto["total"]
print(f"\nValor geral do estoque: R${valor_geral:.2f}")