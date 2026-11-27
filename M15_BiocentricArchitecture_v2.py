
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M15():
    DRIVE_BASE.use_gyro(True)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=300,
        turn_rate=500,
        turn_acceleration=400,
    )
    
  
    
    await DRIVE_BASE.curve(800,57)
    
    await RIGHT_ATTACHMENT.run_angle(500,77)
    await DRIVE_BASE.curve(-50,54)
    #await DRIVE_BASE.curve(90,5)
    await DRIVE_BASE.straight(140)
    await wait(1000)
    await DRIVE_BASE.straight(-50)
    await DRIVE_BASE.turn(30)
    await DRIVE_BASE.curve(-1000,50)
    #await DRIVE_RIGHT.run_angle(360, 260)

    """
    await DRIVE_BASE.straight(85)
    
    await DRIVE_BASE.straight(-55)
    await DRIVE_BASE.turn(30)
    await DRIVE_BASE.curve(-1000,50)
   """
if __name__ == "__main__":
    run_task(M15())