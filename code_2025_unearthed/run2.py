from pybricks.parameters import Color, Direction, Stop
from pybricks.tools import multitask, run_task, wait
from robot_config import FRONT_ATTACHMENT, DRIVE_BASE, HUB, CENTER_ATTACHMENT#, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


async def run2():
    CENTER_ATTACHMENT.reconfigure(Direction.COUNTERCLOCKWISE,gears=[12,36])
    FRONT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[28,36])
    DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
    DRIVE_BASE.use_gyro(True)
    await wait(300)

    await DRIVE_BASE.straight(285)    
    await DRIVE_BASE.turn(53)
    await DRIVE_BASE.straight(230)
    #turn shopping stall and flip scale
    await multitask(FRONT_ATTACHMENT.run_angle(180,110,then=Stop.COAST),
                    CENTER_ATTACHMENT.run_angle(180,110))
    await CENTER_ATTACHMENT.run_angle(180,-90)
    #return
    #pullback stall roof
    DRIVE_BASE.settings(straight_speed=250, straight_acceleration=300)
    await DRIVE_BASE.turn(-90)
    #await DRIVE_BASE.straight(-10)
    await DRIVE_BASE.turn(90)
    await DRIVE_BASE.straight(20)

    await CENTER_ATTACHMENT.run_angle(180,90)
    await DRIVE_BASE.straight(-300)
    await CENTER_ATTACHMENT.run_angle(180,-30) 
    await DRIVE_BASE.straight(100)
    await CENTER_ATTACHMENT.run_angle(180,-60)
    DRIVE_BASE.settings(straight_speed=700, straight_acceleration=700)
    #await DRIVE_BASE.arc(radius=400, distance=-300)
    #await DRIVE_BASE.straight(-300)
    await DRIVE_BASE.arc(radius=750, distance=-600)

    DRIVE_BASE.use_gyro(False) 


if __name__ == "__main__":
    run_task(run2())
