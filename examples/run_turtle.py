from miney import Minetest

# Access to mineyturtle module
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from mineyturtle import Turtle

mt = Minetest(playername="admin", password="")

print("Connected to", mt)


mt.chat.send_to_all("Turtle start")
playerPos = mt.player[0].position


turtle = Turtle(mt, 1)

# for i in range(6):
#     turtle.move_down()

#turtle.turn_left()
#turtle.move_down()
turtle.mine_forward()
turtle.move_forward()
turtle.build_forward(1)  # TODO: build_forward() is not implemented yet
#turtle.build_forward(3)
#turtle.move_forward()

turtle.go()
