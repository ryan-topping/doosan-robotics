"""
Add the following data into  Robot Configuration > User Setting > Tool > TCP
"TOOL0": 0, 0, 0, 0, 0, 0
"TOOL1": 0, 40.4, 70, -90, -30, 90
"TOOL2": 38.40, 12.50, 70, 18, 30, -90
"TOOL3": 23.8, -32.8, 70, -54, 30, -90
"TOOL4": -23.80, -32.80, 70, -126, 30, -90
"TOOL5": -38.40, 12.5, 70, 162, 30, -90
"""
from DRL.DRL import *

drl_report_line(OFF)

# Functions
def change_tcp(name):
    a = posj(0, 0, 0, 0, 0, 0.1)
    b = posj(0, 0, 0, 0, 0, -0.1)
    set_tcp(name)
    movej(a, time=0.01, mod=DR_MV_MOD_REL)
    movej(b, time=0.01, mod=DR_MV_MOD_REL)
    
def pick(position_zero, tool_name, part_offset, approach_height):
    """Pick a part from the tray using variable tool (tcp) names, part_offset values,
    and approach height.
    
    Arguments:
      position_zero: posx     (0, 0) pick on the tray
      tool_name: string       tool name for the pick
      part_offset: posx       offset of the part
      approach_height: float  z distance above tray
    """
    tp_log("New pick, tool: " + tool_name + ", Part Offset: " + str(part_offset))
    change_tcp(tool_name)
    approach = posx(0, 0, approach_height, 0, 0, 0)
    depart   = inverse_pose(approach)
    pounce   = trans(trans(position_zero, approach), part_offset)
    movel(pounce,   time=2.0)
    movel(approach, time=1.0, mod=DR_MV_MOD_REL, ref=DR_TOOL)
    # engage vacuum or gripper here
    wait(0.5)
    movel(depart,   time=1.0, mod=DR_MV_MOD_REL, ref=DR_TOOL)
    
    
# Constant values
HOME  = posj(0, 0, 90, 0, 90, 0)
TOOL0 = "Tool0"
TOOL1 = "Tool1"
TOOL2 = "Tool2"
TOOL3 = "Tool3"
TOOL4 = "Tool4"
TOOL5 = "Tool5"
APPROACH_HEIGHT = 100

# Prep
set_velj(100)
set_accj(100)

# Move to home position
change_tcp(TOOL0)
movej(HOME)

# Test tool center point data
change_tcp(TOOL1)
change_tcp(TOOL2)
change_tcp(TOOL3)
change_tcp(TOOL4)
change_tcp(TOOL5)
change_tcp(TOOL0)

pos, _ = get_current_posx()
pos = trans(pos, posx(0, 0, -200, 0, 0, 0))

#Simulated 5 part pick with sample offset data:
part1 = posx( 50,  15, 0, 0, 0,  30)
part2 = posx(-50,  10, 0, 0, 0,  15)
part3 = posx(  0,  50, 0, 0, 0, 270)
part4 = posx( 20, -35, 0, 0, 0,  60)
part5 = posx(-50, -20, 0, 0, 0, 105)

pick(pos, TOOL1, part1, APPROACH_HEIGHT)
pick(pos, TOOL2, part2, APPROACH_HEIGHT)
pick(pos, TOOL3, part3, APPROACH_HEIGHT)
pick(pos, TOOL4, part4, APPROACH_HEIGHT)
pick(pos, TOOL5, part5, APPROACH_HEIGHT)