from pybricks.parameters import Color, Direction, Stop
from pybricks.tools import multitask, run_task, wait
from robot_config import RIGHT_ATTACHMENT, DRIVE_BASE, HUB, LEFT_ATTACHMENT


async def run2():
    LEFT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,36])
    RIGHT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,36])
    DRIVE_BASE.settings(straight_speed=600, straight_acceleration=600)
    DRIVE_BASE.use_gyro(True)
    await wait(300)

    await multitask (DRIVE_BASE.straight(410), RIGHT_ATTACHMENT.run_angle(600,-20))

    #await wait(5)
    await DRIVE_BASE.arc(320,25,None)
    await DRIVE_BASE.straight(2)
    #await RIGHT_ATTATCHMENT.
    await multitask (LEFT_ATTACHMENT.run_angle(600,40),
                     RIGHT_ATTACHMENT.run_angle(600,-30))
    #await LEFT_ATTACHMENT.run_angle(100,40)
    await DRIVE_BASE.straight(-50)
    await DRIVE_BASE.straight(35)
    await DRIVE_BASE.turn(-22)
    await DRIVE_BASE.straight(-185)
    await DRIVE_BASE.turn(15)
    

    await multitask(LEFT_ATTACHMENT.run_angle(600,-20),
                    RIGHT_ATTACHMENT.run_angle(600,50))
    await multitask(DRIVE_BASE.turn(-15),
                    LEFT_ATTACHMENT.run_angle(600,-20))
    await DRIVE_BASE.straight(-300)

    DRIVE_BASE.use_gyro(False) 


if __name__ == "__main__":
    run_task(run2())
