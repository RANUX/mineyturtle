from miney import Minetest

# Access to mineyturtle module
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from mineyturtle import Turtle

mt = Minetest(playername="admin", password="")

print("Connected to", mt)


mt.chat.send_to_all("Turtle start")
playerPos = mt.player[0].position


turtle = Turtle(mt, 1)

for i in range(3):
    turtle.move_up()

turtle.go()
