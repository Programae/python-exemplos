'''
Exemplo Aula #2
Programaê - Python
http://programae.org.br
'''
from turtle import *

# define o "desenhista"
professor = Turtle()
bgpic("plano_cartesiano.png")

# personalizações: mostra o desenho da tartaruga
professor.shape("turtle")
professor.showturtle()
professor.pensize(5) # ajustando a espessura da linha

professor.avance = professor.forward
professor.recue = professor.back
professor.direita = professor.right
professor.esquerda = professor.left

# desenha um triângulo
professor.avance(100)

professor.home() # volta pra posição inicial
professor.esquerda(-45) # -45 graus
professor.avance(100)

professor.home() # volta pra posição inicial
professor.esquerda(-90) # -45 graus
professor.avance(100)

professor.home() # volta pra posição inicial
professor.esquerda(-90 + -45) # -135 graus
professor.avance(100)

professor.home() # volta pra posição inicial
professor.esquerda(-180) # -45 graus
professor.avance(100)

professor.home() # volta pra posição inicial
professor.esquerda(-180-45) # -45 graus
professor.avance(100)

professor.home() # volta pra posição inicial
professor.esquerda(90) # 90 graus
professor.avance(100)

professor.home() # volta pra posição inicial
professor.esquerda(45) # 45 graus
professor.avance(100) # 100 passos

professor.home() # volta pra posição inicial

# espera um clique do mouse pra sair
exitonclick()
