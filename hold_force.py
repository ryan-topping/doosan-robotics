# If using DART-Studio don't copy-paste this line
from DRL.DRL import *
# -----------------------------------------------


def hold(hold_force, axis, ref, hold_time, timeout, time_step):
    """Hold a force with the robot in the given axis, in the reference frame
    for the time specified with hold time.

    Parameters:
        - hold_force (float or int): A target force in Neutons.
        - axis (int): The axis to measure the force.
        - ref (int): Reference frame.
        - hold_time (float or int): The amount of time in seconds to hold.
        - timeout (float or int): The amount of time to allow before achieving 
        the required force.
        - time_step (float or int): The often to evaluate the force in seconds.
    
    Returns:    
        - success (bool): Whether or not the function succeeded in holding the 
        required force for the required amount of time.
        - held_time (float): The amount of time the required force was held.
        - max_force (float): The maximum force measured.

    Example:
        hold(hold_force=50, axis=DR_AXIS_Z, ref=DR_WORLD, hold_time=3.0,
             timeout=5.0, time_step=0.1)
            Tries to hold a 50 Neuton force in the Z axis relative to the world
            frame. Holds for 3 seconds. Allows 5 seconds to achieve the
            required force. Checks 10 times a second.
    """
    success = False
    held_time = 0
    max_force = 0

    while True:
        measured_forces = get_tool_force(ref)
        measured_axis_force = measured_forces[axis]
        max_force = max(max_force, measured_axis_force)

        if measured_axis_force >= hold_force:
            held_time += time_step
        else:
            timeout -= time_step

        if held_time >= hold_time:
            success = True
            break

        if timeout <= 0:
            break

        wait(time_step)

    return success, held_time, max_force
