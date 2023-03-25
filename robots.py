from enum import Enum


class Model(Enum):
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

Model.H2515.payload = 25
Model.H2515.reach = 1_500
Model.H2515.weight = 77.0
Model.H2515.tool_speed = 1
Model.H2515.repeatability = 0.1
Model.H2515.temperature = 0, 45
Model.H2515.joint_range = [(-360, 360), # J1
                           (-125, 125), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.H2515.joint_speed = [100,         # J1
                           80,          # J2
                           100,         # J3
                           180,         # J4
                           180,         # J5
                           180]         # J6

Model.H2017.payload = 20
Model.H2017.reach = 1_700
Model.H2017.weight = 79.0
Model.H2017.tool_speed = 1
Model.H2017.repeatability = 0.1
Model.H2017.temperature = 0, 45
Model.H2017.joint_range = [(-360, 360), # J1
                           (-125, 125), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.H2017.joint_speed = [100,         # J1
                           80,          # J2
                           100,         # J3
                           180,         # J4
                           180,         # J5
                           180]         # J6

Model.M1509.payload = 15
Model.M1509.reach = 900
Model.M1509.weight = 33.0
Model.M1509.tool_speed = 1
Model.M1509.repeatability = 0.03
Model.M1509.temperature = 0, 45
Model.M1509.joint_range = [(-360, 360), # J1
                           (-125, 125), # J2
                           (-150, 150), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.M1509.joint_speed = [150,         # J1
                           150,          # J2
                           180,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Model.M1013.payload = 10
Model.M1013.reach = 1_300
Model.M1013.weight = 34.0
Model.M1013.tool_speed = 1
Model.M1013.repeatability = 0.05
Model.M1013.temperature = 0, 45
Model.M1013.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.M1013.joint_speed = [120,         # J1
                           120,         # J2
                           180,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Model.M0617.payload = 6
Model.M0617.reach = 1_700
Model.M0617.weight = 35.5
Model.M0617.tool_speed = 1
Model.M0617.repeatability = 0.1
Model.M0617.temperature = 0, 45
Model.M0617.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-165, 165), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.M0617.joint_speed = [100,         # J1
                           100,         # J2
                           150,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Model.M0609.payload = 6
Model.M0609.reach = 900
Model.M0609.weight = 27.5
Model.M0609.tool_speed = 1
Model.M0609.repeatability = 0.03
Model.M0609.temperature = 0, 45
Model.M0609.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-150, 150), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.M0609.joint_speed = [150,         # J1
                           150,         # J2
                           180,         # J3
                           225,         # J4
                           225,         # J5
                           225]         # J6

Model.A0912.payload = 9
Model.A0912.reach = 1_200
Model.A0912.weight = 31.0
Model.A0912.tool_speed = 1
Model.A0912.repeatability = 0.05
Model.A0912.temperature = 0, 45
Model.A0912.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.A0912.joint_speed = [180,         # J1
                           180,         # J2
                           180,         # J3
                           360,         # J4
                           360,         # J5
                           360]         # J6

Model.A0509.payload = 9
Model.A0509.reach = 900
Model.A0509.weight = 21.0
Model.A0509.tool_speed = 1
Model.A0509.repeatability = 0.03
Model.A0509.temperature = 0, 45
Model.A0509.joint_range = [(-360, 360), # J1
                           (-360, 360), # J2
                           (-160, 160), # J3
                           (-360, 360), # J4
                           (-360, 360), # J5
                           (-360, 360)] # J6
Model.A0509.joint_speed = [180,         # J1
                           180,         # J2
                           180,         # J3
                           360,         # J4
                           360,         # J5
                           360]         # J6