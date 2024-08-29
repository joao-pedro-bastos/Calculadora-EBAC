"""Utilize o comando ‘input’ para receber ao menos 2 números de entrada do usuário;

Converta os valores recebidos pelo usuário para número inteiro (int) ou ponto flutuante (float);

Implemente ao menos 4 operações matemáticas em seu código;

Adicione um laço de repetição ou uma condicional. Por exemplo: você pode permitir que o usuário escolha qual operação realizar ou criar um loop que permita ao usuário realizar várias operações consecutivas;

Utilize o comando ‘print’ para exibir o resultado da operação matemática."""

# Variáveis
lista_Sim = ['Sim', 'SIM', 'sim', 's', 'S']
num1 = 0
num2 = 0
resposta = ''

# Recebe dois valores
while True:
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('Adição -> 1\n'
              'Subtração -> 2\n'
              'Divisão -> 3\n'
              'Multiplicação -> 4\n')
    except ValueError:
        print('Não é permitido texto nestes campos')
        break
# Calcula
    calcula = float(input('Qual operação deseja fazer: '))
    if calcula == 1:
        resposta = num1 + num2
    elif calcula == 2:
        resposta = num1 - num2
    elif calcula == 3:
        if num1 or num2 == 0:
            try:
                resposta = num1 / num2
            except ZeroDivisionError:
                print('Não é permitida divisão por zero!')


    elif calcula == 4:
        resposta = num1 * num2

# Resposta do cálculo
    print(f'\nO resultado da operação é: {resposta}\n -----------------')
    continua = str(input('Deseja continuar? SIM / NÃO\n'))
    if continua in lista_Sim:
        pass
    else:
        break
