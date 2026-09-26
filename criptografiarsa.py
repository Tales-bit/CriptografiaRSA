print("==============================================================================")
print("Bem vindo ao codificador e decodificador de mensagens usando criptografia RSA!")
print("==============================================================================")
print("Digite 1 para codificar um numero, 2 para decodificar um numero e 3 para usar \na tabela de conversao:")
esc = int(input())

if esc == 1:
    print("Digite o produto n:")
    n = int(input())
    blocos_codificados = []
    print("Digite a quantidade de blocos que voce quer codificar:")
    qtd = int(input())
    for i in range(qtd):
        print("Digite o bloco {0}:".format(i+1))
        b = int(input())
        a = pow(b, 3, n)
        blocos_codificados.append(a)
    print("A mensagem codificada completa fica igual a")
    for i in blocos_codificados:
        print(i, end="")

if esc == 2:
    print("Digite o primo p:")
    p = int(input())
    print("Digite o primo q:")
    q = int(input())
    n = int(p*q)
    d = int((2*(p-1)*(q-1)+1)/3)
    print("n = {0}\nd = {1}".format(n, d))
    blocos_decodificados = []
    print("Digite a quantidade de blocos que voce quer decodificar:")
    qtd = int(input())
    for i in range(qtd):
        print("Digite o bloco {0}:".format(i+1))
        a = int(input())
        b = pow(a, d, n)
        blocos_decodificados.append(b)
    print("A mensagem decodificada completa fica igual a")
    for i in blocos_decodificados:
        print(i, end="")

if esc == 3:
    print("Digite 1 para transformar uma frase em numero e 2 para transformar um numero \nem uma frase:")
    esc = int(input())
    if esc == 1:
        print("Digite a frase:")
        mensagem = input().upper()
        for letra in mensagem:
            if letra == " ":
                print("99", end="")
            else:
                print(ord(letra) - 55, end="")
    if esc == 2:
        print("Digite o numero que representa a mensagem:")
        mensagem = int(input())
        s = str(mensagem)
        letras = [int(s[i:i+2]) for i in range(0, len(s), 2)]
        for i in letras:
            if i == 99:
                print(" ", end="")
            else:
                print(chr(i + 55), end="")