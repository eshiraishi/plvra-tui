# P L V R A

## Descrição

PLVRA é uma implementação de [wordle](https://www.powerlanguage.co.uk/wordle/) / [termo](term.ooo) na forma de uma TUI (Terminal User Interface) em português, escrito em Python.

Se você não conhece o jogo, as regras são:

Você precisa adivinhar uma palavra de cinco letras em no máximo seis tentativas. A cada tentativa errada, você ganha as seguintes dicas:

* Letras que nunca aparecem na palavra aparecerão vermelhas.
* Letras que aparecem em outra posição aparecerão amarelas.
* Letras que aparecem naquela posição aparecerão verdes.

## Instalação

### PyPI

```shell
pip install -i https://test.pypi.org/simple/ plvra
```

### A partir do código fonte

```shell
git clone https://github.com/eshiraishi/plvra-tui
cd plvra-tui
sudo python setup.py install
```

## Contribuições e adição de novas palavras

Se você tiver qualquer sugestão para novas palavras, por favor [crie um PR](https://github.com/eshiraishi/plvra-tui/pulls/new) modificando `words.txt`.

O código em si está escrito completamente em inglês, então caso queira traduzir o jogo, apenas mude as mensagens em `plvra.py` e as palavras possíveis em `words.txt` por favor crie uma branch para cada idioma.

## Licença

Este software é distribuído sobre a Licença MIT.

---

## Description

PLVRA is a TUI (Terminal User Interface) implementation of [wordle](https://www.powerlanguage.co.uk/wordle/) / [termo](term.ooo) in portuguese, written in Python.

If you are not familiar with the game, the rules are:

You have to guess a five letter word in at most six tries. On each wrong try, you get the following tips:

* Letters that never appear on the word will appear red.
* Letters that appear but in another position will appear yellow.
* Letters that appear on that position will appear green.

## Installation

### PyPI

```shell
pip install -i https://test.pypi.org/simple/ plvra
```

### From source

```shell
git clone https://github.com/eshiraishi/plvra-tui
cd plvra-tui
sudo python setup.py install
```
## Contributing and adding new words

If you have any suggestion for new words, please [create a PR](https://github.com/eshiraishi/plvra-tui/pulls/new) changing `words.txt`.

The code itself is fully written in english, so if you want to translate the game, just change the messages on `plvra.py` and the possible words on `words.txt` (please create another branch for each language).

## License

This is distributed under the MIT License.
