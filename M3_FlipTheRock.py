from pybricks.tools import multitask, run_task
from library import set_drivebase
from robot_config import DRIVE_BASE, RIGHT_ATTACHMENT

async def M3():
    # Step 1: Start the robot with gyro control and base settings for the mission.
    print("Step 1: Initializing drive base and gyro settings")
    DRIVE_BASE.use_gyro(True)
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=500,
        straight_acceleration=300,
        turn_rate=100,
        turn_acceleration=400,
    )

    # Step 2: Move into position and prepare the attachment to flip the rock.
    print("Step 2: Moving into position to flip the rock")
    await DRIVE_BASE.straight(300)
    await multitask(
        DRIVE_BASE.straight(-300),
        RIGHT_ATTACHMENT.run_angle(1000, -90),

    )
    

if __name__ == "__main__":
    run_task(M3())
