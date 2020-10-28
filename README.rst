Simple Tic Toc Toe
******************

This project is a simple tic toc toe game using Finite State Machine

---------------

Tic Tac Toe -
############# 
This is a game normally played with paper and pencil and often called noughts and crosses.
The game is played on a 9-box grid and each player selects their mark as X or O
They take turns placing their mark in one of the 9 boxes and the first to achieve three in a row wins.
Three in a row can be hirizontal, vertical or diagonal.
Its common that no-one wins and that is a Tie game.

Supports 2 players

---------------
Instructions
---------------
``python src/run_script.py``

---------------
TESTS
---------------
``make test``

---------------
Design
---------------
Instead of a game loop, just for fun the implementation uses a finite state machine to switch between player turns.
StartState -> TurnState -> EndState ->StartState

------------------
Next Steps
------------------
Change the display to use Raspberry Pi SenseHat and txt output
Change the display to use tkinter
Add db to provide high score history

Running Instructions
--------------------
.. warning:: I used pyenv 3.7.9, this takes 20mins to recompile during installation on raspberryPi 3. It required 
             ``sudo apt-get install python-scipy``
             ``sudo apt update``
             ``sudo apt install libatlas-base-dev``
             ``sudo apt install libopenjp2-7 sense-hat``
             ``pip install sense-hat rtimulib``

``python src/run_scripts.py``

---------------------
Sensehat installation
---------------------
1. Buy a sense hat and plug it into the raspberry pi when its switched off
2. Update raspberry pi O/S `sudu apt update`
3. install sense hat `sudo apt install sense-hat`
4. reboot `sudo reboot`
5. Sense hat examples can be found here '/usr/src/sense-hat/examples'
6. More sensehat info https://pythonhosted.org/sense-hat/
