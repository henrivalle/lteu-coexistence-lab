# LTE-U Coexistence Lab

[English](README.md)

Explore como uma meta de disponibilidade observada afeta o número de slots de espectro não licenciado que um sistema LTE-U simulado pode planejar usar. O laboratório estima uma capacidade por canal a partir de um CSV com observações de slots livres. A execução usa a biblioteca padrão do Python 3.9 ou posterior.

Para contribuir, escolha uma [tarefa para iniciantes](https://github.com/henrivalle/lteu-coexistence-lab/contribute) e execute a verificação rápida no [guia de contribuição](CONTRIBUTING.md).

```bash
python3 -m lteu_lab examples/synthetic.csv --target 80
python3 -m lteu_lab examples/synthetic.csv --target 95
python3 -m unittest discover -s tests -v
```

A primeira execução retorna dois slots no `lab-a` e cinco no `lab-b`, ambos disponíveis em quatro de cinco observações. Com a meta de 95%, cinco de cinco observações precisam sustentar a estimativa, que cai para zero e um slot, respectivamente. Compare os resultados e discuta o que mudaria com uma amostra maior.

## Entrada e interpretação

O CSV tem as colunas `channel` e `free_slots`. Cada linha é uma observação de mesmo peso para um canal. Os rótulos de canal aceitam até 64 letras e dígitos ASCII, sublinhados, pontos ou hífens e começam por letra ou dígito. Os slots livres são inteiros não negativos. A meta é um percentual inteiro de 1 a 100, com padrão de 90.

Para cada canal, o programa estima a maior quantidade inteira de slots que pelo menos o percentual-alvo de observações sustenta. A saída traz os slots, a quantidade de observações que os sustentam, o tamanho da amostra e a meta. A estimativa descreve a amostra de cada canal individualmente. Ela não mede a disponibilidade conjunta dos canais nem garante disponibilidade futura.

## Contexto da pesquisa

O laboratório usa uma ideia simplificada da pesquisa pública da UFG sobre coexistência LTE-U e alocação estocástica de recursos. A implementação e os exemplos foram escritos para este projeto. O modelo completo da pesquisa inclui decisões sobre demanda de usuários e custos de infraestrutura. [Dissertação da UFG](https://repositorio.bc.ufg.br/tede/items/c5e3a766-3108-4456-8739-180398accbea) · [Artigo do SBRC](https://doi.org/10.5753/sbrc.2018.2459)

O código está disponível sob a licença [MIT](LICENSE). Ao reportar um problema, inclua o comando, a versão do Python e um CSV sintético pequeno.
