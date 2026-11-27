from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M9():
    
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=400,
        straight_acceleration=400,
        turn_rate=500,
        turn_acceleration=400,
    )
    DRIVE_BASE.use_gyro(True)
    await DRIVE_BASE.arc(-750,-52)
    await DRIVE_LEFT.run_angle(300,-220)
        
    await DRIVE_BASE.straight(-500)
    await DRIVE_BASE.straight(40)
    await DRIVE_BASE.straight(-30)
    await DRIVE_BASE.straight(150)
    await DRIVE_BASE.turn(40)
    await DRIVE_BASE.straight(800)


    
    
if __name__ == "__main__":
    run_task(M9())