'''A series of useful utilities for programming a Doosan robot with Doosan
Robotics Language (DRL).'''
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


def rotated(iterable, start_index):
    '''Rotate an iterable about a starting index.
    
    Parameters:
        - iterable (iterable): an iterable object with integer elements.
        - start_index (int): an integer value.
      
    Returns:
        - object (chain): A chain object.
    
    Example:
        rotated([0, 1, 2, 3], 2) -> chain([2, 3], [0, 1])
    '''
    _iterable = iter(iterable)
    next(islice(_iterable, start_index, start_index), None)
    
    return chain(_iterable, islice(iterable, start_index))

def get_minimum_posj_from_posx(target, current = None, ref = DR_BASE):
    '''Find the joint position which requires the minimum joint movement to
    achieve a target task position.
    
    Parameters:
        - target (posx): Target task position.
        - current (posj): Start position or None, default=None. If None the 
        current position is calculated.
        - ref (int): DR reference constant, default=DR_BASE, other options are
        DR_WORLD, and user coordinate index.
      
    Returns:
        - position (posj): joint position
    '''
    if current is None:
        current = get_current_posj()

    sums = [sum(abs(a - b) for a, b in zip(current, ikin(target, solution, ref)))
            for solution in SOLUTION_SPACES]
    
    return ikin(target, sums.index(min(sums)), ref)

def check_joint_limits(joint_position, joint_limits):
    '''Check if a joint position exceeds the joint limits.
    
    Arguments:
        - position (posj): Joint position.
        - joint_limits (list[tuple[int, int]]): a list of lower and upper bound 
        joint limits.
      
    Returns:
        - value (bool): True if all joint angles are within limits, else False.
    '''
    for joint, (lower_limit, upper_limit) in zip(joint_position, joint_limits):
        if not lower_limit < joint < upper_limit:
            return False
        
    return True

def matmul(A, B):
    '''Multiply two matricies. Returns AxB.

    Both A and B must be 2-dimensional array-like structures with an equal
    number of elements in each row. Further, the number of columns in A must
    be equal to the number of rows in B.
    
    Parameters:
        - A (array-like list of lists or similar): 2D Matrix.
        - B (array-like list of lists or similar): 2D Matrix.
      
    Returns:
        - matrix (list of lists): 2D Matrix of size A-rows x B-cols.

    Exception:
        - ValueError: If A and B are not array-like and their dimensions do not 
        conform to the rules of matrix multiplication a ValueError is raised.
    '''
    def array_like(array):
        _iter = iter(array)
        length = len(next(_iter))
        if not all(len(row) == length for row in _iter):
            return False
        return True
    
    if not array_like(A) or not array_like(B):
        raise ValueError("A and B must be array-like structures with an " \
                         "equal number of elements in each row.")
    if len(A[0]) != len(B):
        raise ValueError("For matrix multiplication the number of columns in " \
                         "A must be equal to the number of rows in B.")
    
    return [[sum(a*b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
