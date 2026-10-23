class Aluno: #class é como uma planta (molde) de uma casa, ela cria objetos (que são as casas) a partir dela
    def __init__(self, nome, nota1, nota2): #self é tipo o this no javascript, significa "esse objeto aqui". 
        self.nome = nome  #o self aqui significa que cada objeto terá uma propriedade chamada "nome". self é tipo uma gaveta do objeto. Pega o valor que ta de passagem e guarda no objeto. sem o self o dado sumiria
        self.nota1 = nota1 
        self.nota2 = nota2

    def calcular_media(self): #esse self serve para a funcao acessar os objetos
        return (self.nota1 + self.nota2) / 2

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "aprovado"
        elif media >= 4:
            return "exame final"
        else:
            return "reprovado"

    def exibir_resultado(self):
        print(f"aluno: {self.nome}")
        print(f"Média: {self.calcular_media():.1f}")
        print(f"Situação: {self.verificar_situacao()}")

if __name__ == "__main__": #significa que o código abaixo só vai rodar se o arquivo for executado diretamente, e não importado
    quantidade = int(input("Quantos alunos deseja cadastrar? "))
for i in range(quantidade):
    print(f"\nAluno {i + 1}")
    nome = input("nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    aluno = Aluno(nome, nota1, nota2)    
    aluno.exibir_resultado()


   