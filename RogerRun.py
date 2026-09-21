from pybricks.tools import run_task

from library import set_drivebase
from robot_config import DRIVE_BASE

async def test_run():
	DRIVE_BASE.use_gyro(True)
	await set_drivebase()
	DRIVE_BASE.settings(
		straight_speed=200,
		straight_acceleration=300,
		turn_rate=200,
		turn_acceleration=300,
	)
	print("Driving forward 100 mm")
	await DRIVE_BASE.straight(665)
	print("Turning left 52 degrees")
	await DRIVE_BASE.turn(-52)
	print("Turning opposite 52 degrees")
	await DRIVE_BASE.turn(52)
	#DRIVE_BASE.settings(straight_speed=1000, straight_acceleration=1000)
	print("Returning quickly")
	#await DRIVE_BASE.straight(1000)

	DRIVE_BASE.use_gyro(False)


if __name__ == "__main__":
	run_task(test_run())
