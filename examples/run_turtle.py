from miney import Minetest

# Access to mineyturtle module
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from mineyturtle import Turtle

mt = Minetest(playername="admin", password="")

print("Connected to", mt)


mt.chat.send_to_all("Turtle start")
playerPos = mt.player[0].position

turtle = Turtle(mt, 1)

def mine_forward_blocks(n):
    for _ in range(n):
        turtle.mine_forward()
        turtle.forward()

def mine_backward_blocks(n):
    for _ in range(n):
        turtle.mine_backward()
        turtle.backward()

def build_block_around():
    turtle.build_forward()
    turtle.build_backward()
    turtle.build_left()
    turtle.build_right()
    turtle.build_up()
    turtle.build_down()


mine_forward_blocks(20)
mine_backward_blocks(20)
build_block_around()

turtle.go()
