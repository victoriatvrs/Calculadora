# Calculadora

Repositório dedicado ao desenvolvimento de uma calculadora em Python para terminal, com operações aritméticas básicas e funções matemáticas (potência, raiz quadrada, porcentagem, trigonometria e logaritmo), reunidas em um único script.

---

## Visão Geral

- **Modo de Uso:** Execução única — o usuário escolhe a operação, informa o(s) número(s) e recebe o resultado no terminal
- **Persistência:** Não possui (nenhum dado é salvo entre execuções)
- **Arquitetura:** Script único (`calculadora.py`), sem divisão em módulos
- **Autores:** Victoria Tavares

---

## Tecnologias e Ferramentas

- **Python 3**
- **Módulo `math`** (biblioteca padrão do Python)
- **Git & GitHub** (Versionamento e controle de versões)

---

## Estrutura do Repositório

```text
├── calculadora.py    # Script único: menu, leitura de dados, cálculos e saída
└── README.md         # Documentação do projeto
```

## Como Executar
Certifique-se de ter o Python 3 instalado no sistema.

Clone o repositório:

```Bash
git clone https://github.com/victoriatvrs/Calculadora.git
cd Calculadora
```

Execute o programa:
- No Linux / macOS:
```Bash
python3 calculadora.py
```

- No Windows:
```Bash
python calculadora.py
```

## Funcionalidades e Menu
Menu Principal

1. Soma: `n1 + n2`

2. Subtração: `n1 - n2`

3. Multiplicação: `n1 * n2`

4. Divisão: `n1 / n2`

5. Potência: `n1` elevado a `n2`

6. Raiz quadrada: raiz quadrada de `n1` (pede apenas um número)

7. Porcentagem: `n1`% de `n2`

8. Seno: seno de `n1` (pede apenas um número; ângulo em graus)

9. Cosseno: cosseno de `n1` (pede apenas um número; ângulo em graus)

10. Tangente: tangente de `n1` (pede apenas um número; ângulo em graus)

11. Logaritmo: logaritmo de `n1` na base `n2`

## Validações e Tratamento de Erros
O programa trata automaticamente os casos em que a operação não pode ser realizada:

- **Divisão:** informa que é impossível dividir por 0.
- **Raiz quadrada:** informa que a raiz não existe no conjunto dos reais quando o número é negativo.
- **Logaritmo:** informa que é impossível quando o logaritmando ou a base são menores ou iguais a 0, ou quando a base é igual a 1.
- **Operação inválida:** exibe aviso caso a opção escolhida não esteja no menu.
