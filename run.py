from pybricks.parameters import Color, Direction, Stop
from pybricks.tools import multitask, run_task, wait
from robot_config import RIGHT_ATTACHMENT, DRIVE_BASE, HUB, LEFT_ATTACHMENT


async def TEST():
    LEFT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,36])
    RIGHT_ATTACHMENT.reconfigure(Direction.CLOCKWISE,gears=[12,36])
    DRIVE_BASE.settings(straight_speed=600, straight_acceleration=600)
    DRIVE_BASE.use_gyro(True)
    await wait(300)

    await multitask(LEFT_ATTACHMENT.reset_angle(45),RIGHT_ATTACHMENT.reset_angle(45))
    await DRIVE_BASE.use_gyro(False) 
    
    
    if __name__ == "__main__":
        run_task(TEST())