from pybricks.tools import multitask, run_task, wait
from library import set_drivebase
from robot_config import DRIVE_BASE, DRIVE_LEFT, DRIVE_RIGHT, LEFT_ATTACHMENT, RIGHT_ATTACHMENT

async def M7():
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=700,
		straight_acceleration=700,
		turn_rate=600,
		turn_acceleration=600,
	)
	DRIVE_BASE.use_gyro(True)
	#await DRIVE_BASE.straight(100)
	await DRIVE_BASE.curve(280,90)
	await DRIVE_BASE.straight(380)
	await DRIVE_BASE.curve(-500,90)

if __name__ == "__main__":
	run_task(M7())
