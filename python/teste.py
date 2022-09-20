the_world_is_flat = True#não precisa dizer o tipo da variavel para criar
if the_world_is_flat:
    print("Be careful not to fall off!")
else:
    print("Be")#comentário
    pass
print('don\'t')#\' para desconsidera as ' \' '
print("don\n't")
print(r"don\n't")#r faz remove os caracteres especiais da string
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")#printar do jeito que você quer
print(3*"kaka" + 'baka')#* printa mais de uma vez a mesma string + concatena

string = "nome emon"
print(string[6])#printa um caractere de uma string
print(string[-1])#começar a contar da direita para esquerda
print(string[2:7])#cortando um pedaço especifico da string
print(string[5:])#começando a string de um ponto em especifico
print(string[:5])