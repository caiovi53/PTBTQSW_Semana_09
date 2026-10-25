class Aluno:
    """Representa um aluno e sua nota."""

    def __init__(self, nome, sobrenome, nota):
        if isinstance(nota, bool) or not isinstance(nota, (int, float)):
            raise TypeError("A nota deve ser um número.")
        if not 0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")

        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrarAluno(self):
        """Retorna os dados do aluno em formato textual."""
        return f"Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota}"
