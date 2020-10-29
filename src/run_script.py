from tictactoe_fsm import SimpleDevice
from tictactoe_helpers import setupGame
import signal
import sys
import time

def signal_handler(signal, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)

def beginGame(device):
    device.on_event('Start')
    setupGame(device)


if __name__ == "__main__":
   signal.signal(signal.SIGINT, signal_handler)
   device = SimpleDevice()
   beginGame(device)
