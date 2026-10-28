"""
Calculadora Modular em Python
Arquivo principal (ponto de entrada) responsável pela interação com o usuário.
"""

from operacoes import somar, subtrair, multiplicar, dividir, potencia, porcentagem


def obter_numero(mensagem: str) -> float:
    """
    Solicita um número ao usuário e trata erros caso seja digitado algo inválido.
    Fica em repetição até que um número válido seja digitado.
    """
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido (ex: 10 ou 3.5).")


def exibir_menu():
    """Exibe o menu de operações disponíveis."""
    print("\n" + "=" * 40)
    print("        CALCULADORA MODULAR")
    print("=" * 40)
    print("  +       : Adição")
    print("  -       : Subtração")
    print("  *       : Multiplicação")
    print("  /       : Divisão")
    print("  ** ou ^ : Potência")
    print("  %       : Porcentagem")
    print("  s       : Sair")
    print("=" * 40)


def executar_calculo(num1: float, operacao: str, num2: float):
    """
    Executa a operação matemática correspondente chamando as funções
    do módulo operacoes.py e exibe o resultado formatado.
    """
    if operacao == '+':
        resultado = somar(num1, num2)
        print(f"\n Resultado: {num1} + {num2} = {resultado}")

    elif operacao == '-':
        resultado = subtrair(num1, num2)
        print(f"\n Resultado: {num1} - {num2} = {resultado}")

    elif operacao == '*':
        resultado = multiplicar(num1, num2)
        print(f"\n Resultado: {num1} * {num2} = {resultado}")

    elif operacao == '/':
        try:
            resultado = dividir(num1, num2)
            print(f"\n Resultado: {num1} / {num2} = {resultado}")
        except ValueError as erro:
            print(f"\n Erro: {erro}")

    elif operacao in ('^', '**'):
        resultado = potencia(num1, num2)
        print(f"\n Resultado: {num1} ** {num2} = {resultado}")

    elif operacao == '%':
        resultado = porcentagem(num1, num2)
        print(f"\n Resultado: {num2}% de {num1} = {resultado}")


def main():
    """Função principal que orquestra a execução da calculadora."""
    operacoes_validas = {'+', '-', '*', '/', '**', '^', '%'}

    while True:
        exibir_menu()
        operacao = input("Digite a operação desejada: ").strip().lower()

        # Condição de saída do programa
        if operacao in ('s', 'sair'):
            print("\nObrigado por usar a calculadora! Até a próxima.")
            break

        if operacao not in operacoes_validas:
            print("\n Operação inválida! Escolha uma das opções do menu.")
            continue

        # Coleta dos números conforme a operação
        if operacao == '%':
            num1 = obter_numero("Digite o valor total (base): ")
            num2 = obter_numero("Digite a porcentagem desejada (%): ")
        else:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

        # Execução e exibição
        executar_calculo(num1, operacao, num2)

        input("\nPressione [Enter] para continuar...")


if __name__ == "__main__":
    main()
