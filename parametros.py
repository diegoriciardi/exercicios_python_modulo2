#!/usr/bin/python3

def cadastro(**kwargs):
    return("o usuario {}-{} foi cadastrado com sucesso!".format(kwargs['nome'], kwargs['sobrenome']))

print(cadastro(nome="diego", sobrenome="riciardi", idade=32))

exit()

def soma(*args):
    return(sum(args))

print("A soma dos valores da tupla eh: {}".format(soma(1,11,23,37,49,57,63)))
