

from pybricks.tools import multitask, run_task, wait

from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT


#WHEEL_DIAMETER = 56
#ONE_WHEEL_ROTATION = pi * WHEEL_DIAMETER


async def ArmReset():
	#RIGHT_ATTACHMENT.run_target(360, 29) M12 Arm Reset Position
	await multitask(
		LEFT_ATTACHMENT.run_target(360, 44),
		RIGHT_ATTACHMENT.run_target(360, 29),
	)
	#await DRIVE_BASE.curve(-200, 70)
	#await DRIVE_BASE.straight(800)
	"""
	
	await DRIVE_BASE.turn(-60)
	await DRIVE_BASE.straight(-800)
	"""

	#print("Driving forward one wheel rotation")
	#await DRIVE_BASE.straight(ONE_WHEEL_ROTATION)
	#print("Driving backward one wheel rotation")
	#await DRIVE_BASE.straight(-ONE_WHEEL_ROTATION
	#await DRIVE_BASE.straight(300)
	#await DRIVE_BASE.straight(-300)
	#await DRIVE_BASE.turn(90)
	#await DRIVE_BASE.straight(100)

if __name__ == "__main__":
	run_task(ArmReset())
