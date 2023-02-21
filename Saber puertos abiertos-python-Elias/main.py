import turtle

# Create turtle object
iron_man = turtle.Turtle()

# Set turtle color
iron_man.color("red")

# Draw the head
iron_man.begin_fill()
iron_man.circle(50)
iron_man.end_fill()

# Move turtle to draw body
iron_man.penup()
iron_man.setpos(0, -50)
iron_man.pendown()

# Draw the body
iron_man.begin_fill()
iron_man.circle(100)
iron_man.end_fill()

# Move turtle to draw arms
iron_man.penup()
iron_man.setpos(-70, -50)
iron_man.pendown()

# Draw the left arm
iron_man.begin_fill()
iron_man.circle(20)
iron_man.end_fill()

# Move turtle to draw right arm
iron_man.penup()
iron_man.setpos(70, -50)
iron_man.pendown()

# Draw the right arm
iron_man.begin_fill()
iron_man.circle(20)
iron_man.end_fill()

# Move turtle to draw eyes
iron_man.penup()
iron_man.setpos(-15, 60)
iron_man.pendown()

# Draw the left eye
iron_man.begin_fill()
iron_man.circle(10)
iron_man.end_fill()

# Move turtle to draw right eye
iron_man.penup()
iron_man.setpos(15, 60)
iron_man.pendown()

# Draw the right eye
iron_man.begin_fill()
iron_man.circle(10)
iron_man.end_fill()

# Move turtle to draw mouth
iron_man.penup()
iron_man.setpos(0, 30)
iron_man.pendown()

# Draw the mouth
iron_man.begin_fill()
iron_man.circle(30, 180)
iron_man.end_fill()

# Hide turtle
iron_man.hideturtle()

# Keep window open
turtle.mainloop()
