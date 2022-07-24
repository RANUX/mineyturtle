
# Requirements
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
1. Run minetest
2. Connect to the server
3. Grant privileges to `give`: `/grant <player> give`
4. Use `/give <player> computertest:turtle` to give a turtle to a player
5. cd to examples and open run_turtle.py
6. Change playername and password or set Minetest() without arguments if you connect to localserver
7. Run `python run_turtle.py`
