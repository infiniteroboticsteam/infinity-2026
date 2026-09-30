from pybricks.parameters import Color
from pybricks.tools import run_task, wait,multitask
from pybricks.parameters import Axis, Direction, Port
from robot_config import HUB, CENTER_ATTACHMENT, FRONT_ATTACHMENT, DRIVE_BASE
from library import set_drivebase

from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Direction, Port
#CENTER_ATTACHMENT = Motor(Port.D, Direction.COUNTERCLOCKWISE, gears=[20,40])


async def run6():
    await HUB.speaker.beep()
    DRIVE_BASE.use_gyro(True) 
    
    await DRIVE_BASE.straight(175)

    await DRIVE_BASE.turn(37.5)
    await DRIVE_BASE.straight(225)
    #await DRIVE_BASE.straight(400)
    wait(500)
    await DRIVE_BASE.straight(-300)


    DRIVE_BASE.use_gyro(False) 

if __name__ == "__main__":
    run_task(run6())
