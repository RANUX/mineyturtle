import miney
import time

class Turtle:
    
    def __init__(self, mt: miney.Minetest, player: miney.player.Player, turtle_id: int, batch_mode: bool =False, run_delay: int =1) -> None:
        self.mt = mt
        self._id = turtle_id
        self._delay = run_delay
        self.commands = []
        self._batch_mode = batch_mode
        self._player = player
    
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

    def is_running(self) -> bool:
        return self.mt.lua.run(f"""
            local t = computertest.turtles[{self._id}]
            return coroutine.status(t.coroutine) ~= "dead"
        """)

    def get_pos(self) -> dict:
        return self.mt.lua.run(f"""
            local t = computertest.turtles[{self._id}]
            return t:getLoc()
        """)

    @property
    def position(self) -> dict:
        return self.get_pos()

    def get_loc_relative(self, num_forward, num_up,num_right) -> dict:
        return self.mt.lua.run(f"""
            local t = computertest.turtles[{self._id}]
            return t:getLocRelative({num_forward}, {num_up}, {num_right})
        """)

    def set_batch_mode(self, batch_mode: bool) -> None:
        self._batch_mode = batch_mode

    def _add_cmd(self, command: str, *args) -> None:
        if self._batch_mode:
            self.commands.append(self._build_cmd(command, *args))
        else:
            self.commands.append(self._build_cmd(command, *args))
            self.go()

    def _build_cmd(self, command: str, *args) -> str:
        return f"turtle:{command}({','.join(map(str, args))})"

    def go(self) -> None:
        commands = ';'.join(self.commands)
        self.mt.lua.run(f"""
            local t = computertest.turtles[{self._id}]
            local command = "function init(turtle) {commands} end"
            t:upload_code_to_turtle(minetest.get_player_by_name("{self._player.name}"), command, false)
        """)
        self.commands = []
        time.sleep(self._delay)

