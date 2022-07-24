from miney import Minetest

# Access to mineyturtle module
import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from mineyturtle import Turtle

mt = Minetest(playername="admin", password="")

print("Connected to", mt)


mt.chat.send_to_all("Turtle start")
playerPos = mt.player[0].position

turtle = Turtle(mt, mt.player[0], 1, batch_mode=True)

print("Turtle position:", turtle.position)
print("Get loc relative:", turtle.get_loc_relative(10, 10, 10))

def mine_forward_blocks(n):
    for _ in range(n):
        turtle.mine_forward()
        turtle.forward()
        print("Turtle running: ", turtle.is_running())

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

print("Turtle running: ", turtle.is_running())
turtle.right()
mine_forward_blocks(10)
mine_backward_blocks(10)
build_block_around()
print("Turtle running: ", turtle.is_running())

turtle.go()
