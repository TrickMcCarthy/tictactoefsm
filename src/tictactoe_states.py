from state import State

from tictactoe_helpers import *

# Start of our states
class TurnState(State):
      """
      State which indicates which player turn it is
      """

      def on_event(self, event):
          if event == 'Player1Turn':
             playerActions()
             return TurnState()
          if event == 'Player2Turn':
             computerActions()
             return TurnState()
          if event == 'ComputerWin' or event == 'PlayerWin' or event == 'Tie':
             if anotherGame():
                return StartState()
             else:
                return EndState()

          return self

class EndState(State):
      """
      The state that allows the games to end
      """
      def on_event(self, event):
          return self

class StartState(State):
      """
      The state to start from
      """

      def on_event(self, event):
          if event == 'Start':
             return TurnState()
             
          return self

 # End of our states.
