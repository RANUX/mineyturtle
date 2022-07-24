import miney
import time

class Turtle:
    
    def __init__(self, mt: miney.Minetest, turtle_id: int, delay: int =1) -> None:
        self.mt = mt
        self._id = turtle_id
        self._delay = delay
        self.commands = []
    
    def right(self):
        self.move_right()

    def left(self):
        self.move_left()

    def forward(self):
        self.move_forward()
    
    def backward(self):
        self.move_backward()
    
    def up(self):
        self.move_up()
        
    def move_forward(self) -> None:
        self._add_cmd("moveForward")

    def move_backward(self) -> None:
        self._add_cmd("moveBackward")
    
    def move_up(self) -> None:
        self._add_cmd("moveUp")

    def move_down(self) -> None:
        self._add_cmd("moveDown")

    def move_left(self) -> None:
        self._add_cmd("moveLeft")

    def move_right(self) -> None:
        self._add_cmd("moveRight")

    def mine_up(self) -> None:
        self._add_cmd("mineUp")

    def mine_down(self) -> None:
        self._add_cmd("mineDown")

    def mine_left(self) -> None:
        self._add_cmd("mineLeft")

    def mine_right(self) -> None:
        self._add_cmd("mineRight")

    def mine_forward(self) -> None:
        self._add_cmd("mineForward")

    def mine_backward(self) -> None:
        self._add_cmd("mineBackward")

    def turn_right(self) -> None:
        self._add_cmd("turnRight")

    def turn_left(self) -> None:
        self._add_cmd("turnLeft")

    def build_forward(self) -> None:
        self._add_cmd("buildForward", 1)

    def build_backward(self) -> None:
        self._add_cmd("buildBackward", 1)

    def build_up(self) -> None:
        self._add_cmd("buildUp", 1)

    def build_down(self) -> None:
        self._add_cmd("buildDown", 1)

    def build_left(self) -> None:
        self._add_cmd("buildLeft", 1)

    def build_right(self) -> None:
        self._add_cmd("buildRight", 1)

    def _add_cmd(self, command: str, *args) -> None:
        self.commands.append(self._build_cmd(command, *args))

    def _build_cmd(self, command: str, *args) -> str:
        return f"turtle:{command}({','.join(map(str, args))})"

    def _run_cmd(self, command: str) -> None:
        self.mt.lua.run(f"""
            local function getTurtle(id) return computertest.turtles[id] end
            local t = getTurtle({self._id})
            local command = "function init(turtle) return turtle:{command}() end"
            t:upload_code_to_turtle(minetest.get_player_by_name("{self.mt.playername}"), command, false)
        """)
        time.sleep(self._delay)

    def go(self) -> None:
        commands = ';'.join(self.commands)
        self.mt.lua.run(f"""
            local function getTurtle(id) return computertest.turtles[id] end
            local t = getTurtle({self._id})
            local command = "function init(turtle) {commands} end"
            t:upload_code_to_turtle(minetest.get_player_by_name("{self.mt.playername}"), command, false)
        """)
        self.commands = []
        time.sleep(self._delay)

