"""[LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. 
Utilize um loop 'for' para iterar sobre os alunos e suas notas.

Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando 
que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

Ao final, exiba a média geral da turma."""

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():

    num_alunos = int(input("Digite o número de alunos: "))
    
    total_media = 0
    alunos_aprovados = 0
    alunos_reprovados = 0

    for _ in range(num_alunos):

        nome = input("Digite o nome do aluno: ")
        notas = []
        for i in range(1, 4):
            nota = float(input(f"Digite a {i}ª nota do aluno: "))
            notas.append(nota)
        

        media = calcular_media(notas)
        
 
        status = "Aprovado" if media >= 7.0 else "Reprovado"
        
        # Exibe o resultado do aluno
        print(f"\nAluno: {nome}")
        print(f"Notas: {notas}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")
        print("-" * 30)
        

        total_media += media

        if status == "Aprovado":
            alunos_aprovados += 1
        else:
            alunos_reprovados += 1
    

    media_geral = total_media / num_alunos
    print(f"\nMédia geral da turma: {media_geral:.2f}")
    print(f"Alunos aprovados: {alunos_aprovados}")
    print(f"Alunos reprovados: {alunos_reprovados}")


main()
