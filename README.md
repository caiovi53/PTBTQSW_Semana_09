# Semana 09 — Testes unitários

Projeto simples em Python para cadastrar alunos e identificar as maiores e menores notas da turma.

## Como executar o programa

```bash
python main.py
```

## Como executar os testes

Na pasta do projeto, execute:

```bash
python -m unittest -v testes.py
```

Os testes cobrem a identificação da maior e da menor nota, o intervalo válido de notas (0 a 10), a rejeição de notas inválidas, turmas vazias ou com apenas um aluno, cadastros em chamadas separadas e a saída de `mostrarAlunos`.
