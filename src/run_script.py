from tictactoe_fsm import SimpleDevice
from tictactoe_helpers import setupGame

def beginGame(device):
    device.on_event('Start')
    setupGame(device)


if __name__ == "__main__":
   device = SimpleDevice()
   beginGame(device)
