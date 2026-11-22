
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
        turn_rate=100,
        turn_acceleration=400,
    )
    
    await DRIVE_BASE.straight(460)
    await DRIVE_BASE.turn(45)
    #The one was 300
    await DRIVE_BASE.straight(290)
    await RIGHT_ATTACHMENT.run_angle(100,75)
    await DRIVE_RIGHT.run_angle(360, 193)
    await DRIVE_BASE.straight(85)
    
    await DRIVE_BASE.straight(-55)
    await DRIVE_BASE.turn(38)
    #await DRIVE_BASE.straight(-220)
    
    #await RIGHT_ATTACHMENT.run_angle(75, -195)
    await DRIVE_BASE.curve(-1000,50)
    #await DRIVE_BASE.curve(-900, 50),
    #await DRIVE_BASE.straight(-800)
    #await RIGHT_ATTACHMENT.run_angle(360,  290)
    #await DRIVE_BASE.turn(45)
    #await multitask(
    #        RIGHT_ATTACHMENT.run_angle(360,  -270),
    #        DRIVE_BASE.curve(-900, 50),
    #)
    """
    await multitask(
            RIGHT_ATTACHMENT.run_angle(360, 180),
     
    )

    await DRIVE_BASE.turn(-48)
    await wait(1500)
    await DRIVE_BASE.straight(130)
    await RIGHT_ATTACHMENT.run_angle(360, -60)
    await DRIVE_BASE.curve(-350, -160)
    """
if __name__ == "__main__":
    run_task(M15())