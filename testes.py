import io
import unittest
from contextlib import redirect_stdout

import aluno as a
import turma as t


class TurmaTest(unittest.TestCase):
    def setUp(self):
        self.alunos = [
            a.Aluno("Fabio", "Teixeira", 10),
            a.Aluno("Fabiano", "Teixeira", 8),
            a.Aluno("Melissa", "Teixeira", 9),
            a.Aluno("Angela", "Teixeira", 7),
        ]
        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def testMaior(self):
        self.assertEqual(
            10,
            self.turmaObject.maiorNota.nota,
            "Erro ao encontrar maior nota",
        )
        self.assertEqual("Fabio", self.turmaObject.maiorNota.nome)

    def testMenor(self):
        self.assertEqual(
            7,
            self.turmaObject.menorNota.nota,
            "Erro ao encontrar menor nota",
        )
        self.assertEqual("Angela", self.turmaObject.menorNota.nome)

    def testIntervalo(self):
        """Todas as notas cadastradas devem estar entre 0 e 10."""
        for aluno in self.turmaObject.turma:
            with self.subTest(aluno=aluno.nome):
                self.assertGreaterEqual(aluno.nota, 0)
                self.assertLessEqual(aluno.nota, 10)

    def testNotaAbaixoDoIntervalo(self):
        with self.assertRaisesRegex(ValueError, "entre 0 e 10"):
            a.Aluno("Melissa", "Teixeira", -1)

    def testNotaAcimaDoIntervalo(self):
        with self.assertRaisesRegex(ValueError, "entre 0 e 10"):
            a.Aluno("Melissa", "Teixeira", 11)

    def testNotaDeveSerNumerica(self):
        with self.assertRaisesRegex(TypeError, "deve ser um número"):
            a.Aluno("Melissa", "Teixeira", "oito")

    def testLimitesValidosDaNota(self):
        self.assertEqual(0, a.Aluno("Nota", "Minima", 0).nota)
        self.assertEqual(10, a.Aluno("Nota", "Maxima", 10).nota)

    def testTurmaVaziaNaoTemMaiorOuMenorNota(self):
        turma_vazia = t.Turma()
        self.assertEqual([], turma_vazia.turma)
        self.assertIsNone(turma_vazia.maiorNota)
        self.assertIsNone(turma_vazia.menorNota)

    def testTurmaComUmAluno(self):
        aluno = a.Aluno("Ana", "Silva", 6)
        turma = t.Turma()
        turma.cadastrarAlunos([aluno])
        self.assertIs(turma.maiorNota, aluno)
        self.assertIs(turma.menorNota, aluno)

    def testCadastroEmMaisDeUmaChamadaAtualizaExtremos(self):
        turma = t.Turma()
        turma.cadastrarAlunos([a.Aluno("Joao", "Silva", 5)])
        turma.cadastrarAlunos([a.Aluno("Maria", "Souza", 9)])
        turma.cadastrarAlunos([a.Aluno("Pedro", "Lima", 2)])
        self.assertEqual(9, turma.maiorNota.nota)
        self.assertEqual(2, turma.menorNota.nota)
        self.assertEqual(3, len(turma.turma))

    def testMostrarAlunosExibeQuantidadeENomes(self):
        saida = io.StringIO()
        with redirect_stdout(saida):
            self.turmaObject.mostrarAlunos()
        texto = saida.getvalue()
        self.assertIn("Quantidade de alunos: 4", texto)
        self.assertIn("Fabio Teixeira", texto)
        self.assertIn("Angela Teixeira", texto)


if __name__ == "__main__":
    unittest.main(verbosity=2)
