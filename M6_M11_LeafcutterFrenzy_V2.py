from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE

async def M6_M11():    
    set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=900,
        straight_acceleration=900,
        turn_rate=200,
        turn_acceleration=200,
    )
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.arc(580,85)
    DRIVE_BASE.settings(
        straight_speed=900,
        straight_acceleration=400,
        turn_rate=200,
        turn_acceleration=200,
    )
    await DRIVE_BASE.straight(175)
    await DRIVE_BASE.straight(-100)
    await DRIVE_BASE.turn(-60) 
    await DRIVE_BASE.arc(350,100)
    await DRIVE_BASE.straight(125)
    await DRIVE_LEFT.run_angle(360, -340)  # step 7 push leaves
    DRIVE_BASE.settings(
        straight_speed=100,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )
    await DRIVE_BASE.straight(200)
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )
    await DRIVE_BASE.straight(-40)  # step 10 back up from handle
    DRIVE_BASE.settings(
        straight_speed=900,
        straight_acceleration=900,
        turn_rate=200,
        turn_acceleration=200,
    )
    await DRIVE_BASE.turn(83)  # step 11 turn away from leaves
    await DRIVE_BASE.straight(800)  # step 12 go home
    """
    await DRIVE_BASE.straight(650)
    await DRIVE_BASE.turn(93) 
    await DRIVE_BASE.straight(550)
    await DRIVE_BASE.straight(-100)
    
    await DRIVE_BASE.straight(330)
    await DRIVE_BASE.turn(45)
    await DRIVE_BASE.arc(800,25)
    await DRIVE_BASE.straight(50)
    await DRIVE_LEFT.run_angle(360, -320)  # step 7 push leaves
    DRIVE_BASE.settings(
        straight_speed=100,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )
    await DRIVE_BASE.straight(200)
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )
    await DRIVE_BASE.straight(-40)  # step 10 back up from handle
    await DRIVE_BASE.turn(81)  # step 11 turn away from leaves
    await DRIVE_BASE.straight(800)  # step 12 go home
"""
if __name__ == "__main__":
    run_task(M6_M11())
