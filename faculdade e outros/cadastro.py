cadastro = {}
quantidade = int(input("Quantas pessoas deseja cadastrar?: "))
for i in range(quantidade):
    print(f"Cadastro: {i +1}")
    codigo = input("Codigo da pessoa: ")
    nome = input("Nome da pessoa: ")
    idade = int(input("Idade da pessoa: "))
    cidade = input("cidade da pessoa: ")

    cadastro[codigo] = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

print("\n----Cadastros----")
for codigo, dados in cadastro.items():
    print(f"\nCódigo: {codigo}")
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']}")
    print(f"Cidade: {dados['cidade']}")


    