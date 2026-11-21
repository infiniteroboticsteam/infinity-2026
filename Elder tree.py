from pybricks.parameters import Color, Direction, Stop
from pybricks.tools import multitask, run_task, wait
from robot_config import RIGHT_ATTACHMENT, DRIVE_BASE, HUB, LEFT_ATTACHMENT


async def run2():
    LEFT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,36])
    RIGHT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,36])
    DRIVE_BASE.settings(straight_speed=600, straight_acceleration=600)
    DRIVE_BASE.use_gyro(True)
    await wait(300)

    await multitask (DRIVE_BASE.straight(390), RIGHT_ATTACHMENT.run_angle(600,-10))

    #await wait(5)
    await DRIVE_BASE.arc(370,25,None)
    #await DRIVE_BASE.straight(2)
    #await RIGHT_ATTATCHMENT.
    await multitask (LEFT_ATTACHMENT.run_angle(600,30),
                     RIGHT_ATTACHMENT.run_angle(600,-20))
    #await LEFT_ATTACHMENT.run_angle(100,40)
    return
    await DRIVE_BASE.straight(-60)
    await DRIVE_BASE.straight(50)
    await DRIVE_BASE.turn(-21)  
    await DRIVE_BASE.turn(1)

    await DRIVE_BASE.straight(-200)
    #await DRIVE_BASE.turn(15)
    

    await multitask(LEFT_ATTACHMENT.run_angle(600,-20),
                    RIGHT_ATTACHMENT.run_angle(600,50))
    #await multitask(DRIVE_BASE.turn(-15), LEFT_ATTACHMENT.run_angle(600,-20))
    #await LEFT_ATTACHMENT.run_angle(600,-0)
    await DRIVE_BASE.straight(-290)
    #await DRIVE_BASE.straight(-100)
    return
    await DRIVE_BASE.turn(-20) 
    await RIGHT_ATTACHMENT.run_angle(600,-30)
    #await wait(500)
    await multitask (DRIVE_BASE.straight(290),
                    LEFT_ATTACHMENT.run_angle(600,-200))
    await DRIVE_BASE.turn(-10)
    await DRIVE_BASE.straight(100)
    await DRIVE_BASE.turn(27)
    await multitask (DRIVE_BASE.straight(260), 
                     RIGHT_ATTACHMENT.run_angle(600,-20))
    await RIGHT_ATTACHMENT.run_angle(600,95)
    await RIGHT_ATTACHMENT.run_angle(600,-95)
    await DRIVE_BASE.straight(-800)

    DRIVE_BASE.use_gyro(False) 


if __name__ == "__main__":
    run_task(run2())
