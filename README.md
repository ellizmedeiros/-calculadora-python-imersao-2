# Calculadora Modular em Python

Projeto de calculadora didática desenvolvida em Python, com separação de responsabilidades (arquitetura modular), funções matemáticas puras, validação de entradas do usuário e testes unitários automatizados.

---

## Estrutura do Projeto

```text
calculadora/
├── operacoes.py       # Lógica matemática (funções puras de cálculo)
├── main.py            # Interface com o usuário (menus, validações e fluxo contínuo)
├── test_operacoes.py  # Testes unitários automatizados (18 cenários de teste)
├── .gitignore         # Arquivos e diretórios ignorados pelo Git
└── README.md          # Documentação do projeto
```

---

## Operações Suportadas

* `+` : Adição (suporta decimais e negativos)
* `-` : Subtração
* `*` : Multiplicação
* `/` : Divisão (com proteção contra divisão por zero)
* `**` ou `^` : Potenciação (incluindo raízes por expoente fracionário)
* `%` : Porcentagem (ex: 15% de 200 = 30)
* `s` : Sair do programa

---

## Como Executar a Calculadora

No terminal, dentro da pasta do projeto:
```bash
python main.py
```

---

## Como Executar os Testes Unitários

Para rodar os testes automatizados com o `unittest` nativo:
```bash
python test_operacoes.py
```
