"""A series of useful utilities for programming a Doosan robot with Doosan
Robotics Language (DRL)."""
from enum import Enum
from itertools import chain, islice
from DRL.DRL import *


SOLUTION_SPACES = 0, 1, 2, 3, 4, 5, 6, 7
__solution_space_table__ = '''
 ----------------------------------------------------
| solution  |        |          |         |          |
| space     | binary | shoulder | elbow   | wrist    |
| --------- | ------ | -------- | ------- | -------- |
| 0         | 000    | lefty    | below   | no flip  |
| 1         | 001    | lefty    | below   | flip     |
| 2         | 010    | lefty    | above   | no flip  |
| 3         | 011    | lefty    | above   | flip     |
| 4         | 100    | righty   | below   | no flip  |
| 5         | 101    | righty   | below   | flip     |
| 6         | 110    | righty   | above   | no flip  |
| 7         | 111    | righty   | above   | flip     |
 ----------------------------------------------------
'''

class Robot(Enum):
    H2515 = 'H2515'
    H2017 = 'H2017'
    M1509 = 'M1509'
    M1013 = 'M1013'
    M0617 = 'M0617'
    M0609 = 'M0609'
    A0912 = 'A0912'
    A0509 = 'A0509'

    @property
    def payload(self) -> int:
        return self._payload
    
    @payload.setter
    def payload(self, value: int) -> None:
        self._payload = value

    @property
    def reach(self) -> int:
        return self._reach
    
    @reach.setter
    def reach(self, value: int) -> None:
        self._reach = value

    @property
    def weight(self) -> float:
        return self._weight
    
    @weight.setter
    def weight(self, value: float) -> None:
        self._weight = value

    @property
    def tool_speed(self) -> int:
        return self._tool_speed
    
    @tool_speed.setter
    def tool_speed(self, value: int) -> None:
        self._tool_speed = value

    @property
    def repeatability(self) -> float:
        return self._repeatability
    
    @repeatability.setter
    def repeatability(self, value: float) -> None:
        self._repeatability = value

    @property
    def temperature(self) -> tuple[int, int]:
        return self._temperature
    
    @temperature.setter
    def temperature(self, value: tuple[int, int]) -> None:
        self._temperature = value

    @property
    def joint_range(self) -> list[tuple[int]]:
        return self._range
    
    @joint_range.setter
    def joint_range(self, value: list[tuple[int]]) -> None:
        self._range = value

    @property
    def joint_speed(self) -> list[int]:
        return self._joint_speed
    
    @joint_speed.setter
    def joint_speed(self, value: list[int]) -> None:
        self._joint_speed = value

    @property
    def specifications(self) -> dict:
        return {
            'General': {
                'Payload in kg': self.payload,
                'Reach in mm': self.reach,
                'Weight in kg': self.weight,
            },
            'Performance': {
                'Tool Speed in m/s': self.tool_speed,
                'Repeatability in mm': self.repeatability,
                'Temperature min/max': self.temperature,
            },
            'Joint Movement': {
                'Range in degrees per joint': self.joint_range,
                'Max speed in deg per sec': self.joint_speed,
            },
        }

Robot.H2515.payload = 25
Robot.H2515.reach = 1_500
Robot.H2515.weight = 77.0
Robot.H2515.tool_speed = 1
Robot.H2515.repeatability = 0.1
Robot.H2515.temperature = 0, 45
Robot.H2515.joint_range = [(-360, 360), # J1
                           (-125, 125), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.H2515.joint_speed = [100,         # J1
                           80,          # J2
                           100,         # J3
                           180,         # J4
                           180,         # J5
                           180]         # J6

Robot.H2017.payload = 20
Robot.H2017.reach = 1_700
Robot.H2017.weight = 79.0
Robot.H2017.tool_speed = 1
Robot.H2017.repeatability = 0.1
Robot.H2017.temperature = 0, 45
Robot.H2017.joint_range = [(-360, 360), # J1
                           (-125, 125), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.H2017.joint_speed = [100,         # J1
                           80,          # J2
                           100,         # J3
                           180,         # J4
                           180,         # J5
                           180]         # J6

Robot.M1509.payload = 15
Robot.M1509.reach = 900
Robot.M1509.weight = 33.0
Robot.M1509.tool_speed = 1
Robot.M1509.repeatability = 0.03
Robot.M1509.temperature = 0, 45
Robot.M1509.joint_range = [(-360, 360), # J1
                           (-125, 125), # J2
                           (-150, 150), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.M1509.joint_speed = [150,         # J1
                           150,          # J2
                           180,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Robot.M1013.payload = 10
Robot.M1013.reach = 1_300
Robot.M1013.weight = 34.0
Robot.M1013.tool_speed = 1
Robot.M1013.repeatability = 0.05
Robot.M1013.temperature = 0, 45
Robot.M1013.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.M1013.joint_speed = [120,         # J1
                           120,         # J2
                           180,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Robot.M0617.payload = 6
Robot.M0617.reach = 1_700
Robot.M0617.weight = 35.5
Robot.M0617.tool_speed = 1
Robot.M0617.repeatability = 0.1
Robot.M0617.temperature = 0, 45
Robot.M0617.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-165, 165), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.M0617.joint_speed = [100,         # J1
                           100,         # J2
                           150,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Robot.M0609.payload = 6
Robot.M0609.reach = 900
Robot.M0609.weight = 27.5
Robot.M0609.tool_speed = 1
Robot.M0609.repeatability = 0.03
Robot.M0609.temperature = 0, 45
Robot.M0609.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-150, 150), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.M0609.joint_speed = [150,         # J1
                           150,         # J2
                           180,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Robot.A0912.payload = 9
Robot.A0912.reach = 1_200
Robot.A0912.weight = 31.0
Robot.A0912.tool_speed = 1
Robot.A0912.repeatability = 0.05
Robot.A0912.temperature = 0, 45
Robot.A0912.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.A0912.joint_speed = [180,         # J1
                           180,         # J2
                           180,         # J3
                           360,         # J4
                           360,         # J5
                           360]         # J6

Robot.A0509.payload = 9
Robot.A0509.reach = 900
Robot.A0509.weight = 21.0
Robot.A0509.tool_speed = 1
Robot.A0509.repeatability = 0.03
Robot.A0509.temperature = 0, 45
Robot.A0509.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Robot.A0509.joint_speed = [180,         # J1
                           180,         # J2
                           180,         # J3
                           360,         # J4
                           360,         # J5
                           360]         # J6


def rotated(iterable, start_index):
    """Rotate an iterable about a starting index.
    
    Arguments:
      iterable: an iterable object.
      start_index: an integer value.
      
    Returns:
      A chain object.
    """
    _iterable = iter(iterable)
    next(islice(_iterable, start_index, start_index), None)
    return chain(_iterable, islice(iterable, start_index))

def get_minimum_posj_from_posx(target, current=None, ref=DR_BASE):
    """Find the joint position which requires the minimum joint movement to
    achieve a target task position.
    
    Arguments:
      target: posx position.
      current: posj position or None, default=None. If None the current position
        is calculated.
      ref: DR reference constant, default=DR_BASE.
      
    Returns:
      posj
    """
    if current is None:
        current = get_current_posj()
    sums = [sum(abs(a - b) for a, b in zip(current, ikin(target, sol_space, ref)))
            for sol_space in SOLUTION_SPACES]
    return ikin(target, sums.index(min(sums)), ref)

def check_joint_limits(pos, joint_limits):
    """Check if a joint position exceeds the joint limits.
    
    Arguments:
      pos: posj joint position.
      joint_limits: a list of lower and upper bound joint limits.
      
    Returns:
      bool.
    """
    for joint, (lower_limit, upper_limit) in zip(pos, joint_limits):
        if not lower_limit < joint < upper_limit:
            return False
    return True

def matmul(A, B):
    """Multiply two matricies.
    
    Arguments:
      A: 2D Matrix.
      B: 2D Matrix.
      
    Returns:
      2D Matrix.
    """
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
