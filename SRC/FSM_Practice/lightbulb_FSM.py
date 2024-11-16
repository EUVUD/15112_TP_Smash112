# Example project from: https://youtu.be/E45v2dD3IQU?si=Ooj8rFOT69xm8a3U
from random import randint
import time

State = type("State", (object,), {})

class LightOn(State):
    def Execute(self):
        print("Light is On!")

class LightOff(State):
    def Execute(self):
        print("Light is Off!")


class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print("transitioning")

class SimpleFSM(object):
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None

    def SetState(self, stateName):
        self.curState = self.states[stateName]


    def Transition(self, transName):
        self.trans = self.transitions[transName]

    def Execute(self):
        if (self.trans):
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.curState.Execute()

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.LightOn = True


if __name__ == "__main__":
    light = Char()

    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    light.FSM.transitions["toOn"] = Transition("On")
    light.FSM.transitions["toOff"] = Transition("Off")

    light.FSM.SetState("On")

    for i in range(20):
        timeInterval = 1  # 1 second interval
        time.sleep(timeInterval)  # Replace clock-based wait

        # Randomly decide to toggle the light state
        if randint(0, 2):
            if light.LightOn:
                light.FSM.Transition("toOff")
                light.LightOn = False
            else:
                light.FSM.Transition("toOn")
                light.LightOn = True

        # Execute the FSM
        light.FSM.Execute()