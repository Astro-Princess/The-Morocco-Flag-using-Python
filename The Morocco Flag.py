import turtle

def draw_drapo(taille, couleur):

    astro = turtle.Turtle()
    astro.shape("turtle")
    astro.color(couleur)
    astro.speed(1)
    astro.width(13)
    astro.goto(-150,0)

    i = 0
    while i < 5:
        astro.forward(300)
        astro.right(180*4/5)

        i+=1
    astro.ht()

window = turtle.Screen()
window.bgcolor("red")
window.title("The Morocco Flag")
draw_drapo(250,"green")
