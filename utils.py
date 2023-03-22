"""A series of useful utilities for programming a Doosan robot with Doosan
Robotics Language (DRL)."""

from itertools import chain, islice
from DRL.DRL import *


SOL_SPACES = 0, 1, 2, 3, 4, 5, 6, 7

J1 = -360, 360
J2 =  -95,  95
J3 = -135, 135
J4 = -360, 360
J5 = -135, 135
J6 = -360, 360

JOINT_LIMITS = J1, J2, J3, J4, J5, J6

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
            for sol_space in SOL_SPACES]
    return ikin(target, sums.index(min(sums)), ref)

def check_joint_limits(pos, joint_limits=JOINT_LIMITS):
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
