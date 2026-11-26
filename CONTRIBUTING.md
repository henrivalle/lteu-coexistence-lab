# Contributing / Como contribuir

Pick a [beginner task](https://github.com/henrivalle/lteu-coexistence-lab/contribute) and use Python 3.9 or newer. Issues and pull requests are welcome in English and Portuguese.

Escolha uma [tarefa para iniciantes](https://github.com/henrivalle/lteu-coexistence-lab/contribute) e use Python 3.9 ou posterior. Issues e pull requests são bem-vindos em inglês e português.

## First check / Primeira verificação

Run from the repository root. Execute na raiz do repositório.

```bash
python3 -m lteu_lab examples/synthetic.csv --target 80
python3 -m unittest discover -s tests -v
```

The first command reports two slots for `lab-a` and five for `lab-b`. When changing an example, update both READMEs and include the command and expected output in the PR. Use synthetic data and link the issue if the PR addresses one.

O primeiro comando retorna dois slots para `lab-a` e cinco para `lab-b`. Ao mudar um exemplo, atualize os dois READMEs e inclua no PR o comando e a saída esperada. Use dados sintéticos e vincule a issue se o PR resolver uma.
