from __future__ import annotations
from typing import Optional, Union, overload


# On/Off
ON = 1
OFF = 0

# Ref
DR_BASE = 0
DR_TOOL = 1
DR_WORLD = 2

# Seg_type
DR_LINE = 0
DR_CIRCLE = 1

# Movement basis
DR_MV_MOD_ABS = 0
DR_MV_MOD_REL = 1

# Reactive motion mode
DR_MV_RA_DUPLICATE = 0
DR_MV_RA_OVERRIDE = 1

# Application mode
DR_MV_APP_NONE = 0
DR_MV_APP_WELD = 1

# Orientation mode
DR_MV_ORI_TEACH = 0
DR_MV_ORI_FIXED = 1
DR_MV_ORI_RADIAL = 2

# Velocity option
DR_MVS_VEL_NONE = 0
DR_MVS_VEL_CONST = 1

# Axis
DR_AXIS_X = 0
DR_AXIS_Y = 1
DR_AXIS_Z = 2

# Check motion state
DR_STATE_IDLE = 0   # no motion in action
DR_STATE_INIT = 1   # motion being calculated
DR_STATE_BUSY = 2   # motion in operation

# Target home position
DR_HOME_TARGET_MECHANIC = 0
DR_HOME_TARGET_USER = 1

# Stop mode
DR_QSTOP_STO = 0    # Quick stop (category 1) without STO (safe torque off)
DR_QSTOP = 1        # Quick stop (category 2)
DR_SSTOP = 2        # Soft stop
DR_HOLD = 3         # HOLE stop

# Message type
DR_PM_MESSAGE = 0
DR_PM_WARNING = 1
DR_PM_ALARM = 2

# Input type
DR_VAR_INT = 0
DR_VAR_FLOAT = 1
DR_VAR_STR = 2
DR_VAR_BOOL = 3

# None Condition
DR_COND_NONE = -10_000

SERIAL_BAUDRATES = 2_400, 4_800, 9_600, 19_200, 38_400, 57_600, 115_200

# Byte size
DR_FIVEBITS = 5
DR_SIXBITS = 6
DR_SEVENBITS = 7
DR_EIGHTBITS = 8

# Parity checking
DR_PARITY_NONE = 'N'
DR_PARITY_EVEN = 'E'
DR_PARITY_ODD = 'O'
DR_PARITY_MARK = 'M'
DR_PARITY_SPACE = 'S'

# Number of stop bits
DR_STOPBITS_ONE = 1.0
DR_STOPBITS_ONE_POINT_FIVE = 1.5
DR_STOPBITS_TWO = 2.0


# Motion-related Commands
class posj(list):
    '''Joint space position, joint angles.'''
    def __init__(self, 
                 J1: Union[float, list[float], posj] = 0,
                 J2: float = 0, 
                 J3: float = 0, 
                 J4: float = 0,
                 J5: float = 0, 
                 J6: float = 0) -> None: ...
class posx(list):
    '''Task space position, coordinates.'''
    def __init__(self,
                 X: Union[float, list[float], posx] = 0, 
                 Y: float = 0, 
                 Z: float = 0, 
                 A: float = 0, 
                 B: float = 0, 
                 C: float = 0) -> None:
        '''This function designates the task space in coordinate values.

        posx(X=0, Y=0, Z=0, A=0, B=0, C=0)
        '''
def trans(pos: Union[posx, list[float]], 
          delta: Union[posx, list[float]], 
          ref_in: int, 
          ref_out: int) -> posx:
    '''pos (pose) defined based on the ref coordinate is moved/rotated by the 
    amount equal to delta, and then a value converted based on the ref_out 
    coordinate is returned. In case that the ref coordinate is the tool 
    coordinate, this function retuns the value based on input parameter(pos)'s 
    coordinate without ref_out coordinate.

    trans(pos, delta, ref_in, ref_out)
    '''
class posb(list):
    '''Constant-velocity blending motion task space coordinates.'''
    def __init__(self, 
                 seg_type: int, 
                 posx1: posx, 
                 posx2: posx, 
                 radius: float = 0) -> None:
        '''Input parameters for constant-velocity blending motion (moveb and 
        amoveb) with the Posb coordinates of each waypoint and the data of the 
        unit path type (line or arc) define the unit segment object of the 
        trajectory to be blended.
        Only posx1 is inputted if seg_type is a line (DR_LINE), and posx2 is also 
        inputted if seg_type is a circle (DR_CIRCLE). Radius sets the blending 
        radius with the continued segment.

        posb(seg_type, posx1, posx2=None, radius=0)
        '''
def fkin(pos: Union[posj, list[float]], 
         ref: int = DR_BASE) -> posx:
    '''This function receives the input data of joint angles or equivalent 
    forms (float[6]) in the joint space and returns the TCP (objects in the 
    task space) based on the ref coordinate.

    fkin(pos, ref)
    '''
def ikin(pos: posx, 
         sol_space: int, 
         ref: int) -> posj: ...
def addto(pos: Union[posj, list[float]], 
          add_val: Optional[list[float]] = None) -> posj: ...
def set_velj(vel: Union[float, list[float]]) -> int:
    '''This function sets the global velocity in joint motion (movej, movejx, 
    amovej, or amovejx) after using this command. The default velocity is 
    applied to the globall set vel if movej() is called without the explicit
    input of the velocity argument.

    Parameters:
        - vel (float or list[float*6]): velocity for all axes or velocity to 
        each axis in degrees per second.

    Returns:
        - value (int): 0 = Success.

    Exceptions:
        - DR_Error (ER_ERROR_TYPE): Parameter data type error occurred.
    '''
def set_accj(acc: Union[float, list[float]]) -> int: ...
@overload
def set_velx(vel1: float, vel2: float) -> int: ...
@overload
def set_velx(vel1: float) -> int: ...
@overload
def set_accx(acc1: float, 
             acc2: float) -> int: ...
@overload
def set_accx(acc: float) -> int: ...
def set_tcp(name: str) -> int:
    '''This function calls the name of the TCP registered in the Teach Pendant
    and sets it as the current TCP.

    Parameters:
        - name (string): Name of the TCP registered in the TP
    
    Returns:
        - value (int): 0 = Success, negative value = Failed
    '''
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
          vel: Optional[Union[float, list[float]]] = None,
          v: Optional[Union[float, list[float]]] = None,
          acc: Optional[Union[float, list[float]]] = None,
          a: Optional[Union[float, list[float]]] = None,
          time: Optional[float] = None,
          t: Optional[float] = None,
          radius: Optional[float] = None,
          r: Optional[float] = None,
          ref: Optional[int] = None,
          mod: int = DR_MV_MOD_ABS,
          ra: int = DR_MV_RA_DUPLICATE,
          app_type: int = DR_MV_APP_NONE) -> int:
    '''The robot moves along the straight line to the target position (pos) 
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
    '''
def movejx(pos: Union[posx, list[float]],
           *,
           vel: Optional[Union[float, list[float]]] = None,
           v: Optional[Union[float, list[float]]] = None,
           acc: Optional[Union[float, list[float]]] = None,
           a: Optional[Union[float, list[float]]] = None,
           time: Optional[float] = None,
           t: Optional[float] = None,
           radius: Optional[float] = None,
           r: Optional[float] = None,
           ref: Optional[int] = None,
           mod: int = DR_MV_MOD_ABS,
           ra: int = DR_MV_RA_DUPLICATE,
           sol: int = 0) -> int: ...
def movec(pos: Union[posx, list[float]],
          pos2: Union[posx, list[float]],
          *,
          vel: Optional[Union[float, list[float]]] = None,
          v: Optional[Union[float, list[float]]] = None,
          acc: Optional[Union[float, list[float]]] = None,
          a: Optional[Union[float, list[float]]] = None,
          time: Optional[float] = None,
          t: Optional[float] = None,
          radius: Optional[float] = None,
          r: Optional[float] = None,
          ref: Optional[int] = None,
          mod: int = DR_MV_MOD_ABS,
          angle: Optional[Union[float, list[float]]] = None,
          an: Optional[Union[float, list[float]]] = None,
          ra: int = DR_MV_RA_DUPLICATE,
          ori: int = DR_MV_ORI_TEACH,
          app_type: int = DR_MV_APP_NONE) -> int:
    '''
    Parameters:
        - pos (posx or list[6 floats]): position.
        - vel (v) Optional(float or list[2 floats]) = None: velocity.
        - acc (a) Optional(float or list[2 floats]) = None: acceleration.
        - time (t) Optional(float) = None: reach time [seconds], if time is 
        specified, values are processed based on time, ignoring vel and acc.
        - radius (r) Optional(float) = None: radius for blending.
        - ref Optional(int) = None: reference coordinate; DR_BASE: base 
        coordinate, DR_WORLD: world coordinate, DR_TOOL: tool coordinate, 
        user_coordinate: user defined.
        - mod (int) = DR_MV_MOD_ABS: Movement basis; DR_MV_MOD_ABS: absolute,
        DR_MV_MOD_REL: relative.
        - angle (an) Optional(float or list[2 floats]) = None: angle, or angle1,
        angle2
        - ra (int) = DR_MV_RA_DUPLICATE: Reactive motion mode; 
        DR_MV_RA_DUPLICATE: duplicate, DR_MV_RA_OVERRIDE: override.
        - ori (int) = DR_MV_ORI_TEACH: Orientation mode; DR_MV_ORI_TEACH 
        orientation changes continuously from the initial to the final taught
        value, DR_MV_ORI_FIXED orientation holds with the initial orientation,
        DR_MV_ORI_RADIAL orientation changes radially from the initial value.
        - app_type (int) = DR_MV_APP_NONE: Application mode; 
        DR_MV_APP_NONE: No application related, DR_MV_APP_WELD: Welding 
        application related.
    '''
def movesj(pos_list: list[posj],
           *,
           vel: Optional[float] = None,
           v: Optional[float] = None,
           acc: Optional[float] = None,
           a: Optional[float] = None,
           time: Optional[float] = None,
           t: Optional[float] = None,
           mod: int = DR_MV_MOD_ABS) -> int: ...
def movesx(pos_list: list[posx],
           *,
           vel: Optional[Union[float, list[float]]] = None,
           v: Optional[Union[float, list[float]]] = None,
           acc: Optional[Union[float, list[float]]] = None,
           a: Optional[Union[float, list[float]]] = None,
           time: Optional[float] = None,
           t: Optional[float] = None,
           ref: Optional[int] = None,
           mod: int = DR_MV_MOD_ABS,
           vel_opt: int = DR_MVS_VEL_NONE) -> int: ...
def moveb(pos_list: list[posb],
          *,
          vel: Optional[Union[float, list[float]]] = None,
          v: Optional[Union[float, list[float]]] = None,
          acc: Optional[Union[float, list[float]]] = None,
          a: Optional[Union[float, list[float]]] = None,
          time: Optional[float] = None,
          t: Optional[float] = None,
          ref: Optional[int] = None,
          mod: int = DR_MV_MOD_ABS,
          app_type: int = DR_MV_APP_NONE) -> int: ...
def move_spiral(rev: float = 10.0,
                rmax: float = 10.0,
                lmax: float = 0.0,
                vel: Optional[float] = None,
                v: Optional[float] = None,
                acc: Optional[float] = None,
                a: Optional[float] = None,
                time: Optional[float] = None,
                t: Optional[float] = None,
                axis: int = DR_AXIS_Z,
                ref: int = DR_TOOL) -> int: ...
def move_periodic(amp: list[float],
                  period: Union[float, list[float]],
                  atime: float = 0.0,
                  repeat: int = 1,
                  ref: int = DR_TOOL) -> int: ...
def move_home(target: int) -> int: ...
def amovej(pos: Union[posj, list[float]],
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
def amovel(pos: Union[posx, list[float]],
           *,
           vel: Optional[Union[float, list[float]]] = None,
           v: Optional[Union[float, list[float]]] = None,
           acc: Optional[Union[float, list[float]]] = None,
           a: Optional[Union[float, list[float]]] = None,
           time: Optional[float] = None,
           t: Optional[float] = None,
           radius: Optional[float] = None,
           r: Optional[float] = None,
           ref: Optional[int] = None,
           mod: int = DR_MV_MOD_ABS,
           ra: int = DR_MV_RA_DUPLICATE,
           app_type: int = DR_MV_APP_NONE) -> int: ...
def amovejx(pos: Union[posx, list[float]],
            *,
            vel: Optional[Union[float, list[float]]] = None,
            v: Optional[Union[float, list[float]]] = None,
            acc: Optional[Union[float, list[float]]] = None,
            a: Optional[Union[float, list[float]]] = None,
            time: Optional[float] = None,
            t: Optional[float] = None,
            radius: Optional[float] = None,
            r: Optional[float] = None,
            ref: Optional[int] = None,
            mod: int = DR_MV_MOD_ABS,
            ra: int = DR_MV_RA_DUPLICATE,
            sol: int = 0) -> int: ...
def amovec(pos: Union[posx, list[float]],
           pos2: Union[posx, list[float]],
           *,
           vel: Optional[Union[float, list[float]]] = None,
           v: Optional[Union[float, list[float]]] = None,
           acc: Optional[Union[float, list[float]]] = None,
           a: Optional[Union[float, list[float]]] = None,
           time: Optional[float] = None,
           t: Optional[float] = None,
           radius: Optional[float] = None,
           r: Optional[float] = None,
           ref: Optional[int] = None,
           mod: int = DR_MV_MOD_ABS,
           angle: Optional[Union[float, list[float]]] = None,
           an: Optional[Union[float, list[float]]] = None,
           ra: int = DR_MV_RA_DUPLICATE,
           ori: int = DR_MV_ORI_TEACH,
           app_type: int = DR_MV_APP_NONE) -> int: ...
def amovesj(pos_list: list[posj],
            *,
            vel: Optional[float] = None,
            v: Optional[float] = None,
            acc: Optional[float] = None,
            a: Optional[float] = None,
            time: Optional[float] = None,
            t: Optional[float] = None,
            mod: int = DR_MV_MOD_ABS) -> int: ...
def amovesx(pos_list: list[posx],
            *,
            vel: Optional[Union[float, list[float]]] = None,
            v: Optional[Union[float, list[float]]] = None,
            acc: Optional[Union[float, list[float]]] = None,
            a: Optional[Union[float, list[float]]] = None,
            time: Optional[float] = None,
            t: Optional[float] = None,
            ref: Optional[int] = None,
            mod: int = DR_MV_MOD_ABS,
            vel_opt: int = DR_MVS_VEL_NONE) -> int: ...
def amoveb(pos_list: list[posb],
           *,
           vel: Optional[Union[float, list[float]]] = None,
           v: Optional[Union[float, list[float]]] = None,
           acc: Optional[Union[float, list[float]]] = None,
           a: Optional[Union[float, list[float]]] = None,
           time: Optional[float] = None,
           t: Optional[float] = None,
           ref: Optional[int] = None,
           mod: int = DR_MV_MOD_ABS,
           app_type: int = DR_MV_APP_NONE) -> int: ...
def amove_spiral(rev: float = 10.0,
                 rmax: float = 10.0,
                 lmax: float = 0.0,
                 vel: Optional[float] = None,
                 v: Optional[float] = None,
                 acc: Optional[float] = None,
                 a: Optional[float] = None,
                 time: Optional[float] = None,
                 t: Optional[float] = None,
                 axis: int = DR_AXIS_Z,
                 ref: int = DR_TOOL) -> int: ...
def amove_periodic(amp: list[float],
                   period: Union[float, list[float]],
                   atime: float = 0.0,
                   repeat: int = 1,
                   ref: int = DR_TOOL) -> int: ...
def mwait(time: float) -> int: ...
def begin_blend(radius: float = 0.0) -> int: ...
def end_blend() -> int: ...
def check_motion() -> int: ...
def stop(st_mode: int) -> int: ...
def change_operation_speed(speed: int) -> int:
    '''This function adjusts the operation velocity. The argument is the
    relative velocity in a percentage of the currently set velocity and has a 
    value from 1 to 100. Therefore, a value of 50 means that the velocity is
    to 50% of the currently set velocity.

    Parameters:
        - speed (int): operation speed (10~100)

    Returns:
        - value (int): 0 = Success, negative value = Failed
    
    Exception:
        - DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
        - DR_Error (DR_ERROR_VALUE): Parameter value is invalid.
        - DR_Error (DR_ERROR_RUNTIME): C extension module error occured.
        - DR_Error (ER_ERROR_STOP): Program terminated forcefully.
    '''
def wait_manual_guide(): ...
def wait_nudge(): ...
def enable_alter_motion(): ...
def alter_motion(): ...
def disable_alter_motion(): ...
def servoj(): ...
def servol(): ...
def speedj(): ...
def speedl(): ...

# Math Function
def inverse_pose(posx1: posx) -> posx:
    '''This function returns the posx value that represents the inverse of posx.

    Parameters:
        - posx1 (posx | list[6 floats]): position

    Returns:
        - position (posx): inverse position.

    Exception:
        - DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
    '''

# Auxilliary Control Commands
def get_control_mode(): ...
def get_control_space(): ...
def get_current_posj() -> posj: ...
def get_current_velj(): ...
def get_desired_posj(): ...
def get_desired_velj(): ...
def get_current_posx() -> tuple[posj, int]: ...
def get_current_tool_flange_posx(): ...
def get_current_velx(): ...
def get_desired_posx(): ...
def get_current_solution_space(): ...
def get_current_rotm(): ...
def get_joint_torque(): ...
def get_external_torque(): ...
def get_tool_force(): ...
def get_solution_space(): ...
def get_orientation_error(): ...

# 5. Other Settings Commands
def get_workpiece_weight(): ...
def reset_workpiece_weight(): ...
def set_workpiece_weight(): ...
def set_tool(): ...
def set_tool_shape(): ...
# 5.2 Control Mode Settings
def set_singularity_handling(): ...
def set_singular_handling_force(): ...
def set_palletizing_mode(): ...
def set_motion_end(): ...

# 6. Force Control and Other Commands
# 6.1 Force/Compliance Control
def release_compliance_ctrl(): ...
def task_compliance_ctrl(): ...
def set_stiffnessx(): ...
def set_desired_force(): ...
def release_force(): ...
def get_force_control_state(): ...
def set_damping_factor(): ...
def set_force_factor(): ...
# 6.2 User-friendly Functions
@overload
def parallel_axis(x1: Union[posx, list[float]],
                  x2: Union[posx, list[float]],
                  x3: Union[posx, list[float]],
                  axis: int,
                  ref: int = DR_BASE) -> int: ...
@overload
def parallel_axis(vect: list[float],
                  axis: int,
                  ref: int = DR_BASE) -> int: ...
@overload
def align_axis(x1: Union[posx, list[float]],
               x2: Union[posx, list[float]],
               x3: Union[posx, list[float]],
               pos: Union[posx, list[float]],
               axis: int,
               ref: int = DR_BASE) -> int: ...
@overload
def align_axis(vect: list[float],
               pos: Union[posx, list[float]],
               axis: int,
               ref: int = DR_BASE) -> int: ...
def is_done_bolt_tightening(): ...

def set_stiffnessx(): ...
def calc_coord(): ...
@overload
def set_user_cart_coord(pos: Union[posx, list[float]],
                        ref: int) -> int: ...
@overload
def set_user_cart_coord(x1: Union[posx, list[float]],
                        x2: Union[posx, list[float]],
                        x3: Union[posx, list[float]],
                        pos: Union[posx, list[float]],
                        ref: int = DR_BASE) -> int: ...
@overload
def set_user_cart_coord(u1: list[float],
                        v1: list[float],
                        pos: Union[posx, list[float]],
                        ref: int = DR_BASE) -> int: ...
def overwrite_user_cart_coord(): ...
def get_user_cart_coord(): ...
def check_position_condition(): ...
def check_force_condition(): ...
@overload
def check_orientation_condition(axis: int,
                                min: Union[posx, list[float]],
                                max: Union[posx, list[float]],
                                ref: Optional[int] = None,
                                mod: int = DR_MV_MOD_ABS) -> bool: ...
@overload
def check_orientation_condition(axis: int,
                                min: float = DR_COND_NONE,
                                max: float = DR_COND_NONE,
                                ref: Optional[int] = None,
                                mod: int = DR_MV_MOD_REL) -> bool: ...
def coord_transform(): ...

# 7. System Commands
# 7.1 IO Related
def set_digital_output(index, 
                       val = None): ...
@overload
def set_digital_outputs(bit_list): ...
@overload
def set_digital_outputs(bit_start, 
                        bit_end, 
                        val): ...
def set_digital_output(index,
                       val = None,
                       time = None,
                       val2 = None): ...
def get_digital_input(index): ...
@overload
def get_digital_inputs(bit_list): ...
@overload
def get_digital_inputs(bit_start, 
                       bit_end): ...
def wait_digital_input(index,
                       val,
                       timeout = None): ...
@overload
def set_tool_digital_output(index,
                            val = None): ...
@overload
def set_tool_digital_outputs(bit_list): ...
@overload
def set_tool_digital_outputs(bit_start, 
                             bit_end,
                             val): ...
@overload
def set_tool_digital_output(index,
                            val = None,
                            time = None,
                            val2 = None): ...
def get_tool_digital_input(index): ...
@overload
def get_tool_digital_inputs(bit_list): ...
@overload
def get_tool_digital_inputs(bit_start, 
                            bit_end): ...
def wait_tool_digital_input(index,
                            val,
                            timeout = None): ...
def set_mode_analog_output(ch,
                           mod): ...
def set_mode_analog_input(ch,
                          mod): ...
def set_analog_output(ch,
                      val): ...
def get_analog_input(ch): ...
def set_output(port_type,
               index,
               val = None,
               time = None,
               val2 = None): ...
def get_input(port_type,
              index): ...
def wait_input(port_type,
               index,
               val,
               timeout = None,
               condition = None): ...
def wait_analog_input(ch,
                      condition,
                      val,
                      timeout = None): ...
def wait_tool_analog_input(ch,
                           condition,
                           val,
                           timeout = None): ...

# 7.2 TP Interface
def tp_popup(message: str, 
             pm_type: int = DR_PM_MESSAGE,
             button_type: int = 0) -> int:
    '''This function provides a message to users through the Teach Pendant. The 
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
    '''
def tp_log(message: str) -> int:
    '''This function records the user-written log to the teach pendant.

    Parameters:
        - message (str): Message provided to the user; limit 256 bytes.

    Returns:
        - value (int): 0 = Success, negative value = Failed.

    Exception:
        - DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
        - DR_Error (DR_ERROR_VALUE): Parameter value is invalid.
        - DR_Error (DR_ERROR_RUNTIME): C extension module error occured.
        - DR_Error (ER_ERROR_STOP): Program terminated forcefully.
    '''
def tp_get_user_input(message: str, 
                      input_type: int) -> Union[int, float, str, bool]:
    '''This function receives the user input data through the Teach Pendant.
    
    Parameters:
        - message (str): Character string message to be displayed on the TP user
        input window.
        - input_type (int): TP user input message type

    Returns:
        - data (int or float or str or bool): user input data received from the TP.

    Exception:
        - DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
        - DR_Error (DR_ERROR_VALUE): Parameter value is invalid.
        - DR_Error (DR_ERROR_RUNTIME): C extension module error occured.
        - DR_Error (ER_ERROR_STOP): Program terminated forcefully.
    '''
# 7.3 Thread
def thread_run(th_func_name,
               loop = False): ...
def thread_stop(th_id): ...
def thread_pause(th_id): ...
def thread_resume(th_id): ...
def thread_state(th_id): ...

# 7.4 Others
def wait(time: int) -> int:
    '''This functionw aits for the specified time.

    Parameters:
        - time (float): time in seconds.

    Returns:
        - value (int): 0 = Success, negative value = Failed.
    '''
def exit(): ...
def sub_program_run(name): ...
def drl_report_line(option: int) -> None:
    '''This command is used to turn ON / OFF the execution line display function 
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
        - option (int):   Whether to display the DRL execution line
        ON(1), OFF(0)
    
    Returns:
        - None
    '''
def set_fm(key,
           value): ...
def get_robot_model(): ...
def get_robot_serial_num(): ...
def check_robot_jts(): ...
def check_robot_fts(): ...
def start_timer(): ...
def end_timer(): ...

# 8 Mathematical Function
# 8.1 Basic Function
def ceil(x): ...
def floor(x): ...
def pow(x, y): ...
def sqrt(x): ...
def log(x, b): ...
def d2r(x): ...
def r2d(x): ...
def random(): ...

# 8.2 Trigonometric Functions
def sin(x): ...
def cos(x): ...
def tan(x): ...
def asin(x): ...
def acos(x): ...
def atan(x): ...
def atan2(y, x): ...

# 8.3 Linear algebra
def norm(x): ...
def rotx(angle): ...
def roty(angle): ...
def rotz(angle): ...
def rotm2eul(rotm): ...
def rotm2rotvec(rotm): ...
def eul2rotm(eul): ...
def eul2rotvec(eul): ...
def eul2rpy(eul): ...
def rpy2eul(rpy): ...
def rotvec2eul(rotvec): ...
def rotvec2rotm(rotvec): ...
def htrans(posx1, posx2): ...
def get_intermediate_pose(posx1, posx2, alpha): ...
def get_distance(posx1, posx2): ...
def get_normal(x1, x2, x3): ...
def add_pose(posx1, posx2): ...
def subtract_pose(posx1, posx2): ...
def inverse_pose(posx1): ...
def dot_pose(posx1, posx2): ...
def cross_pose(posx1, posx2): ...
def unit_pose(posx1): ...

# 9 External Communication Commands
# 9.1 Serial
def serial_open(port: Optional[str] = None,
                baudrate: int = 115_200,
                bytesize: int = DR_EIGHTBITS,
                parity: str = DR_PARITY_NONE,
                stopbits: float = DR_STOPBITS_ONE):
    '''This function opens a serial communication port.
    
    Parameters:
        - port Optional(str) = None: D-sub (9-pin) connection "COM", 
        USB to Serial Connection "COM_USB".
        - baudrate (int) = 115200: Baudrate.
        - bytesize (int) = DR_EIGHTBITS: Number of data bits DR_FIVEBITS, 
        DR_SIXBITS, DR_SEVENBITS, DR_EIGHTBITS.
        - parity (str) = DR_PARITY_NONE: Parity checking DR_PARITY_NONE,
        DR_PARITY_EVEN, DR_PARITY_ODD, DR_PARITY_MARK, DR_PARITY_SPACE.
        - stopbits (float) = DR_STOPBITS_ONE: Number of stop bits 
        DR_STOPBITS_ONE, DR_STOPBITS_ONE_POINT_FIVE, DR_STOPBITS_TWO.
        
    Returns:
        - serial.Serial instance.

    Exceptions:
        - DR_Error (DR_ERROR_TYPE): Parameter data type error occured.
        - DR_Error (DR_ERROR_VALUE): Parameter value is invalid.
        - DR_Error (DR_ERROR_RUNTIME): Serial.SerialException error occurred.
    '''
# 9.2 TCP/Client

# 9.3 TCP/Server
