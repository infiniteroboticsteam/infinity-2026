from pybricks.tools import multitask, run_task
from library import set_drivebase
from robot_config import DRIVE_BASE, RIGHT_ATTACHMENT

async def M3_M4():
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
    await RIGHT_ATTACHMENT.run_angle(180, -100)
    await DRIVE_BASE.straight(500)
    await DRIVE_BASE.straight(-200)

    # Step 3: Reset the drivebase for a faster, more controlled approach.
    print("Step 3: Resetting drive base for the next movement")
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=800,
        straight_acceleration=1000,
        turn_rate=300,
        turn_acceleration=600,
    )

    # Step 4: Turn and drive toward the rock, then align for the flip.
    print("Step 4: Turning and driving toward the rock")
    await DRIVE_BASE.turn(30)
    await DRIVE_BASE.straight(530)
    await DRIVE_BASE.turn(-77.777)

    # Step 5: Slow down for precise attachment motion and contact with the rock.
    print("Step 5: Adjusting speed for precise rock flip")
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=100,
        straight_acceleration=100,
        turn_rate=300,
        turn_acceleration=600,
    )
    print("Starting attachment +160")
    await RIGHT_ATTACHMENT.run_angle(180, 90)
    print("Attachment +160 done")
    await DRIVE_BASE.straight(260)
    print("Drive 260 done")
    await RIGHT_ATTACHMENT.run_angle(180, -100)
    print("Attachment -100 done")

    # Step 6: Return to a better position and finish the mission route.
    print("Step 6: Exiting the mission area and completing the run")
    await set_drivebase()
    DRIVE_BASE.settings(
        straight_speed=800,
        straight_acceleration=1000,
        turn_rate=300,
        turn_acceleration=600,
    )
    #await DRIVE_BASE.straight(440)
    #await DRIVE_BASE.turn(-90)
    await DRIVE_BASE.curve(-350, -160)
if __name__ == "__main__":
    run_task(M3_M4())
