class Turma:
    """Armazena alunos e acompanha as maiores e menores notas."""

    def __init__(self):
        self.turma = []
        self.menorNota = None
        self.maiorNota = None

    def cadastrarAlunos(self, alunos):
        """Cadastra alunos e recalcula as notas extremas da turma."""
        novos_alunos = list(alunos)
        self.turma.extend(novos_alunos)

        if self.turma:
            self.menorNota = min(self.turma, key=lambda aluno: aluno.nota)
            self.maiorNota = max(self.turma, key=lambda aluno: aluno.nota)

    def mostrarAlunos(self):
        """Exibe a quantidade de alunos e os dados de cada um."""
        print("Quantidade de alunos:", len(self.turma))
        for aluno in self.turma:
            print(aluno.mostrarAluno())
