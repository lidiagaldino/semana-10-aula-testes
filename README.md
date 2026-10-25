# Semana 10 — Conversão de números romanos

Programa em Python que converte um numeral romano em um inteiro.
Usa apenas a biblioteca padrão. Os testes são feitos com PyUnit (`unittest`).

## Executar o exemplo

```bash
python main.py
```

Resultado esperado: `24`.

## Executar os testes

```bash
python -m unittest discover -v
```

Alternativamente: `python test_numeroromano.py`.

## Casos solicitados e diagnóstico

| Numeral | Esperado | Resultado original | Após correção |
| --- | ---: | ---: | ---: |
| I | 1 | 1 | 1 |
| V | 5 | 5 | 5 |
| II | 2 | 2 | 2 |
| XXII | 22 | 22 | 22 |
| IX | 9 | 11 | 9 |
| XXIV | 24 | 26 | 24 |

Os seis testes foram executados antes da alteração: quatro passaram e dois falharam (`IX` e `XXIV`).

### Erro na subtração

O algoritmo percorre o numeral da direita para a esquerda. Quando o símbolo atual é menor que seu vizinho à direita, deve subtraí-lo do acumulador. O código original usava `multiplicador = 1` também nessa condição, somando o valor. A correção é usar `multiplicador = -1`.

Assim, `IX` passa a ser `10 - 1 = 9`, e `XXIV` passa a ser `5 - 1 + 10 + 10 = 24`.

### Erro adicional na tabela

O símbolo `M` estava definido como `10000`. Um teste adicional reproduziu esse erro. Seu valor foi corrigido para `1000`, conforme a tabela do enunciado.

## Validação final

A suíte contém 9 métodos de teste: os 6 casos solicitados e 3 testes com subcasos para os demais símbolos, demais pares subtrativos e numerais compostos. Todos passaram após as correções.

Também foram verificados `IV`, `XL`, `XC`, `CD`, `CM`, `XV`, `XXVIII`, `MCMXCIV` e `MMMCMXCIX`, além dos sete símbolos básicos. O exemplo principal foi executado e retornou `24`.

O programa mantém o escopo original: conversão de numerais romanos válidos. Não foi acrescentada validação de grafias inválidas, como `IIII` ou `IC`.

## Arquivos

- `numeroromano.py`: conversor corrigido.
- `main.py`: exemplo original de execução.
- `test_numeroromano.py`: testes PyUnit.
- `.gitignore`: ignora ambientes virtuais e caches Python.
- `README.md`: instruções e explicação das correções.

Extraia o ZIP e copie seu conteúdo para a raiz do repositório antes de fazer o commit. O ZIP não contém a pasta `.git` nem arquivos temporários.
