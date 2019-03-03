from turing_machine import TuringMachine
from state import State, StateType
from transition import Transition
from direction import Direction
from tape import Tape

tape = Tape('aaabbb', 'abxy')
states = [
            State("s0", StateType.Start),
            State("s1", StateType.Empty),
            State("s2", StateType.Empty),
            State("sf", StateType.Final)
         ]

transitions = [
                 Transition("s0", "$", "s0", "$", Direction.Right),
                 Transition("s0", "a", "s1", "x", Direction.Right),
                 Transition("s1", "a", "s1", "a", Direction.Right),
                 Transition("s1", "b", "s2", "y", Direction.Left),
                 Transition("s2", "a", "s2", "a", Direction.Left),
                 Transition("s2", "x", "s0", "x", Direction.Right),
                 Transition("s1", "y", "s1", "y", Direction.Right),
                 Transition("s2", "y", "s2", "y", Direction.Left),
                 Transition("s0", "y", "sf", "y", Direction.Neutral)
              ]

tm = TuringMachine(states, transitions, tape)
tm.process(verbose=True)
print(tm.get_tape())