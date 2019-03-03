from turing_machine import TuringMachine
from direction import Direction
from state import StateType, State
from tape import Tape
from transition import Transition

inp = int(input("Enter decimal digit: "))
word = ""
for i in range(inp):
    word += '1'
tape = Tape(word,"10x")
states = [
    State("s0", StateType.Start),
    State("s1", StateType.Empty),
    State("s2", StateType.Empty),
    State("s3", StateType.Empty),
    State("s4", StateType.Empty), #getting rid of x in tape
    State("sf", StateType.Final)
]

transitions = [
    Transition('s0', '$', 's0', '$', Direction.Right),
    Transition('s0', '1', 's1', 'x', Direction.Left),
    Transition('s1', '$', 's2', '1', Direction.Right),
    Transition('s2', '1', 's2', '1', Direction.Right),
    Transition('s2', '0', 's2', '0', Direction.Right),
    Transition('s2', 'x', 's3', 'x', Direction.Right),
    Transition('s3', 'x' , 's3', 'x', Direction.Right),
    Transition('s3', '1', 's1', 'x', Direction.Left),
    Transition('s1', '1', 's1', '0', Direction.Left),
    Transition('s1', 'x', 's1', 'x', Direction.Left),
    Transition('s1', '0', 's2', '1', Direction.Right),
    Transition('s3', '#', 's4', '#', Direction.Left), #clearing x
    Transition('s4', 'x', 's4', '#', Direction.Left),
    Transition('s4', '1', 'sf', '1', Direction.Neutral),
    Transition('s4', '0', 'sf', '0', Direction.Neutral),
]

tm = TuringMachine(states, transitions, tape)
tm.process(verbose=False)
print("FINAL TAPE: " + tm.get_tape())