# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:56:53 2017

@author: Matheus
"""

import turtle

window = turtle.Screen()

n = input("Digite as instruções para a tartaruga('F' para andar, '-' para virar à direita em 90, '+' para virar à esquerda em 90, '(' para virar à esquerda em 60, ')' para virar à direita em 60 e 'f' para andar sem rastro): ")
F = input("Digite a regra de movimento de 'F': ")
f = input("Digite a regra de movimento de 'f': ")
r = int(input("Quantas repetições terá o desenho: "))
c = input("Escolha uma cor da tartaruga (escreva a cor dela em inglês): ")
bc = input("Escolha uma cor de fundo (escreva a cor do fundo em inglês): ")
l = n.split()
lF = F.split()
lf = f.split()
tartaruga1 = turtle.Turtle()
tartaruga1.speed('fastest')
tartaruga1.penup()
tartaruga1.left(90)
tartaruga1.setpos(-150, -100)
tartaruga1.pendown()
tartaruga1.color(c)
window.bgcolor(bc)

for i in range(r):
    for g in range(len(l)):
        if l[g] == 'F':
            l[g] = lF
        if l[g] == 'f':
            l[g] = lf
    l = [item for sublist in l for item in sublist]
for a in range(len(l)):
    if l[a] == 'F':
        tartaruga1.forward(5)
    if l[a] == 'f':
        tartaruga1.penup()
        tartaruga1.forward(5)
        tartaruga1.pendown()
    if l[a] == '+':
        tartaruga1.left(90)
    if l[a] == '-':
        tartaruga1.right(90)
    if l[a] == '(':
        tartaruga1.left(60)
    if l[a] == ')':
        tartaruga1.right(60)