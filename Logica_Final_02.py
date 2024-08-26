#Descobrindo o Número Mágico na Rede Polkadot
#1. O "Número Mágico" é o primeiro número dentro de um intervalo que atende a todas as condições abaixo:
#2. É divisível por 4.
#3. É um número primo.
#4. A soma dos dígitos do número é um número ímpar.
#5. Se nenhum número no intervalo atender a todas essas condições, o programa deverá informar que o "Número Mágico" não foi encontrado.

#Criação e Dicas:
#• Comece pedindo ao usuário para inserir dois números inteiros que definirão o intervalo.
#• Crie uma função para verificar se um número é primo e outra para calcular a soma dos dígitos de um número.
#• Percorra o intervalo utilizando um laço de repetição e aplique as funções criadas para identificar o número mágico.
#• Certifique-se de que seu código é eficiente, especialmente ao verificar se um número é primo.

def solicita_numero(x, y):
    while True:
        try:
            if x is None:
                numero = int(input("Insira o primeiro número: "))
            else:
                numero = int(input("Insira o segundo número: "))  
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def intervalo_valido(inicio, fim):
  if (inicio <= fim):
    return True
  else:
    return False

def eh_primo(numero):
    if numero <= 1:
        return False
    if numero == 2 or numero == 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos(num01, num02):
    primos = []
    for num in range(num01, num02 + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

def soma_dos_digitos(numero):
    # Converte o número para string, itera sobre cada caractere, converte de volta para inteiro e soma
    soma = sum(int(digito) for digito in str(numero))
    return soma

def eh_impar(numero):
    # Verifica se o resto da divisão do número por 2 é diferente de zero
    return numero % 2 != 0

def atendeRequisitos(numerosPrimos):
    for numero in numerosPrimos:
        if eh_primo(numero) and eh_impar(soma_dos_digitos(numero)) and numero % 4 == 0:
            return numero
    return None

def buscaNumeroMagico():
  numero_01 = None
  numero_02 = None
  resultado = None
  listaPrimos = []

  numero_01 = solicita_numero(numero_01, numero_02)
  numero_02 = solicita_numero(numero_01, numero_02)
  intervalo = intervalo_valido(numero_01, numero_02)
  if intervalo :
    listaPrimos = encontrar_primos(numero_01, numero_02)
    resultado = atendeRequisitos(listaPrimos)
  else:
    print("O intervalo não é válido")

  if resultado is not None:
    print(f"O Número Mágico é: {resultado}")
  else:
    print("O Número Mágico não foi encontrado.")

buscaNumeroMagico()