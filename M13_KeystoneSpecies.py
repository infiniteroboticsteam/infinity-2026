
from pybricks.tools import multitask, run_task, wait
from robot_config import DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT, DRIVE_LEFT

from library import set_drivebase
from robot_config import DRIVE_BASE


async def M13():
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=400,
        turn_rate=600,
        turn_acceleration=600,
    )
    DRIVE_BASE.use_gyro(True)
    
    await DRIVE_BASE.straight(720)
    await DRIVE_BASE.turn(43)
    await DRIVE_BASE.straight(120)
    await DRIVE_BASE.straight(-100)
    await DRIVE_LEFT.run_angle(100,60)
    
    await RIGHT_ATTACHMENT.run_angle(100,-60)
    await wait(500)
    await RIGHT_ATTACHMENT.run_angle(900,60)

    await DRIVE_BASE.straight(-110)
    
    await DRIVE_BASE.turn(15)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=400,
        turn_rate=600,
        turn_acceleration=100,
    )
    await RIGHT_ATTACHMENT.run_angle(100,-60)
    
    
    #await DRIVE_LEFT.run_angle(100,60)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(450)
    
    
if __name__ == "__main__":
    run_task(M13())