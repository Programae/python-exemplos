'''
Exemplo Aula #1
Programae - Python
http://programae.org.br
'''
from turtle import *

# define o "desenhista"
professor = Turtle()

# personalizações: mostra o desenho da tartaruga
professor.shape("turtle")
professor.showturtle()


'''
Mapeamento das regras

Dica: crie junto com seus alunos estas regras de movimentação.

____.avance(pixels) -> anda com a tartaruga o numero de pixels no plano x,y
____.recue(angulo)
____.direita(angulo)
____.esquerda(angulo)
'''

professor.avance = professor.forward
professor.recue = professor.back
professor.direita = professor.right
professor.esquerda = professor.left

# desenha um quadrado
professor.avance(100)
professor.direita(90)
professor.avance(100)
professor.esquerda(90)
professor.recue(100)
professor.direita(90)
professor.recue(100)

# espera um clique do mouse pra sair
exitonclick()
