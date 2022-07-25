
# How to run MineySandbox with Turtle on Windows
Download and install mineysandbox with Computertest + MineyTurtle: 
[https://github.com/RANUX/mineyturtle/releases/](https://github.com/RANUX/mineyturtle/releases/)

## How to build custom MineySandbox

Download and install mineysandbox:
[https://github.com/miney-py/miney_distribution/releases](https://github.com/miney-py/miney_distribution/releases)

How to install mineysandbox:
[https://miney.readthedocs.io/en/latest/quickstart.html#installation](https://miney.readthedocs.io/en/latest/quickstart.html#installation)

# how to install for mineysandbox
Download latest version: 
Open command prompt and go to miney folder
```
cd path_to_miney_folder\miney_x64\Python>
```
Install package
```
python.exe -m pip install git+https://github.com/RANUX/mineyturtle.git@main#egg=mineyturtle
```
Install computer test mod:
1. Download forket computertest archive: https://github.com/RANUX/Computertest
2. Extract to miney_x64\Minetest\mods
3. Run mine miney_launcher.exe, click to `Open Minetest`
4. Chose world and click Settings
5. Select mod computertest and enable it

# How to setup miney independent from mineysandbox
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
# How to run
#### In mineysanbox
1. Run minetest
2. Play world or Connect to the server
3. Grant privileges to `give`: `/grant <player> give`. For single player <player> enter `/grant MineyPlayer give`
4. Use `/give <player> computertest:turtle` to give a turtle to a player. For single player: `/give MineyPlayer computertest:turtle`
5. Switch to Python IDLE and run test code:
 ```python
import miney
from mineyturtle import Turtle
mt = miney.Minetest()
# print(mt.player[0])  # get player name
turtle = Turtle(mt, mt.player[0], 1)
turtle.forward()
```
  
####  Out of mineysandbox
1. cd to examples and open run_turtle.py
2. Change playername and password or set Minetest() without arguments if you connect to localserver
3. Run `python run_turtle.py`
