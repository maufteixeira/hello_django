from django.shortcuts import render, HttpResponse

# Create your views here.
def hello (request, nome, idade):
    return HttpResponse('<h1>Olá {} de {} anos!!!</h1>'.format(nome, idade))


def soma (request, a, b):
    return HttpResponse('<h1>O valor da soma de {} e {} é igual {}</h1>'.format(a, b, a+b))

def subtracao (request, a, b):
    return HttpResponse('<h1>O valor da subtração de {} e {} é igual {}</h1>'.format(a, b, a-b))

def multiplicacao (request, a, b):
    return HttpResponse('<h1>O valor da multiplicação de {} e {} é igual {}</h1>'.format(a, b, a*b))

def divisao (request, a, b):
    return HttpResponse('<h1>O valor da divisão de {} e {} é igual {}</h1>'.format(a, b, a/b))