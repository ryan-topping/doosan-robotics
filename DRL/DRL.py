from __future__ import annotations
from typing import Optional, Union, overload

# On/Off
ON  = 1
OFF = 0

# Ref
DR_BASE  = 0
DR_TOOL  = 1
DR_WORLD = 2

# Seg_type
DR_LINE   = 0
DR_CIRCLE = 1

# Movement basis
DR_MV_MOD_ABS = 0
DR_MV_MOD_REL = 1

# Reactive motion mode
DR_MV_RA_DUPLICATE = 0
DR_MV_RA_OVERRIDE  = 1

# Application mode
DR_MV_APP_NONE = 0
DR_MV_APP_WELD = 1

# Message type
DR_PM_MESSAGE = 0
DR_PM_WARNING = 1
DR_PM_ALARM   = 2

# Input type
DR_VAR_INT    = 0
DR_VAR_FLOAT  = 1
DR_VAR_STR    = 2
DR_VAR_BOOL   = 3


# Motion-related Commands
class posj(list):
    """Joint space angle."""
    def __init__(self, 
                 J1: Union[float, list[float], posj] = 0,
                 J2: float = 0, J3: float = 0, J4: float = 0,
                 J5: float = 0, J6: float = 0) -> None:
        """This function designates the joint space angle in coordinate values.

        posj(J1=0, J2=0, J3=0, J4=0, J5=0, J6=0)
        """
class posx(list):
    """Task space coordinates."""
    def __init__(self,
                 X: Union[float, list[float], posx] = 0, 
                 Y: float = 0, Z: float = 0, A: float = 0, 
                 B: float = 0, C: float = 0) -> None:
        """This function designates the task space in coordinate values.

        posx(X=0, Y=0, Z=0, A=0, B=0, C=0)
        """
def trans(pos: Union[posx, list[float]], delta: Union[posx, list[float]], 
          ref_in: int, ref_out: int) -> posx:
    """pos (pose) defined based on the ref coordinate is moved/rotated by the 
    amount equal to delta, and then a value converted based on the ref_out 
    coordinate is returned. In case that the ref coordinate is the tool 
    coordinate, this function retuns the value based on input parameter(pos)'s 
    coordinate without ref_out coordinate.

    trans(pos, delta, ref_in, ref_out)
    """
class posb(list):
    """Constant-velocity blending motion task space coordinates."""
    def __init__(self, seg_type: int, posx1: posx, posx2: posx, 
                 radius: float = 0) -> None:
        """Input parameters for constant-velocity blending motion (moveb and 
        amoveb) with the Posb coordinates of each waypoint and the data of the 
        unit path type (line or arc) define the unit segment object of the 
        trajectory to be blended.
        Only posx1 is inputted if seg_type is a line (DR_LINE), and posx2 is also 
        inputted if seg_type is a circle (DR_CIRCLE). Radius sets the blending 
        radius with the continued segment.

        posb(seg_type, posx1, posx2=None, radius=0)
        """
def fkin(pos: Union[posj, list[float]], ref: int = DR_BASE) -> posx:
    """This function receives the input data of joint angles or equivalent 
    forms (float[6]) in the joint space and returns the TCP (objects in the 
    task space) based on the ref coordinate.

    fkin(pos, ref)
    """
def ikin(pos: posx, sol_space: int, ref: int) -> posj: ...
def addto(pos: Union[posj, list[float]], 
          add_val: Optional[list[float]] = None) -> posj: ...
def set_velj(vel: Union[float, list[float]]) -> int: ...
def set_accj(acc: Union[float, list[float]]) -> int: ...
@overload
def set_velx(vel1: float, vel2: float) -> int: ...
@overload
def set_velx(vel1: float) -> int: ...
@overload
def set_accx(acc1: float, acc2: float) -> int: ...
@overload
def set_accx(acc: float) -> int: ...
def set_tcp(name: str) -> int:
    """This function calls the name of the TCP registered in the Teach Pendant
    and sets it as the current TCP.

    Parameters:
        name (string): Name of the TCP registered in the TP
    
    Returns:
        value (int): 0 = Success, -value = Failed
    """
def set_ref_coord(coord: int) -> int: ...
def movej(pos: Union[posj, list[float]],
          *,
          vel: Optional[Union[float, list[float]]] = None,
          v: Optional[Union[float, list[float]]] = None,
          acc: Optional[Union[float, list[float]]] = None,
          a: Optional[Union[float, list[float]]] = None,
          time: Optional[float] = None,
          t: Optional[float] = None,
          radius: Optional[float] = None,
          r: Optional[float] = None,
          mod: int = DR_MV_MOD_ABS,
          ra: int = DR_MV_RA_DUPLICATE) -> int: ...
def movel(pos: Union[posx, list[float]],
          *,
          vel: Optional[Union[float, list[float]]] = None, # float, or 2 floats
          v: Optional[Union[float, list[float]]] = None,   # float, or 2 floats
          acc: Optional[Union[float, list[float]]] = None, # float, or 2 floats
          a: Optional[Union[float, list[float]]] = None,   # float, or 2 floats
          time: Optional[float] = None,
          t: Optional[float] = None,
          radius: Optional[float] = None,
          r: Optional[float] = None,
          ref: Optional[int] = None,
          mod: int = DR_MV_MOD_ABS,
          ra: int = DR_MV_RA_DUPLICATE,
          app_type: int = DR_MV_APP_NONE) -> int:
    """The robot moves along the straight line to the target position (pos) 
    within the task space.
    
    movel(pos, vel=None, acc=None, time=None, radius=None, ref=None, 
    mod=DR_MV_MOD_ABS, ra=DR_MV_RA_DUPLICATE, app_type=DR_MV_APP_NONE)

    Parameters:
        pos (posx or list[6 floats]): position.
        vel (v) (float or list[2 floats]) = None: velocity.
        acc (a) (float or list[2 floats]) = None: acceleration.
        time (t) (float) = None: reach time [seconds], if time is specified, 
        values are processed based on time, ignoring vel and acc.
        radius (r) (float) = None: radius for blending.
        ref (int) = None: reference coordinate; DR_BASE: base coordinate, 
        DR_WORLD: world coordinate, DR_TOOL: tool coordinate, 
        user_coordinate: user defined.
        mod (int) = DR_MV_MOD_ABS: Movement basis; DR_MV_MOD_ABS: absolute,
        DR_MV_MOD_REL: relative.
        ra (int) = DR_MV_RA_DUPLICATE: Reactive motion mode; 
        DR_MV_RA_DUPLICATE: duplicate, DR_MV_RA_OVERRIDE: override.
        app_type (int) = DR_MV_APP_NONE: Application mode; 
        DR_MV_APP_NONE: No application related, DR_MV_APP_WELD: Welding 
        application related.
    """

# Math Function
def inverse_pose(posx1: posx) -> posx:
    """This function returns the posx value that represents the inverse of posx.

    Parameters:
        posx1 (posx | list[6 floats]): position

    Returns:
        position (posx): inverse position.

    Exception:
        DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
    """

# Auxilliary Control Commands
def get_current_posj() -> posj: ...
def get_current_posx() -> tuple[posj, int]: ...

# System Commands
# System Commands > TP Interface Commands
def tp_popup(message: str, 
             pm_type: int = DR_PM_MESSAGE,
             button_type: int = 0) -> int:
    """This function provides a message to users through the Teach Pendant. The 
    higher level controller receives the string and displays it in the popup
    window, and the window must be closed by a user's confirmation.

    Parameters:
        message (str): Message provided to the user; limit 256 bytes.
        pm_type (int) = DR_PM_MESSAGE: Message type; DR_PM_MESSAGE, 
        DR_PM_WARNING, DR_PM_ALARM
        button_type (int) = 0: Button type of TP popup message; 0 = show Stop 
        and Resume button, 1 = show Stop button.

    Returns:
        value (int): 0 = Success, -value = Failed.
        
    Exception:
        DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
        DR_Error (DR_ERROR_VALUE): Parameter value is invalid.
        DR_Error (DR_ERROR_RUNTIME): C extension module error occured.
        DR_Error (ER_ERROR_STOP): Program terminated forcefully.
    """
def tp_log(message: str) -> int:
    """This function records the user-written log to the teach pendant.

    Parameters:
        message (str): Message provided to the user; limit 256 bytes.

    Returns:
        value (int): 0 = Success, -value = Failed.

    Exception:
        DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
        DR_Error (DR_ERROR_VALUE): Parameter value is invalid.
        DR_Error (DR_ERROR_RUNTIME): C extension module error occured.
        DR_Error (ER_ERROR_STOP): Program terminated forcefully.
    """
def tp_get_user_input(message: str, 
                      input_type: int) -> Union[int, float, str, bool]:
    """This function receives the user input data through the Teach Pendant.
    
    Parameters:
        message (str): Character string message to be displayed on the TP user
        input window.
        input_type (int): TP user input message type

    Returns:
        data (int or float or str or bool): user input data received from the TP.

    Exception:
        DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
        DR_Error (DR_ERROR_VALUE): Parameter value is invalid.
        DR_Error (DR_ERROR_RUNTIME): C extension module error occured.
        DR_Error (ER_ERROR_STOP): Program terminated forcefully.
    """
# System Commands > Other Commands
def wait(time: int) -> int:
    """This functionw aits for the specified time.

    Parameters:
        time (float): time in seconds.

    Returns:
        value (int): 0 = Success, -value = Failed.
    """
def drl_report_line(option: int) -> None:
    """This command is used to turn ON / OFF the execution line display function 
    when the DRL script is running. When the run line display function is turned 
    OFF, the time required to execute the run line display function is reduced, 
    which significantly speeds up the execution of the DRL.

    drl_report_line(option)

    The following features do not operate in the section where the execution 
    line display function is turned OFF.
    - Execution time display by line
    - Variable monitoring
    - System Variable Update
    - Step by Step in Debug mode
    - Brake Point in Debug mode

    Parameters:
        option (int):   Whether to display the DRL execution line
          ON(1), OFF(0)
    
    Returns:
        None
    """
