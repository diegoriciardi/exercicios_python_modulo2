#!/usr/bin/python3

lista = []

def ler_arquivo(nome):
    try:
        with open(nome, 'r') as f:
            print(f.readlines())
    except FileNotFoundError:
        print("Erro: arquivo não encontrado")
    except Exception as e:
        print("Erro: {}".format(e))

def contar_linhas(arquivo):
    try:
        with open(arquivo, 'r') as f:
            lista = f.readlines()
            print("O arquivo '{}' tem {} linhas".format(arquivo, len(lista)))
    except FileNotFoundError:
        print("Erro: arquivo não encontrado")
    except Exception as e:
        print("Erro: {}".format(e))

def escrever_arquivo(arquivo, *args):
    try:
        with open(arquivo, 'a') as f:
            for argumento in args:
                f.writelines(argumento)

    except FileNotFoundError:
        print("Erro: arquivo não encontrado")
    except Exception as e:
        print("Erro: {}".format(e))

#ler_arquivo('arquivo.texto.desafio')
print("\n------->lendo arquivo ANTES de escrever o novo conteúdo\n")
ler_arquivo('arquivo.texto.desafio')
print("------->Informando o número de linhas do arquivo\n")
contar_linhas('arquivo.texto.desafio')
novo_conteudo = [ '\n', 'conteúdo novo\n', 'mais um registro\n' ]
escrever_arquivo('arquivo.texto.desafio', novo_conteudo)
print("------->lendo arquivo DEPOIS de escrever o novo conteúdo\n")
ler_arquivo('arquivo.texto.desafio')


