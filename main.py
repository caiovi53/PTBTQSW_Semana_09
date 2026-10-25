import aluno as a
import turma as t


def main():
    alunos = [
        a.Aluno("Fabio", "Teixeira", 10),
        a.Aluno("Fabiano", "Teixeira", 8),
        a.Aluno("Melissa", "Teixeira", 9),
        a.Aluno("Angela", "Teixeira", 7),
    ]

    turma_object = t.Turma()
    turma_object.cadastrarAlunos(alunos)

    turma_object.mostrarAlunos()
    print("*" * 30)
    print("Aluno com menor nota:", turma_object.menorNota.mostrarAluno())
    print("Aluno com maior nota:", turma_object.maiorNota.mostrarAluno())


if __name__ == "__main__":
    main()
