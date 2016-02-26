import turtle

abc = turtle.Turtle()

abc.shape("arrow")
abc.color("blue")
abc.speed(1000)
abc.ht()

abc.up()
abc.setpos(0,0)
abc.down()

for i in range(1,37):  
    abc.left(35)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(145)
    abc.forward(50)
    abc.right(35)
    abc.forward(50)
    abc.right(10)
    
abc.up()
abc.setpos(0,-50)
abc.seth(270)
abc.down()
abc.forward(200)
